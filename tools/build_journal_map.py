#!/usr/bin/env python3
"""从「期刊缩写数据.txt」生成 index.html 里的 BIB_JOURNAL_MAP。

数据源：同级目录的 期刊缩写数据.txt（Python dict 语法，带分组注释）
用法：  python3 tools/build_journal_map.py            # 写回 index.html
        python3 tools/build_journal_map.py --check    # 只校验是否已同步，不写文件
方向是**单向**的：txt → 生成 → index.html。网页把整张表内联在 JS 里，
运行时**不读取** txt / 不依赖任何外部数据文件；txt 与 tools/ 删掉也不影响网页。
注：查表时代码会把输入转小写，所以这里输出的键一律小写；
    txt 里 "# INSPIRE 写 xxx" 的标注只是给人看的，不写进 JS。
"""
import re
import sys
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
TXT = REPO / '期刊缩写数据.txt'
HTML = REPO / 'index.html'
CHECK = '--check' in sys.argv


def parse_txt(path):
    """-> [(组名, [(键, 值, 注释)])]"""
    groups, cur = [], None
    for line in path.read_text(encoding='utf-8').split('\n'):
        s = line.strip()
        m = re.match(r'#\s*=+\s*(.+?)\s*=+\s*$', s)
        if m:
            cur = (m.group(1), [])
            groups.append(cur)
            continue
        m = re.match(r'"((?:[^"\\]|\\.)*)"\s*:\s*"((?:[^"\\]|\\.)*)"\s*,?\s*(#.*)?$', s)
        if m and cur is not None:
            key, val, note = m.group(1), m.group(2), (m.group(3) or '').strip()
            note = note.lstrip('#').strip()
            if note.startswith('INSPIRE 写'):        # 只标注给人看，不进 JS
                note = ''
            cur[1].append((key, val, note))
    return [(g, items) for g, items in groups if items]


def js_str(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


def build_block(groups):
    out = ['    const BIB_JOURNAL_MAP = {']
    for gname, items in groups:
        out.append(f'        // === {gname} ===')
        for key, val, note in items:
            line = f'        {js_str(key.lower())}: {js_str(val)},'
            if note:
                line += f'   // {note}'
            out.append(line)
        out.append('')
    while out[-1] == '':
        out.pop()
    out.append('    };')
    return '\n'.join(out)


def main():
    groups = parse_txt(TXT)
    n = sum(len(items) for _, items in groups)
    block = build_block(groups)
    html = HTML.read_text(encoding='utf-8')
    m = re.search(r'    const BIB_JOURNAL_MAP = \{.*?\n    \};', html, re.S)
    if not m:
        sys.exit('✗ index.html 里找不到 BIB_JOURNAL_MAP')
    if html[m.start():m.end()] == block:
        print(f'✓ 已同步（{n} 条 / {len(groups)} 组），无需改动')
        return
    if CHECK:
        sys.exit(f'✗ 不同步：txt 有 {n} 条，index.html 需要重新生成（去掉 --check 运行即可）')
    HTML.write_text(html[:m.start()] + block + html[m.end():], encoding='utf-8')
    print(f'✓ 已写入 index.html：{n} 条 / {len(groups)} 组')

    # 回读校验
    html2 = HTML.read_text(encoding='utf-8')
    block2 = re.search(r'    const BIB_JOURNAL_MAP = \{.*?\n    \};', html2, re.S).group(0)
    got = re.findall(r"'\s*((?:[^'\\]|\\.)*)'\s*:\s*'((?:[^'\\]|\\.)*)'", block2)
    want = [(k.lower(), v) for _, items in groups for k, v, _ in items]
    if got != want:
        missing = [w for w in want if w not in got]
        extra = [g for g in got if g not in want]
        sys.exit(f'✗ 回读校验失败：缺 {missing[:5]} 多 {extra[:5]}')
    print(f'✓ 回读校验通过（{len(got)} 条键值一致）')


if __name__ == '__main__':
    main()

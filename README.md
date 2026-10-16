# 学术文献工作台

一个面向电脑端文献整理流程的在线工作台，帮助研究人员快速获取文献全文、BibTeX 引用信息，并在浏览器本地维护待导出的引用库。

功能覆盖：DOI查询、标题/作者搜索、批量处理、BibTeX导出、引用预览。

## 功能特性

### 📋 核心功能

- 🔍 **InspireHEP (优先)** — 通过DOI自动获取BibTeX引用，期刊已标准缩写，优先使用InspireHEP API
- 🔗 **doi.org BibTeX** — 从 doi.org 官方内容协商取 BibTeX（`Accept: application/x-bibtex`），页面内按 bibtex.org/Convert 的规则重排（固定字段序、默认去 abstract/copyright/keywords、url/month/pages 规范化、scholar 风格 citation key），journal 缩写按 **INSPIRE 的写法**取（先用 DOI 查 INSPIRE 文献库，查不到再用记录里的 ISSN 查 INSPIRE 期刊库；都没有才用本地表《期刊缩写数据.txt》合并进来的 102 条映射表，如 `Physical Review C` → `Phys. Rev. C`），并把 APS 常见的 MathML title 转成可读 LaTeX（`$^{254}\mathrm{No}$`、`$\mu$`、`$T_c$`）；支持一次多个 DOI 或 arXiv ID
- ⚡ **APS 全文自动回退** — 先尝试并验证历史 Harvest `/fulltext` PDF；失败后回退到 APS 官网 PDF（`journals.aps.org/<刊名>/pdf/<DOI>`），无法识别期刊时再打开 DOI 落地页
- 🟢 **开放 PDF 查找** — 并行查询 Crossref 与 Semantic Scholar；读取候选文件首段并识别 `%PDF-` 文件签名，只有确认是真实 PDF 才自动打开，无法确认时仅显示候选链接
- 🤝 **科研通文献求助** — 一键打开 AbleSci 文献互助平台，结果区保留当前 DOI 便于提交求助
- 📚 **Sci-Hub 连通性检测** — 并行检测候选站点能否建立网络连接，找到可连接站点后打开；检测结果不代表站内已经加载 PDF
- 📖 **Library Genesis** — 数字图书馆资源搜索

### 🆕 高级功能

- **标题/作者搜索** — 按标题关键词、作者名、年份在 InspireHEP 中搜索；支持随时停止、15 秒自动超时和陈旧响应隔离，避免网络不稳定时一直停留在“搜索中”
- **批量DOI处理** — 自动规范化并去重 DOI，最多 3 路并发获取，支持取消任务与进度显示
- **本地引用库** — 待导出的条目自动保存在浏览器，可筛选、查看、复制 citation key、复制 BibTeX 或逐条删除
- **导入 .bib 合并** — 导入已有的.bib文件，自动按citation key去重合并
- **导出 .bib 文件** — 将所有已获取的条目合并导出为标准.bib文件
- **引用预览** — 将BibTeX条目渲染为 APS, Elsevier, 纯文本三种引用格式
- **arXiv识别** — 自动检测并显示arXiv ID和分类（如nucl-th）
- **DOI历史** — 最近查询的DOI自动保存，点击即可重新查询
- **智能DOI提取** — 从任意文本（URL、doi:标注、整段引用文字）中自动识别DOI
- **深色模式** — 右上角🌙/☀️切换，偏好自动保存

### 🎨 视觉

- **Three.js 3D背景** — 动态粒子星系 + 原子轨道环，鼠标跟随视角
- **实时时钟** — 页面顶部显示当前日期时间
- **桌面工作台布局** — 针对电脑端文献整理流程优化，常用入口无需折叠

## 使用方法

### DOI查询
1. 输入文献的DOI号（支持智能粘贴识别）
2. 选择需要的服务：
   - **APS 全文（自动回退）**：依次尝试 Harvest 旧 `/fulltext` 接口、APS 官网 PDF、DOI 落地页；Harvest 只有读到 `%PDF-` 文件签名才会使用
   - **查找开放 PDF**：从 Crossref 与 Semantic Scholar 查找候选，并验证响应是否为 PDF
   - **科研通文献求助**：打开 AbleSci，需要时提交 DOI 求助
   - **检测并打开 Sci-Hub**：先检测候选站点的网络连通性，再打开首个可连接站点；不判断站内 PDF 是否已加载
   - **LibGen搜索**：在Library Genesis中搜索
   - **获取BibTeX**：自动从InspireHEP获取（查不到时在新标签页打开doi2bib.org）
   - **doi.org BibTeX**：从 doi.org 官方内容协商取 BibTeX，页面内按 bibtex.org/Convert 的规则重排；journal 缩写按 INSPIRE 的写法取（先按 DOI 查 INSPIRE 文献库，查不到再用 ISSN 查 INSPIRE 期刊库，都没有才用本地表），title 里的 MathML 转成 LaTeX（如 `$^{254}\mathrm{No}$`）；支持一次填多个 DOI 或 arXiv ID（空格/换行分隔）
3. 获取到的BibTeX可直接复制，或添加到批量导出列表

### 全文入口的判定方式

- **开放 PDF / APS Harvest**：页面会读取候选文件首段，只有识别到 `%PDF-` 文件签名才判定为 PDF。跨域限制、权限错误、HTML 页面或超时均不会被误报为成功。
- **APS 自动回退**：Harvest 旧 `/fulltext` 接口验证失败后，自动打开 APS 官网 PDF；无法识别期刊路径时再回退到 DOI 落地页。APS 官网仍可能要求机构订阅，或显示站点自身的浏览器检查页面。
- **Sci-Hub 连通性**：仅使用浏览器的跨域网络请求判断候选站点能否建立连接，无法读取对方 HTTP 状态或确认站内 PDF，因此结果只代表网络连通性。

### 标题/作者搜索
1. 切换到「标题/作者搜索」标签页
2. 输入标题关键词、作者名、年份（可选）
3. 点击搜索，结果列表显示标题、作者、期刊、年份、arXiv
4. 搜索期间可点击「停止搜索」；超过 15 秒会自动结束并提示重试
5. 可查看BibTeX或直接添加到批量导出

### 批量获取
1. 切换到「批量DOI」标签页
2. 每行输入一个DOI
3. 点击「批量获取 BibTeX」，页面以最多 3 路并发处理，可随时取消
4. 重复 DOI 和引用库中已有条目会自动跳过
5. 完成后进入本地引用库，可检查、筛选并导出为 `.bib` 文件

### 导入已有.bib
在批量标签页点击「导入 .bib 合并」，选择已有bib文件，自动去重合并。

## 示例DOI

- `10.1103/PhysRevC.106.064325`
- `10.1103/PhysRevLett.133.022501`
- `10.1016/j.physletb.2025.140130`
- `10.1038/s41586-023-05899-8`

## 数据来源

- [InspireHEP](https://inspirehep.net/) — 高能物理文献数据库（优先）
- [doi.org](https://doi.org/) — DOI 官方内容协商（`Accept: application/x-bibtex`，302 到注册机构 Crossref/DataCite）；页面内按 bibtex.org/Convert 的规则重排，不经过第三方站点
- [doi2bib.org](https://www.doi2bib.org/) — BibTeX引用生成工具（回退）
- [APS 官网 PDF 直链](https://journals.aps.org/) — 按 DOI 直接下载 APS 全文（机构订阅 IP；`journals.aps.org/<刊名>/pdf/<DOI>`，DOI 大小写敏感）
- [APS Harvest](https://harvest.aps.org/docs/harvest-api) — `/fulltext` 作为历史兼容入口尝试；当前正式接口以内容协商和授权说明为准
- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) — 出版商全文链接元数据
- [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/api-docs/) — 开放获取全文候选
- [科研通（AbleSci）](https://www.ablesci.com/) — 文献互助平台
- [Sci-Hub](https://sci-hub.se/) — 开放获取文献
- [Library Genesis](https://libgen.gl/) — 数字图书馆

## 技术栈

- 纯HTML/CSS/JavaScript
- [Three.js](https://threejs.org/) — 3D粒子背景
- [InspireHEP API](https://inspirehep.net/api) — BibTeX数据源
- 桌面优先布局
- 数据存储在 localStorage

## 维护期刊缩写表

期刊缩写源数据保存在 `期刊缩写数据.txt`，网页运行时使用内联在 `index.html` 中的映射，不依赖该文本文件。修改源数据后执行：

```bash
python3 tools/build_journal_map.py
python3 tools/build_journal_map.py --check
```

## 部署说明

可直接用浏览器打开 `index.html`（file://协议），或部署到任意静态服务器。

GitHub Pages 部署：
```
https://[你的用户名].github.io/[仓库名称]/
```

## 许可证

MIT License

## 免责声明

本工具仅供学术研究使用，请遵守相关版权法律法规。

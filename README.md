# 学术文献获取工具

一个集成了多个学术资源平台的在线工具，帮助研究人员快速获取文献全文、BibTeX引用信息。

功能覆盖：DOI查询、标题/作者搜索、批量处理、BibTeX导出、引用预览。

## 功能特性

### 📋 核心功能

- 🔍 **InspireHEP (优先)** — 通过DOI自动获取BibTeX引用，期刊已标准缩写，优先使用InspireHEP API
- ⚡ **APS Harvest** — 美国物理学会官方全文平台
- 📚 **Sci-Hub** — 开放获取学术文献平台（自动检测可用域名）
- 📖 **Library Genesis** — 数字图书馆资源搜索

### 🆕 高级功能

- **标题/作者搜索** — 按标题关键词、作者名、年份在InspireHEP中搜索文献
- **批量DOI处理** — 粘贴多个DOI（每行一个），批量获取BibTeX，进度条显示
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
- **响应式设计** — 桌面/移动端自适应

## 使用方法

### DOI查询
1. 输入文献的DOI号（支持智能粘贴识别）
2. 选择需要的服务：
   - **APS Harvest**：查看官方全文
   - **Sci-Hub**：尝试免费下载文献
   - **LibGen搜索**：在Library Genesis中搜索
   - **获取BibTeX**：自动从InspireHEP获取（查不到时在新标签页打开doi2bib.org）
3. 获取到的BibTeX可直接复制，或添加到批量导出列表

### 标题/作者搜索
1. 切换到「标题/作者搜索」标签页
2. 输入标题关键词、作者名、年份（可选）
3. 点击搜索，结果列表显示标题、作者、期刊、年份、arXiv
4. 可查看BibTeX或直接添加到批量导出

### 批量获取
1. 切换到「批量DOI」标签页
2. 每行输入一个DOI
3. 点击「批量获取BibTeX」，进度条显示处理进度
4. 完成后自动加入批量列表，可导出为.bib文件

### 导入已有.bib
在批量标签页点击「导入 .bib 合并」，选择已有bib文件，自动去重合并。

## 示例DOI

- `10.1103/PhysRevC.106.064325`
- `10.1103/PhysRevLett.133.022501`
- `10.1016/j.physletb.2025.140130`
- `10.1038/s41586-023-05899-8`

## 数据来源

- [InspireHEP](https://inspirehep.net/) — 高能物理文献数据库（优先）
- [doi2bib.org](https://www.doi2bib.org/) — BibTeX引用生成工具（回退）
- [APS Harvest](https://harvest.aps.org/) — APS官方全文
- [Sci-Hub](https://sci-hub.se/) — 开放获取文献
- [Library Genesis](https://libgen.gl/) — 数字图书馆

## 技术栈

- 纯HTML/CSS/JavaScript
- [Three.js](https://threejs.org/) — 3D粒子背景
- [InspireHEP API](https://inspirehep.net/api) — BibTeX数据源
- 响应式设计
- 数据存储在 localStorage

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

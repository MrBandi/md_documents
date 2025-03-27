# Markdown 文件管理模組

<div align="right">
    <a href="/README_tw.md">中文</a> | <a href="/README.md">English</a>
</div>

<a id="chinese"></a>
### 模組概述
此模組允許在 Odoo 中建立並管理 Markdown 格式的文件。它提供了完整的文件分類、標籤管理和版本控制功能。模組名稱為 `md_documents`，由 MrBandi 所開發。

### 核心功能
- 建立和管理 Markdown 格式文件
- 文件分類與樹狀結構的類別管理
- 文件版本控制與修訂歷史
- 使用者權限與存取控制
- 文件預覽功能
- 文件標記（標籤）與搜尋

### 技術架構
此模組遵循 Odoo 標準的架構：

#### 模型 (Models)
- `my.document`: 主要文件模型，包含標題、內容、版本等字段
- `my.document.category`: 文件類別模型，支援階層式分類
- `my.document.tag`: 文件標籤模型，用於標記文件

#### 視圖 (Views)
- `document_views.xml`: 定義文件的表單、列表和搜尋視圖
- `document_category_views.xml`: 定義類別的樹狀結構和表單視圖
- `menu_views.xml`: 定義選單項目和結構
- `templates.xml`: 包含文件預覽模板

#### 控制器 (Controllers)
- 提供文件預覽功能
- 提供 Markdown 轉換 HTML 的 API

#### 安全設定 (Security)
- 定義模型的存取權限
- 設定規則與群組權限

#### 初始數據 (Data)
- 文件編號的序列設定

### 安裝與設定
1. 將模組複製到 Odoo 的自訂模組目錄中
2. 更新模組列表
3. 安裝「Markdown Documents」模組
4. 設定用戶權限

### 使用指南
模組安裝後，可以通過「Markdown Documents」選單進行以下操作：
1. 建立文件類別和子類別
2. 新增 Markdown 文件
3. 為文件加上標籤
4. 瀏覽和搜尋文件
5. 預覽文件內容

### 依賴項目
- `base`: Odoo 基礎模組
- `web_editor`: Odoo 網頁編輯器模組

### 授權資訊
此模組採用 LGPL-3 授權。

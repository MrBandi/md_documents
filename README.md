# Markdown Document Management Module

<div align="right">
    <a href="/README_tw.md">中文</a> | <a href="/README.md">English</a>
</div>

<a id="english"></a>
### Module Overview
This module allows creating and managing documents in Markdown format within Odoo. It provides comprehensive document classification, tag management, and version control features. The module name is `md_documents`.

### Core Features
- Create and manage documents in Markdown format
- Document classification with hierarchical category structure
- Document version control and revision history
- User permissions and access control
- Document preview functionality
- Document tagging and search capabilities

### Technical Architecture
This module follows the standard Odoo architecture:

#### Models
- `my.document`: Main document model containing fields for title, content, version, etc.
- `my.document.category`: Document category model supporting hierarchical classification
- `my.document.tag`: Document tag model for document labeling

#### Views
- `document_views.xml`: Defines form, list, and search views for documents
- `document_category_views.xml`: Defines tree structure and form views for categories
- `menu_views.xml`: Defines menu items and structure
- `templates.xml`: Contains document preview templates

#### Controllers
- Provides document preview functionality
- Provides API for Markdown to HTML conversion

#### Security
- Defines model access rights
- Sets up rules and group permissions

#### Initial Data
- Document numbering sequence configuration

### Installation and Setup
1. Copy the module to Odoo's custom module directory
2. Update the module list
3. Install the "Markdown Documents" module
4. Configure user permissions

### Usage Guide
After installation, you can perform the following operations through the "Markdown Documents" menu:
1. Create document categories and subcategories
2. Add Markdown documents
3. Tag documents
4. Browse and search documents
5. Preview document content

### Dependencies
- `base`: Odoo basic module
- `web_editor`: Odoo web editor module

### License Information
This module is licensed under LGPL-3.


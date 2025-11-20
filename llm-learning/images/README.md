# Images Directory

This directory stores images and diagrams for the Python Learning Repository.

## About Diagrams in This Repository

### Mermaid Diagrams

Most architecture diagrams in this repository use **Mermaid**, a markdown-compatible diagramming syntax that renders automatically on:

- ✅ **GitHub** - Renders natively
- ✅ **GitLab** - Renders natively  
- ✅ **VS Code** - With Markdown Preview Mermaid Support extension
- ✅ **Obsidian** - With Mermaid plugin
- ✅ **Notion** - Supports Mermaid blocks
- ✅ **Documentation sites** - Docusaurus, MkDocs, etc.

### Benefits of Mermaid

1. **Version Control Friendly** - Text-based, easy to diff
2. **No External Tools** - No need for draw.io, Lucidchart, etc.
3. **Auto-Rendering** - GitHub renders them automatically
4. **Easy to Edit** - Just edit text in markdown
5. **Professional Quality** - Beautiful diagrams

### Example Mermaid Syntax

\`\`\`mermaid
flowchart LR
    A[User] --> B[API]
    B --> C[Database]
    C --> B
    B --> A
\`\`\`

This renders as a flowchart automatically!

### Converting Mermaid to PNG/SVG (If Needed)

If you need standalone image files:

**Online:**
- Mermaid Live Editor: https://mermaid.live/
  - Paste your mermaid code
  - Export as PNG or SVG

**Command Line:**
```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Convert to PNG
mmdc -i diagram.mmd -o diagram.png

# Convert to SVG
mmdc -i diagram.mmd -o diagram.svg
```

**VS Code Extension:**
- Install "Markdown Preview Mermaid Support"
- Right-click on preview → "Export to PNG/SVG"

### Additional Images

Place any additional screenshots, photos, or generated images in this directory:

```
images/
├── README.md (this file)
├── architecture-overview.png (if exported)
├── langchain-flow.png (if exported)
├── mcp-architecture.png (if exported)
└── screenshot-*.png (any screenshots)
```

### File Naming Convention

Use descriptive names with hyphens:
- ✅ `langchain-rag-architecture.png`
- ✅ `mcp-protocol-flow.svg`
- ✅ `complete-system-diagram.png`
- ❌ `diagram1.png`
- ❌ `image.jpg`

---

**Note:** The main document `llm-application-architecture.md` uses Mermaid diagrams extensively, which will render automatically on GitHub without needing separate image files.


---
name: jupyter-notebooks
description: "Use when creating, editing, or manipulating Jupyter notebooks (.ipynb) programmatically."
category: tech
displayName: Jupyter Notebooks
color: orange
triggers:
  - notebook
  - jupyter
  - ipynb
  - colab
  - .ipynb
---

# Jupyter Notebooks

You are an expert at creating, editing, and manipulating Jupyter notebooks programmatically.

## 🚀 ANALYZE BEFORE ACTING

**Always detect the context first:**
1. **Operation**: Creating a new notebook, editing an existing one, or converting?
2. **Platform**: Standard Jupyter, Google Colab, or JupyterLab?
3. **Content**: Data science, ML training, documentation, or tutorial?

---

## 📐 Notebook Structure

A `.ipynb` file is JSON with this structure:

```json
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {"provenance": []},
    "kernelspec": {"name": "python3", "display_name": "Python 3"}
  },
  "cells": []
}
```

---

## 🛡️ CORE RULES

### 1. Cell Source Format
- `source` is an **array of strings**, each ending with `\n` (except possibly the last).
- **NEVER** use a single string for `source`.
- Example: `["print('hello')\n", "print('world')"]`

### 2. JSON Escaping
When writing notebook JSON:
- Escape quotes: `\"`
- Escape literal newlines in strings: `\\n`
- Escape backslashes: `\\`
- Array newlines (line breaks between source items): `\n`

### 3. Cell IDs
- Every cell **must** have a unique `metadata.id`.
- Use descriptive IDs: `"install_deps"`, `"train_model"`, `"plot_results"`.

### 4. Cell Types

**Markdown Cell:**
```json
{
  "cell_type": "markdown",
  "source": [
    "# My Notebook\n",
    "\n",
    "Description here.\n"
  ],
  "metadata": {"id": "intro"}
}
```

**Code Cell:**
```json
{
  "cell_type": "code",
  "source": [
    "import torch\n",
    "import numpy as np\n",
    "\n",
    "print('Ready!')\n"
  ],
  "metadata": {"id": "imports"},
  "execution_count": null,
  "outputs": []
}
```

---

## 🔧 Editing Notebooks

### Safe Edit Pattern
```python
import json

# Read
with open('notebook.ipynb', 'r') as f:
    nb = json.load(f)

# Find cell by ID
for cell in nb['cells']:
    if cell.get('metadata', {}).get('id') == 'target_id':
        # Modify cell['source']
        break

# Write back
with open('notebook.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
```

### Insert Cell
```python
new_cell = {
    "cell_type": "code",
    "source": ["# new code\n"],
    "metadata": {"id": "new_cell"},
    "execution_count": None,
    "outputs": []
}
nb['cells'].insert(index, new_cell)
```

### Delete Cell
```python
nb['cells'] = [c for c in nb['cells']
               if c.get('metadata', {}).get('id') != 'cell_to_delete']
```

---

## 📦 Common Patterns

### Setup Cell
```json
["#@title Setup\n",
 "!pip install -q package1 package2\n",
 "\n",
 "import package1\n",
 "import package2\n",
 "\n",
 "print('✓ Setup complete')\n"]
```

### Config Cell (Colab Forms)
```json
["#@title Configuration { display-mode: \"form\" }\n",
 "\n",
 "MODEL_NAME = \"gpt2\"  #@param {type:\"string\"}\n",
 "BATCH_SIZE = 32  #@param {type:\"integer\"}\n",
 "USE_GPU = True  #@param {type:\"boolean\"}\n"]
```

### Colab Form Field Syntax
```python
"#@title Cell Title { display-mode: \"form\" }\n"
"param = \"default\"  #@param {type:\"string\"}\n"
"number = 10  #@param {type:\"integer\"}\n"
"flag = True  #@param {type:\"boolean\"}\n"
"choice = \"A\"  #@param [\"A\", \"B\", \"C\"]\n"
```

### Progress Display
```json
["from tqdm.notebook import tqdm\n",
 "\n",
 "for i in tqdm(range(100)):\n",
 "    # work\n",
 "    pass\n"]
```

### Collapsible Sections (Colab)
Use `#@title` on code cells — they become collapsible when run.

---

## ✅ QUALITY CHECKLIST

Before finalizing a notebook:

- [ ] All cells have **unique IDs**
- [ ] Markdown cells have proper headers and formatting
- [ ] Code cells are **logically ordered**
- [ ] Imports are at the top or in a setup cell
- [ ] Config values use Colab form fields where appropriate
- [ ] Error handling for common failures
- [ ] Clear output messages (`✓` for success, `⚠️` for warnings)
- [ ] Section dividers between major parts

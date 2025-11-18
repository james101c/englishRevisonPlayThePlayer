# English Assignment Assistant

A Python tool to save and manage suggestions and prompts for English assignments.

## Features

- **Save Suggestions**: Store writing tips, grammar rules, and style recommendations
- **Save Prompts**: Keep track of writing prompts and assignment ideas
- **Categorize**: Organize items by category (grammar, style, creative-writing, analysis, etc.)
- **View History**: List all saved suggestions and prompts with timestamps
- **Filter by Category**: View items from specific categories

## Installation

No installation required! Just Python 3.6+ is needed.

## Usage

### Add a Suggestion

```bash
python english_assistant.py add-suggestion "Your suggestion text" [category]
```

Example:
```bash
python english_assistant.py add-suggestion "Use active voice for stronger writing" grammar
```

### Add a Prompt

```bash
python english_assistant.py add-prompt "Your prompt text" [category]
```

Example:
```bash
python english_assistant.py add-prompt "Write about a childhood memory" creative-writing
```

### List All Items

```bash
python english_assistant.py list-all
```

### List Suggestions

```bash
python english_assistant.py list-suggestions [category]
```

Examples:
```bash
python english_assistant.py list-suggestions          # All suggestions
python english_assistant.py list-suggestions grammar  # Only grammar suggestions
```

### List Prompts

```bash
python english_assistant.py list-prompts [category]
```

### View Categories

```bash
python english_assistant.py categories
```

## Data Storage

All data is stored in `english_data.json` in the same directory. This file is automatically created and updated as you add items.

## Example Workflow

```bash
# Add some writing tips
python english_assistant.py add-suggestion "Avoid redundant adjectives" grammar
python english_assistant.py add-suggestion "Show, don't tell" style

# Add assignment prompts
python english_assistant.py add-prompt "Describe a perfect day" creative-writing
python english_assistant.py add-prompt "Compare two poems' themes" analysis

# View everything
python english_assistant.py list-all

# View only grammar suggestions
python english_assistant.py list-suggestions grammar
```

## Categories

Common categories you might use:
- `grammar` - Grammar rules and tips
- `style` - Writing style recommendations
- `creative-writing` - Creative writing prompts
- `analysis` - Analysis and critical thinking prompts
- `general` - General suggestions or prompts (default)

You can create your own categories as needed! 

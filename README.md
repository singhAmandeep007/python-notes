## Requirements

- Python 3.11 or above

## How to setup Poetry on mac-OS vscode ?

1. Install poetry `curl -sSL https://install.python-poetry.org | python3 -`
2. Add path to poetry `export PATH="/Users/<username>/.local/bin:$PATH"` in `.zshrc`
3. cd to project directory and run `poetry install`
4. Make sure to add path to virtualenvs created by poetry in vscode settings.json `"python.venvPath": "~/Library/Caches/pypoetry/virtualenvs"`
5. Install python version >= python version mentioned under `[tool.poetry.dependencies]` in `pyproject.toml`.
6. Activate virtual environment `poetry shell`
7. Select python interpreter which is in virtual environment created by poetry in vscode.

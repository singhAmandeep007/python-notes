## How to setup on mac-OS vscode ?

1. Install poetry `curl -sSL https://install.python-poetry.org | python3 -`
2. Add path to poetry `export PATH="/Users/<username>/.local/bin:$PATH"` in `.zshrc`
3. cd to project directory and run `poetry install`
4. Make sure to add path to virtualenvs created by poetry in vscode settings.json `"python.venvPath": "~/Library/Caches/pypoetry/virtualenvs"`
5. Install python version >= python version mentioned under `[tool.poetry.dependencies]` in `pyproject.toml`.
6. Activate virtual environment `poetry shell`
7. Select python interpreter which is in virtual environment created by poetry in vscode.

## How to run get_weather.py ?

1. cd into weather directory
2. Run `poetry run python get_weather.py --lat=44.34 --lng=10.99`
   1. Note: lat and lng defaults to New York if not provided.

## How to run tests ?

1. cd into weather directory
2. Run `poetry run pytest -vv -s`

## How to run formatter ?

1. cd into weather directory
2. Run `poetry run black .`

## Weather API

1. Call current Weather data Eg. https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}

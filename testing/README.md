## Setup

1. [Poetry](../README.md)

## Linting

- To execute linting on any file
  - ` pylint filename.py --rcfile="pylintrc"`
- To execute linting on a directory
  - ` pylint directoryname --rcfile="pylintrc"`

## Testing

- To execute all tests
  - `pytest folder -vv -s`
- To execute tests on any file
  - `pytest folder/filename.py -vv`
- To execute tests which marked as slow
  - `pytest -m slow -vv`
- To execute a specific test
  - `pytest -k test_function_name -vv`

## Profiling Tests

- To get a list of the slowest 10 test durations over 1.0s long:
  - `pytest --durations=10 --durations-min=1.0 -vv`

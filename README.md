# find-my-number

![alt text](image.png)

Given the above keypad find all 10 key sequences that can be keyed in given the following
constraints:

1. The initial keypress can be any key.
2. Each subsequent keypress must be a knight move from the previous key.
3. There can be at most 2 vowels in the sequence.

A knight move is defined as either of the following:

- Move two keys vertically and one horizontally.
- Move two keys horizontally and one vertically.

As a follow up task, can you please work out the answer to the same question however this time the allowed moves are bishop moves.

A Bishop move is defined as follows:

- Diagonally in any direction
- Any distance is acceptable as long as you are not off the board.

# Useage

Before running ensure you have uv installed (can be downloaded from the company store - but will need a S4 reboot)

## To initialise the project please run

```
uv sync
```

## To run please use

```
uv run main.py
```

## To run the python tests please use

```
uv run pytest -s --cov .
```

## To run a linting check please run

```
uvx ruff check .
```

## To run a type checker please run

```
uvx ty check .
```

To run without uv please run the following commands (reccomended method is to create a virtual environment)

## Create and activate Virtual environment

```
python -m venv venv
venv/Scripts/activate
```

## install dependencies

```
pip install pytest
pip install pytest-cov
```

## run without uv please use

```
python main.py
```

## To run the python tests without please use

```
pytest -s --cov .
```

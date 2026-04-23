# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workflow

After every meaningful change, commit with a clean message and push to GitHub (`agferb/beginning`, `master` branch).

## Running code

```bash
# Run the pi calculator (default 50 digits)
python calculate_pi.py

# Run with custom digit count
python calculate_pi.py 100

# Open the Tic Tac Toe game
start tictactoe.html
```

## Math operations

Prefer `numpy` methods over Python builtins or the `math` module for all mathematical operations (e.g. `np.sqrt`, `np.ceil`).

## Project structure

This is a small exploratory/learning repo with standalone files — no shared modules or build system:

- `calculate_pi.py` — Computes π using the Chudnovsky algorithm. Uses Python's `decimal` module for arbitrary precision. Note: currently uses `math.ceil` — prefer `np.ceil` for new math code.
- `tictactoe.html` — Self-contained single-file browser game (HTML + CSS + JS). Supports 2-player and vs-computer (minimax-lite AI) modes.
- `test_cursor.py` — Scratch/experimental file using `numpy`.

## Dependencies

- Python stdlib only for `calculate_pi.py` (plus `numpy` if refactored)
- `numpy` for `test_cursor.py` (`pip install numpy`)
- No package manager or virtual environment is configured

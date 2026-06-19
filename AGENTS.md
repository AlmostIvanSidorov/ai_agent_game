# AGENTS.md

## Running the game

```bash
source setvar.sh   # sets SCREEN_WIDTH=800, SCREEN_HEIGHT=800
pip install -r requirements.txt
python ncb.py
```

- `SCREEN_WIDTH` / `SCREEN_HEIGHT` env vars default to 900×700 in `game_classes.py:16-17` if unset. `setvar.sh` overrides to 800×800.
- Always run from the repo root. All sprite/audio paths are hardcoded as `sprites/...` relative paths.

## Architecture

- `ncb.py` — entry point. Main game loop, menu rendering, event handling, collision logic.
- `game_classes.py` — `Player`, `Enemy`, `Cloud` sprite classes. Also exports `screen_width`, `screen_height`, `shutdown_func`, and pygame constants (`RLEACCEL`, `K_*`, `KEYDOWN`, `QUIT`).
- `ncb.py` uses `from game_classes import *` — changes to game_classes exports silently affect ncb.py.
- `shutdown_func` is defined but never called in the current codebase.

## Game state

- Three-state machine: `menu` → `playing` → `game_over` → `playing` (restart) or exit.
- Player has 3 lives; hit triggers 60-frame invincibility with blink effect.

## Dependencies

- Only `pygame==2.6.1` (pinned in `requirements.txt`). No other packages.

## Testing

- No test suite exists.

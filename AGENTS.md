# AGENTS.md

## Running the game

```bash
source setvar.sh   # sets SCREEN_WIDTH=800, SCREEN_HEIGHT=600
pip install -r requirements.txt
python ncb.py
```

- `SCREEN_WIDTH` and `SCREEN_HEIGHT` env vars are **required** — `game_classes.py` reads them via `os.getenv()` with no defaults; missing values cause an immediate crash.
- Always run from the repo root. All sprite/audio paths are hardcoded as `sprites/...` relative paths.

## Architecture

- `ncb.py` — entry point. Main game loop, menu rendering, event handling.
- `game_classes.py` — `Player`, `Enemy`, `Cloud` sprite classes. Also exports `screen_width`, `screen_height`, `shutdown_func`, and pygame constants.
- `ncb.py` uses `from game_classes import *` — changes to game_classes exports silently affect ncb.py.

## Stale docs

- README references `GnomesCatsGame.py`; that file does not exist. The real entry point is `ncb.py`.

## Testing

- No test suite exists.

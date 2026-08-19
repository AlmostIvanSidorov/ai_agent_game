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

## Verification

```bash
pip install -r requirements.txt   # includes pytest
python -m pytest
```

- `tests/test_launch.py` is a smoke test: it runs `ncb.main()` under `SDL_VIDEODRIVER=dummy` / `SDL_AUDIODRIVER=dummy` with a QUIT timer, verifying pygame init, all sprite/audio loading, and a clean exit. It does not cover game logic.
- No lint or typecheck config exists.

## Sprite gotchas

- All sprites use a black colorkey `(0, 0, 0)` with `RLEACCEL`, except `heart.png` which uses white `(255, 255, 255)` (see `ncb.py` `main`). New sprites must match their actual background color.
- `ncb.py` additionally loads and re-scales cloud/naruto/kunai/heart surfaces itself for menus and the HUD; the classes in `game_classes.py` load the same PNGs unscaled for in-game sprites.

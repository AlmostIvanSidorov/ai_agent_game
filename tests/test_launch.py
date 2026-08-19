from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_game_launches_and_exits_cleanly(monkeypatch):
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")
    monkeypatch.setenv("SDL_AUDIODRIVER", "dummy")
    monkeypatch.setenv("SCREEN_WIDTH", "800")
    monkeypatch.setenv("SCREEN_HEIGHT", "800")
    monkeypatch.chdir(REPO_ROOT)

    import pygame

    import ncb

    pygame.init()
    pygame.time.set_timer(pygame.QUIT, 500)

    ncb.main()

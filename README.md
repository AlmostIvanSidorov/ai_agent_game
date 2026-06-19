# AI Agent Game

A simple arcade game where Naruto battle in the clouds!!!

## Description

This is a test game created to improve programming skills using Python and Pygame. The game features a player character (Naruto) navigating through the screen while avoiding incoming enemies (kunai) thrown by cats. The game includes sound effects, background music, and visual elements like clouds in the background.

## Game Concept

- Player character: Naruto
- Enemies: Kunai thrown by cats
- Objective: Avoid collisions with kunai for as long as possible
- Controls: Arrow keys to move Naruto up, down, left, and right
- Visuals: Sprites for Naruto, kunai, clouds, and background
- Audio: Background music (Naruto Theme), jumping sounds, and collision sounds

## Requirements

- Python 3.x
- Pygame library
- Various sound and image files in the sprites directory

## How to Run

1. Install required dependencies: `pip install -r requirements.txt`

2. Set environment variables for screen dimensions. Defaults are 900×700 if unset. Use `source setvar.sh` to set 800×800, or set manually: `SCREEN_WIDTH=800 SCREEN_HEIGHT=800`

3. Run the game: `python ncb.py`

## Files

- `ncb.py`: Main game loop and logic
- `game_classes.py`: Defines game classes (Player, Enemy, Cloud)
- `requirements.txt`: Python dependencies
- `sprites/`: Directory containing game assets (images and sounds)

## Controls

- Arrow keys (UP, DOWN, LEFT, RIGHT) to move Naruto
- Mouse click to interact with menu buttons (Start, Restart, Exit)
- ESC key to exit the game

## Features

- Menu screen with Start and Exit buttons
- Game Over screen with Restart and Exit buttons
- Player has 3 lives; getting hit triggers a brief invincibility period with blink effect
- Player movement with boundary checking
- Randomly generated enemies (kunai)
- Randomly generated clouds in background
- Sound effects for movement and collisions
- Background music (Naruto Theme)
- Collision detection between player and enemies

## Future Improvements

- Add AI for enemies to follow the player
- Add a visible scoring/survival time display
- Add power-ups
- Improve graphics and animations
- Add multiple levels

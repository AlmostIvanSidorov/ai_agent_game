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

2. Set environment variables for screen dimensions (e.g., SCREEN_WIDTH=800, SCREEN_HEIGHT=600)

3. Run the game: `python ncb.py`

## Files

- `GnomesCatsGame.py`: Main game loop and logic
- `game_classes.py`: Defines game classes (Player, Enemy, Cloud)
- `requirements.txt`: Python dependencies
- `sprites/`: Directory containing game assets (images and sounds)

## Controls

- Arrow keys (UP, DOWN, LEFT, RIGHT) to move Naruto
- ESC key to exit the game

## Features

- Player movement with boundary checking
- Randomly generated enemies (kunai)
- Randomly generated clouds in background
- Sound effects for movement and collisions
- Background music
- Collision detection between player and enemies
- Score tracking (based on survival time)

## Future Improvements

- Add AI for enemies to follow the player
- Implement scoring system
- Add power-ups
- Improve graphics and animations
- Add multiple levels

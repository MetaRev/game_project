# Top-Down Action RPG (Pygame)

This is a classic top-down action RPG built with Python and Pygame. Explore, fight monsters, use magic, and upgrade your character!

## Features
- Top-down action RPG gameplay
- Multiple enemy types with unique behaviors
- Player attacks and magic abilities
- Animated sprites and particle effects
- Audio: background music, attack, magic, and enemy sounds
- Upgrade system for player stats
- Interactive UI for health, energy, and experience

## Setup

### Requirements
- Python 3.8+
- [Pygame](https://www.pygame.org/) (install with `pip install pygame`)

### Installation
1. Clone or download this repository.
2. Ensure the following folder structure (key folders):
    - `code/` (main game code)
    - `graphics/` (sprites, tiles, particles)
    - `audio/` (sound effects and music)
    - `map/` (CSV map files)
3. Run the game:
    ```bash
    cd code
    python main.py
    ```

## Controls
- **Arrow Keys**: Move player
- **Space**: Attack
- **Left Ctrl**: Cast magic
- **Q**: Switch weapon
- **E**: Switch magic
- **M**: Toggle upgrade menu

## Notes
- Make sure all asset paths use backslashes (`\`) for Windows compatibility.
- Audio requires working `.wav` and `.ogg` files in the `audio/` directory.
- The game window size and other settings can be adjusted in `settings.py`.

## Credits
- Inspired by classic top-down action RPGs
- Sprites, audio, and code: [Your Name or Team]

---
Enjoy exploring and battling in your own action RPG world! 
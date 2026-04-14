<h1 align="center">2D Diamond Catcher</h1>

<p align="center">
	🎮 A fast, simple, and fun diamond-catching game built with PyOpenGL.<br>
	✨ Dodge, move, pause, restart, and chase a higher score.
</p>

---

## What You Get

This project is centered on the game itself, with a clean loop and interactive controls.

- 🎯 Manual midpoint line drawing implementation
- ⌨️ Keyboard and mouse driven controls
- 💎 Catch-the-diamond game loop with pause, restart, collision, and scoring
- 🚀 Speed scaling that keeps the game moving

---

## Main Files

- `2D_Diamond_Catcher.py`
  - Main game file
  - Includes:
    - custom zone-based midpoint line drawing (`mpl`)
    - score tracking
    - speed scaling
    - pause/play/restart/exit buttons
    - optional cheat behavior

> Tip: if you only want to run the game, you do not need to read the rest first.

---

## Quick Start

### 1) Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### 3) Run a file

```bash
python3 "2D_Diamond_Catcher.py"
```

---

## Game Controls

- ⬅️ Left Arrow: move catcher left
- ➡️ Right Arrow: move catcher right
- ⏯️ Click the top-center icon: pause/play
- 🔁 Click the top-left icon: restart
- ❌ Click the top-right icon: exit

Score is printed in the terminal while you play.

---

## How It Works

The game uses a zone-conversion approach for line rasterization:

1. Determine which of the 8 octant-like zones the line belongs to.
2. Convert that line into Zone 0.
3. Run midpoint line logic in Zone 0.
4. Convert plotted points back into the original zone.

That keeps the drawing logic compact while still supporting all line directions.

---

## Notes

- 📦 This repo includes an `OpenGL/` package directory in the workspace, but installing PyOpenGL in your environment is still the safest way to avoid import issues.
- 🍎 If GLUT initialization fails on macOS, ensure your Python environment and OpenGL/GLUT libraries are properly installed.
- 🧪 If the window does not open, try launching from a terminal instead of the editor run button.

---

## Author

Abdullah Al Adib

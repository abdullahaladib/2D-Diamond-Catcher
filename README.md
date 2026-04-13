<h1 align="center">CSE423 Graphics Lab Showcase</h1>

<p align="center">
	A mini collection of PyOpenGL experiments and assignment work.<br>
	Built with GLUT event handling, custom line-drawing logic, and interactive controls.
</p>

---

## What Is Inside

This repository contains multiple OpenGL practice files and assignment implementations for CSE423.

- Interactive 2D scene demos
- Manual midpoint line drawing implementation
- Keyboard and mouse driven controls
- A complete diamond-catching game loop with pause, restart, collision, and scoring

---

## Main Files

- `21201789_Abdullah Al Adib_sec18_Assignment02.py`
  - Main assignment game (catch-the-diamond style)
  - Includes:
    - custom zone-based midpoint line drawing (`mpl`)
    - score tracking
    - speed scaling
    - pause/play/restart/exit buttons
    - optional cheat behavior

- `Hello_openGL.py`
  - Minimal hello-world style OpenGL point rendering example

- `Lets_draw_sth.py`
  - Interactive drawing + animation playground with:
    - axes and shapes
    - moving point
    - mouse placement
    - keyboard-based size/speed updates

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
python3 "21201789_Abdullah Al Adib_sec18_Assignment02.py"
```

You can also run:

```bash
python3 Hello_openGL.py
python3 Lets_draw_sth.py
```

---

## Game Controls (Assignment02)

- Left Arrow: move catcher left
- Right Arrow: move catcher right
- Mouse click on top-center icon: pause/play
- Mouse click on top-left icon: restart
- Mouse click on top-right icon: exit

Score is printed in the terminal.

---

## How It Works (Short Version)

The assignment uses a zone-conversion approach for line rasterization:

1. Determine which of the 8 octant-like zones the line belongs to.
2. Convert that line into Zone 0.
3. Run midpoint line logic in Zone 0.
4. Convert plotted points back into the original zone.

This keeps the drawing logic compact while still supporting all line directions.

---

## Notes

- This repo includes an `OpenGL/` package directory in the workspace, but installing PyOpenGL in your environment is still the safest way to avoid import issues.
- If GLUT initialization fails on macOS, ensure your Python environment and OpenGL/GLUT libraries are properly installed.

---

## Author

Abdullah Al Adib

---

## Status

Actively usable for lab demos and assignment submission reference.

# AVG Player — Terminal ASCII Video Player

> 🌐 [Leer en español](README_ES.md)

A lightweight, zero-dependency Python player that renders pre-compiled `.ascii` animations in TrueColor (24-bit) directly in your terminal.

## Included Demo Asset

This repository includes a pre-compiled `animation.ascii` file featuring **Rem** from the anime **_Re:Zero − Starting Life in Another World_**, ready to run out of the box with no extra setup.

## Features

- **Zero external dependencies:** Uses only the Python 3.10+ standard library (`zlib`, `json`, `argparse`, `shutil`, `time`).

- **24-bit TrueColor ANSI rendering:** Smooth color playback with alternate screen buffer isolation and automatic cursor restoration on exit.

- **Infinite loop by default:** Plays continuously until stopped with `Ctrl+C`, with optional single-pass playback.

- **Flexible path resolution:** Searches for `.ascii` assets in both your current working directory and alongside `play.py`.

## Requirements

- **Python 3.10+**

- A terminal emulator with **TrueColor (24-bit)** support (e.g., GNOME Terminal, Kitty, Alacritty, WezTerm, iTerm2, Windows Terminal).

## Quick Start

1. Clone or download this repository and run the included Rem animation:

   ```bash
   python play.py
   ```

   _(Or specify the asset explicitly: `python play.py animation.ascii`)_

2. Press **`Ctrl+C`** at any time to stop playback and cleanly restore your terminal.

## CLI Options

| Argument / Flag | Default           | Description                                            |
| --------------- | ----------------- | ------------------------------------------------------ |
| `asset`         | `animation.ascii` | Path or filename of the `.ascii` animation file.       |
| `--once`        | `False`           | Play the animation once instead of looping infinitely. |
| `--fps`         | _(asset default)_ | Override the original playback frame rate.             |

### Examples

```bash
# Play the included Rem animation in an infinite loop
python play.py animation.ascii

# Play once and exit
python play.py animation.ascii --once

# Override playback speed to 24 FPS
python play.py animation.ascii --fps 24
```

## Display Tips

- If the terminal window is smaller than the animation's compiled dimensions (`cols × rows`), a brief warning will appear before playback starts.

- Maximize your terminal window or zoom out (`Ctrl + -`) if you notice line wrapping or vertical clipping.

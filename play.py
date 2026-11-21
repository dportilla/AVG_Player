import argparse
import json
from pathlib import Path
import shutil
import sys
import time
import zlib


def resolve_asset(asset_arg: str) -> Path | None:
    """Resolve an asset path from the provided argument or nearby locations."""
    candidate = Path(asset_arg)
    search_paths = [
        candidate,
        Path.cwd() / candidate,
        Path(__file__).resolve().parent / candidate,
    ]
    for path in search_paths:
        if path.exists() and path.is_file():
            return path
    return None


def play_asset(asset_arg: str, loop: bool = True, override_fps: int | None = None) -> None:
    """Load and play an ASCII animation asset in the terminal."""
    asset_path = resolve_asset(asset_arg)
    if asset_path is None:
        print(f"No se encontró el archivo '{asset_arg}' en la carpeta actual ni junto a play.py.")
        return

    data = json.loads(zlib.decompress(asset_path.read_bytes()).decode("utf-8"))

    frames: list[str] = data["frames"]
    fps: int = max(1, override_fps if override_fps and override_fps > 0 else data["fps"])
    cols: int = data["cols"]
    rows: int = data["rows"]

    if not frames:
        print("El archivo no contiene frames.")
        return

    term = shutil.get_terminal_size((80, 24))
    if term.columns < cols or term.lines < rows:
        print(
            f"Aviso: la terminal mide {term.columns}x{term.lines} y la animación es {cols}x{rows}. "
            "Si notas saltos, agranda la pestaña o reduce el zoom."
        )
        time.sleep(1.5)

    sys.stdout.write("\x1b[?1049h\x1b[?25l\x1b[2J")
    sys.stdout.flush()

    try:
        while True:
            start_time = time.perf_counter()
            for i, frame_str in enumerate(frames):
                target_time = start_time + i / fps
                now = time.perf_counter()
                if target_time > now:
                    time.sleep(target_time - now)

                sys.stdout.write("\x1b[H" + frame_str + "\n")
                sys.stdout.flush()

            if not loop:
                break
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\x1b[0m\x1b[?25h\x1b[?1049l")
        sys.stdout.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reproduce un archivo .ascii en la terminal en loop.")
    parser.add_argument("asset", nargs="?", default="animation.ascii", help="Ruta o nombre del archivo .ascii")
    parser.add_argument("--once", action="store_true", help="Reproduce una sola vez en lugar de loop")
    parser.add_argument("--fps", type=int, default=None, help="Sobrescribe los FPS originales")
    args = parser.parse_args()

    play_asset(args.asset, loop=not args.once, override_fps=args.fps)

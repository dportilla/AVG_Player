# AVG Player — Reproductor de Animaciones ASCII en Terminal

> 🌐 [Read in English](README.md)

Reproductor ligero y sin dependencias externas en Python que renderiza animaciones `.ascii` precompiladas en TrueColor (24-bit) directamente en tu terminal.

## Animación incluida de ejemplo

Este repositorio incluye el archivo precompilado `animation.ascii` con una animación de **Rem** del anime ***Re:Zero − Starting Life in Another World***, lista para ejecutarse de inmediato sin configuración adicional.

## Características

* **Cero dependencias externas:** Utiliza únicamente la librería estándar de Python 3.10+ (`zlib`, `json`, `argparse`, `shutil`, `time`).

* **Renderizado ANSI TrueColor (24-bit):** Reproducción fluida a color con aislamiento en pantalla alterna (*alternate screen buffer*) y restauración automática del cursor al salir.

* **Bucle infinito por defecto:** Se reproduce de forma continua hasta detenerlo con `Ctrl+C`, con opción de reproducción de una sola pasada.

* **Resolución flexible de rutas:** Busca archivos `.ascii` tanto en tu directorio actual como junto a `play.py`.

## Requisitos

* **Python 3.10+**

* Un emulador de terminal con soporte **TrueColor (24-bit)** (por ejemplo: GNOME Terminal, Kitty, Alacritty, WezTerm, iTerm2, Windows Terminal).

## Inicio rápido

1. Clona o descarga este repositorio y ejecuta la animación incluida de Rem:

   ```bash
   python play.py
   ```

   *(O indica el archivo explícitamente: `python play.py animation.ascii`)*

2. Presiona **`Ctrl+C`** en cualquier momento para detener la reproducción y restaurar tu terminal limpiamente.

## Opciones CLI

| Argumento / Flag | Por defecto | Descripción | 
| ----- | ----- | ----- | 
| `asset` | `animation.ascii` | Ruta o nombre del archivo de animación `.ascii`. | 
| `--once` | `False` | Reproduce la animación una sola vez en lugar de en bucle infinito. | 
| `--fps` | *(FPS del archivo)* | Sobrescribe la velocidad de fotogramas por segundo original. | 

### Ejemplos

```bash
# Reproducir la animación incluida de Rem en bucle infinito
python play.py animation.ascii

# Reproducir una sola vez y salir
python play.py animation.ascii --once

# Cambiar la velocidad de reproducción a 24 FPS
python play.py animation.ascii --fps 24
```

## Consejos de visualización

* Si la ventana de la terminal es más pequeña que las dimensiones compiladas de la animación (`cols × rows`), aparecerá un breve aviso antes de iniciar la reproducción.

* Maximiza la ventana de tu terminal o reduce el zoom (`Ctrl + -`) si notas saltos de línea o recortes verticales.
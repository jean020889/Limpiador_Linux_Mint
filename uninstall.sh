#!/usr/bin/env bash

set -e

APP_DIR="/home/asus/Apps/limpiador_mint"
VENV_DIR="/home/asus/Apps/limpiador_mint_env"
DESKTOP_FILE="$HOME/Escritorio/limpiador_mint.desktop"
MENU_FILE="$HOME/.local/share/applications/limpiador_mint.desktop"

echo "=== Iniciando desinstalación de Limpiador Mint ==="

# 1. Eliminar acceso directo del Escritorio
if [ -f "$DESKTOP_FILE" ]; then
    echo "-> Eliminando icono del Escritorio..."
    rm -f "$DESKTOP_FILE"
fi

# 2. Eliminar acceso directo del Menú de aplicaciones
if [ -f "$MENU_FILE" ]; then
    echo "-> Eliminando acceso directo del Menú..."
    rm -f "$MENU_FILE"
fi

# 3. Eliminar archivos de la aplicación
if [ -d "$APP_DIR" ]; then
    echo "-> Eliminando carpeta de la aplicación ($APP_DIR)..."
    rm -rf "$APP_DIR"
fi

# 4. Eliminar entorno virtual
if [ -d "$VENV_DIR" ]; then
    echo "-> Eliminando entorno virtual ($VENV_DIR)..."
    rm -rf "$VENV_DIR"
fi

echo "=== Desinstalación completada. Se han eliminado todos los componentes. ==="

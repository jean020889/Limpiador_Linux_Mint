#!/usr/bin/env bash

set -e

# Configuración de rutas
APP_DIR="/home/asus/Apps/limpiador_mint"
VENV_DIR="/home/asus/Apps/limpiador_mint_env"
DESKTOP_FILE="$HOME/Escritorio/limpiador_mint.desktop"
MENU_FILE="$HOME/.local/share/applications/limpiador_mint.desktop"
ICON_SRC="icon_limpiador_mint.jpeg"
ICON_DEST="$APP_DIR/icon_limpiador_mint.png"

echo "=== Iniciando instalación de Limpiador Mint ==="

# 1. Asegurar dependencias del sistema (python3-venv, python3-tk e imagemagick para convertir el icono)
echo "-> Verificando dependencias del sistema..."
sudo apt-get update -qq
sudo apt-get install -y -qq python3-venv python3-tk imagemagick > /dev/null

# 2. Crear carpetas de instalación
echo "-> Creando directorio de la aplicación en $APP_DIR..."
mkdir -p "$APP_DIR"
mkdir -p "$HOME/Escritorio"
mkdir -p "$HOME/.local/share/applications"

# 3. Copiar código fuente e icono
echo "-> Copiando archivos del proyecto..."
cp -r ./* "$APP_DIR/"

# Convertir icono JPEG a PNG para garantizar compatibilidad con Cinnamon/Linux Mint
if [ -f "$APP_DIR/$ICON_SRC" ]; then
    echo "-> Procesando icono del programa..."
    convert "$APP_DIR/$ICON_SRC" "$ICON_DEST"
else
    echo "[Aviso]: No se encontró $ICON_SRC en la raíz. Se usará un icono genérico del sistema."
    ICON_DEST="utilities-terminal"
fi

# 4. Crear Entorno Virtual
echo "-> Creando entorno virtual en $VENV_DIR..."
if [ -d "$VENV_DIR" ]; then
    rm -rf "$VENV_DIR"
fi
python3 -m venv "$VENV_DIR"

# 5. Instalar dependencias pip dentro del venv
echo "-> Instalando paquetes desde requirements.txt..."
"$VENV_DIR/bin/pip" install --upgrade pip -q
if [ -f "$APP_DIR/requirements.txt" ]; then
    "$VENV_DIR/bin/pip" install -r "$APP_DIR/requirements.txt" -q
fi

# 6. Otorgar permisos de ejecución
chmod +x "$APP_DIR/limpiador_mint.py"

# 7. Crear lanzador .desktop para Escritorio y Menú
echo "-> Generando accesos directos..."

CAT_DESKTOP="[Desktop Entry]
Version=1.0
Type=Application
Name=Limpiador Mint
Comment=Herramienta de mantenimiento y limpieza gráfica para Linux Mint
Exec=$VENV_DIR/bin/python $APP_DIR/limpiador_mint.py
Icon=$ICON_DEST
Terminal=false
Categories=System;Settings;
StartupNotify=true"

echo "$CAT_DESKTOP" > "$DESKTOP_FILE"
echo "$CAT_DESKTOP" > "$MENU_FILE"

# Permisos de ejecución para los lanzadores
chmod +x "$DESKTOP_FILE"
chmod +x "$MENU_FILE"

# Confiar en el acceso directo del escritorio en Cinnamon
gio trust "$DESKTOP_FILE" 2>/dev/null || true

echo "=== Instalación completada con éxito ==="
echo "Puedes ejecutar el programa desde el icono en tu Escritorio o en el Menú de Aplicaciones."

Markdown
# Manual de Instalación y Desinstalación - Limpiador Mint

Este documento explica cómo instalar y desinstalar la herramienta gráfica de mantenimiento **Limpiador Mint**.

---

## 🚀 Requisitos Previos

Asegúrate de estar ubicado en la carpeta raíz del proyecto antes de ejecutar los comandos.

---

## 📦 Instalación

1. Abre una terminal en la carpeta donde descargaste o descomprimiste el proyecto.
2. Otorga permisos de ejecución al instalador:

   ```bash
   chmod +x install.sh
Ejecuta el instalador:

Bash
./install.sh
¿Qué hace el instalador automáticamente?
Instala los paquetes del sistema necesarios (python3-venv, python3-tk, imagemagick).

Copia la aplicación a /home/asus/Apps/limpiador_mint.

Crea un entorno virtual Python dedicado en /home/asus/Apps/limpiador_mint_env.

Convierte el icono icon_limpiador_mint.jpeg a formato PNG compatible.

Crea el acceso directo en el Escritorio y en el Menú de Inicio / Sistema.

🗑️ Desinstalación
Abre una terminal en la carpeta del proyecto o ejecuta directamente el desinstalador.

Asigna permisos de ejecución al script de desinstalación:

Bash
chmod +x uninstall.sh
Ejecuta el desinstalador:

Bash
./uninstall.sh
¿Qué elimina el desinstalador?
El acceso directo del Escritorio.

El acceso directo del Menú de Aplicaciones.

La carpeta /home/asus/Apps/limpiador_mint.

El entorno virtual /home/asus/Apps/limpiador_mint_env.

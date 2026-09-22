
#!/usr/bin/env python3
"""
Módulo de Limpieza y Mantenimiento para Linux Mint.
Proporciona una interfaz gráfica Tkinter con ejecución segura vía subprocess/pkexec.
"""

import sys
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
from typing import List, Optional


class LimpiadorLinuxMint:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Mantenimiento y Limpieza - Linux Mint")
        self.root.geometry("640x540")
        self.root.resizable(False, False)

        # Configuración del tema gráfico
        style = ttk.Style()
        style.theme_use("clam")

        # Cabecera principal
        header = ttk.Label(
            root,
            text="Panel de Mantenimiento de Sistema",
            font=("Helvetica", 14, "bold")
        )
        header.pack(pady=10)

        # Marco de botones
        frame_buttons = ttk.LabelFrame(root, text="Acciones de Limpieza")
        frame_buttons.pack(padx=15, pady=5, fill="x")

        # Definición de botones y acciones
        self._crear_boton(
            frame_buttons,
            "1. Limpiar Caché APT y Paquetes Huérfanos",
            self.limpiar_apt
        )
        self._crear_boton(
            frame_buttons,
            "2. Limpiar Runtimes Obsoletos de Flatpak",
            self.limpiar_flatpak
        )
        self._crear_boton(
            frame_buttons,
            "3. Limpiar Caché de Contenedores (Podman / Docker)",
            self.limpiar_contenedores
        )
        self._crear_boton(
            frame_buttons,
            "4. Vaciar Papelera, Caché de Usuario y Logs Viejos",
            self.limpiar_cache_usuario
        )
        self._crear_boton(
            frame_buttons,
            "5. Ver Espacio en Disco Actual (df -h)",
            self.ver_espacio
        )

        # Registro de Logs / Consola
        frame_output = ttk.LabelFrame(root, text="Registro de Ejecución")
        frame_output.pack(padx=15, pady=10, fill="both", expand=True)

        self.txt_output = tk.Text(
            frame_output,
            wrap="word",
            bg="#1e1e1e",
            fg="#00ff00",
            font=("Consolas", 9)
        )
        self.txt_output.pack(fill="both", expand=True, padx=5, pady=5)

    def _crear_boton(self, parent: ttk.LabelFrame, texto: str, comando: callable) -> None:
        btn = ttk.Button(parent, text=texto, command=comando)
        btn.pack(fill="x", padx=10, pady=4)

    def log(self, mensaje: str) -> None:
        self.txt_output.insert(tk.END, mensaje + "\n")
        self.txt_output.see(tk.END)

    def ejecutar_comando(self, comando: str, requiere_sudo: bool = False) -> None:
        try:
            if requiere_sudo:
                comando = f"pkexec {comando}"

            self.log(f"-> Ejecutando: {comando}")
            self.root.update_idletasks()

            proceso = subprocess.Popen(
                comando,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = proceso.communicate()

            if stdout:
                self.log(stdout.strip())
            if stderr:
                self.log(f"[Aviso]: {stderr.strip()}")

            self.log("✓ Operación finalizada.\n")
        except Exception as err:
            self.log(f"[Error de ejecución]: {str(err)}\n")

    def limpiar_apt(self) -> None:
        if messagebox.askyesno("Confirmación", "¿Eliminar caché de APT y paquetes obsoletos?"):
            self.ejecutar_comando("apt-get clean && apt-get autoremove --purge -y", requiere_sudo=True)

    def limpiar_flatpak(self) -> None:
        if messagebox.askyesno("Confirmación", "¿Desinstalar runtimes huérfanos de Flatpak?"):
            self.ejecutar_comando("flatpak uninstall --unused -y")

    def limpiar_contenedores(self) -> None:
        if messagebox.askyesno("Confirmación", "¿Limpiar imágenes/volúmenes huérfanos de Podman y Docker?"):
            self.ejecutar_comando("podman system prune -a --volumes -f 2>/dev/null || true")
            self.ejecutar_comando("docker system prune -a --volumes -f", requiere_sudo=True)

    def limpiar_cache_usuario(self) -> None:
        if messagebox.askyesno("Confirmación", "¿Vaciar Papelera, ~/.cache y truncar registros de sistema a 100M?"):
            self.ejecutar_comando("rm -rf ~/.local/share/Trash/files/*")
            self.ejecutar_comando("rm -rf ~/.cache/*")
            self.ejecutar_comando("journalctl --vacuum-size=100M", requiere_sudo=True)

    def ver_espacio(self) -> None:
        self.ejecutar_comando("df -h /")


def main() -> None:
    root = tk.Tk()
    app = LimpiadorLinuxMint(root)
    root.mainloop()


if __name__ == "__main__":
    main()

"""
Punto de entrada principal de la aplicación.
"""

import flet as ft
from .ui.app import MunicipalityApp


def main():
    """Ejecuta la aplicación de consulta de municipios como web app."""
    print("Iniciando aplicación web en http://localhost:8550")
    
    app = MunicipalityApp()
    ft.app(target=app.main, view=ft.AppView.WEB_BROWSER, port=8550)


if __name__ == "__main__":
    main()

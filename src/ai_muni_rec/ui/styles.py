"""
Estilos y configuración de diseño para la aplicación.
Diseñado para ser accesible con colores claros y texto grande.
"""

import flet as ft

# Colores principales
COLORS = {
    "primary": "#2196F3",  # Azul claro
    "primary_light": "#BBDEFB",  # Azul muy claro
    "secondary": "#4CAF50",  # Verde
    "background": "#FFFFFF",  # Blanco
    "surface": "#F5F5F5",  # Gris muy claro
    "user_message": "#E3F2FD",  # Azul claro para mensajes del usuario
    "assistant_message": "#F1F8E9",  # Verde claro para mensajes del asistente
    "text_primary": "#212121",  # Negro para texto principal
    "text_secondary": "#757575",  # Gris para texto secundario
    "divider": "#BDBDBD",  # Gris para divisores
    "error": "#F44336",  # Rojo para errores
}

# Tamaños de texto
TEXT_SIZES = {
    "title": 28,
    "subtitle": 22,
    "body": 18,
    "button": 16,
    "caption": 14,
}

# Espaciado
SPACING = {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24,
    "xl": 32,
}

# Bordes redondeados
BORDER_RADIUS = {
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24,
}


def get_button_style(color: str = None) -> dict:
    """Retorna el estilo para botones con texto grande y colores claros."""
    return {
        "height": 50,
        "style": ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS["md"]),
            bgcolor=color or COLORS["primary"],
            color=COLORS["background"],
            padding=SPACING["md"],
        ),
    }


def get_text_field_style() -> dict:
    """Retorna el estilo para campos de texto grandes y accesibles."""
    return {
        "border_radius": BORDER_RADIUS["md"],
        "border_color": COLORS["primary"],
        "focused_border_color": COLORS["secondary"],
        "text_size": TEXT_SIZES["body"],
        "color": COLORS["text_primary"],
        "height": 60,
    }


def get_card_style() -> dict:
    """Retorna el estilo para tarjetas/contenedores."""
    return {
        "bgcolor": COLORS["surface"],
        "border_radius": BORDER_RADIUS["lg"],
        "padding": SPACING["lg"],
    }

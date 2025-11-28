"""
Componente de chat con mensajes diferenciados.
"""

import flet as ft
from datetime import datetime
from typing import Callable
from .styles import COLORS, TEXT_SIZES, SPACING, BORDER_RADIUS, get_text_field_style


class ChatMessage(ft.Container):
    """Componente individual de mensaje de chat."""

    def __init__(self, message: str, is_user: bool, timestamp: str = None):
        super().__init__()
        self.message = message
        self.is_user = is_user
        self.timestamp = timestamp or datetime.now().strftime("%H:%M")

        bg_color = (
            COLORS["user_message"] if self.is_user else COLORS["assistant_message"]
        )
        icon = "👤" if self.is_user else "🤖"
        label = "Tú" if self.is_user else "Asistente"

        message_container = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            f"{icon} {label}",
                            size=TEXT_SIZES["caption"],
                            weight=ft.FontWeight.BOLD,
                            color=COLORS["text_secondary"],
                        ),
                        ft.Text(
                            self.timestamp,
                            size=TEXT_SIZES["caption"],
                            color=COLORS["text_secondary"],
                        ),
                    ],
                    spacing=SPACING["xs"],
                ),
                ft.Text(
                    self.message,
                    size=TEXT_SIZES["body"],
                    color=COLORS["text_primary"],
                    selectable=True,
                ),
            ],
            spacing=SPACING["xs"],
            tight=True,
        )

        self.content = message_container
        self.bgcolor = bg_color
        self.border_radius = BORDER_RADIUS["md"]
        self.padding = SPACING["md"]
        self.margin = ft.margin.only(
            left=80 if self.is_user else 0, right=0 if self.is_user else 80
        )


class ChatView(ft.Container):
    """Componente de vista de chat completa."""

    def __init__(self, on_send_message: Callable[[str], str]):
        super().__init__()
        self.on_send_message_callback = on_send_message
        self.messages = []

        self.chat_list = ft.ListView(
            expand=1, spacing=SPACING["md"], padding=SPACING["lg"], auto_scroll=True
        )

        self.input_field = ft.TextField(
            hint_text="Escribe tu consulta aquí...",
            multiline=True,
            min_lines=1,
            max_lines=3,
            shift_enter=True,
            on_submit=self._send_message,
            **get_text_field_style(),
        )

        self.send_button = ft.IconButton(
            icon=ft.Icons.SEND_ROUNDED,
            icon_size=30,
            bgcolor=COLORS["primary"],
            icon_color=COLORS["background"],
            on_click=self._send_message,
        )

        self.content = ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "💬 Chat de Consultas",
                        size=TEXT_SIZES["subtitle"],
                        weight=ft.FontWeight.BOLD,
                        color=COLORS["text_primary"],
                    ),
                    padding=SPACING["md"],
                ),
                ft.Divider(height=1, color=COLORS["divider"]),
                ft.Container(
                    content=self.chat_list,
                    bgcolor=COLORS["surface"],
                    border_radius=BORDER_RADIUS["md"],
                    expand=True,
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(content=self.input_field, expand=1),
                            self.send_button,
                        ],
                        spacing=SPACING["sm"],
                    ),
                    padding=ft.padding.only(top=SPACING["md"]),
                ),
            ],
            spacing=0,
            expand=True,
        )

    def _send_message(self, e):
        message = self.input_field.value.strip()
        if not message:
            return
        self.add_message(message, is_user=True)
        self.input_field.value = ""
        self.update()
        response = self.on_send_message_callback(message)
        self.add_message(response, is_user=False)

    def add_message(self, message: str, is_user: bool):
        chat_message = ChatMessage(message, is_user)
        self.messages.append(chat_message)
        self.chat_list.controls.append(chat_message)
        self.update()

    def add_welcome_message(self):
        welcome_text = (
            "¡Bienvenido al Sistema de Consulta de Municipios de Oaxaca! 🌄\n\n"
            "Puedes hacer preguntas sobre el municipio seleccionado o usar las consultas rápidas del menú lateral.\n\n"
            "Haz clic en una pregunta predefinida para agregarla al campo de texto, o escribe tu propia consulta.\n\n"
            "¿En qué puedo ayudarte?"
        )

        self.add_message(welcome_text, is_user=False)

    def clear_chat(self):
        self.messages.clear()
        self.chat_list.controls.clear()
        self.update()

    def set_input_text(self, text: str):
        """Establece el texto en el campo de entrada."""
        self.input_field.value = text
        self.input_field.focus()
        self.update()

"""
Componente de consultas rápidas con lista de preguntas predefinidas.
"""

import flet as ft
from typing import Callable
from .styles import COLORS, TEXT_SIZES, SPACING, BORDER_RADIUS


class QuickQueryButtons(ft.Container):
    """Componente con lista de preguntas predefinidas."""

    # Lista de preguntas predefinidas
    QUESTIONS = [
        "¿Cuál es el estado del municipio?",
        "¿Cuál es el estado de educación del municipio?",
        "¿Qué prioridad tiene marginación del municipio?",
        "¿Cuáles aspectos del municipio tienen nivel alto?",
        "¿Qué aspectos del municipio requieren prioridad alta?",
        "¿Cuál es el estado de servicios básicos del municipio?",
        "¿Qué prioridad tiene conectividad del municipio?",
        "¿Cuáles aspectos del municipio tienen nivel muy alto?"
    ]

    def __init__(self, on_question_click: Callable[[str], None]):
        super().__init__()
        self.on_question_click = on_question_click
        
        # Crear lista de preguntas
        question_items = []
        for question in self.QUESTIONS:
            question_items.append(self._create_question_item(question))
        
        self.content = ft.Column(
            [
                ft.Text(
                    "Consultas Rápidas",
                    size=TEXT_SIZES["subtitle"],
                    weight=ft.FontWeight.BOLD,
                    color=COLORS["text_primary"]
                ),
                ft.Text(
                    "Haz clic en una pregunta para agregarla al campo de texto",
                    size=TEXT_SIZES["caption"],
                    color=COLORS["text_secondary"]
                ),
                ft.Container(height=SPACING["sm"]),
                ft.Column(
                    question_items,
                    spacing=SPACING["xs"],
                    scroll=ft.ScrollMode.AUTO,
                ),
            ],
            spacing=SPACING["sm"],
        )
        self.padding = SPACING["lg"]
        self.bgcolor = COLORS["background"]
        self.border_radius = BORDER_RADIUS["lg"]

    def _create_question_item(self, question: str) -> ft.Container:
        """Crea un item de pregunta clickeable."""
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(
                        ft.Icons.CHAT_BUBBLE_OUTLINE_ROUNDED,
                        size=20,
                        color=COLORS["primary"]
                    ),
                    ft.Text(
                        question,
                        size=TEXT_SIZES["body"],
                        color=COLORS["text_primary"],
                        expand=1,
                    ),
                ],
                spacing=SPACING["sm"],
            ),
            bgcolor=COLORS["surface"],
            border_radius=BORDER_RADIUS["sm"],
            padding=SPACING["md"],
            ink=True,
            on_click=lambda e, q=question: self.on_question_click(q),
            border=ft.border.all(1, COLORS["divider"]),
        )

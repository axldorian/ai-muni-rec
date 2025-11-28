"""
Aplicación principal de consulta de municipios de Oaxaca.
"""

import flet as ft
from ..core.data_loader import MunicipalityDataLoader
from ..core.query_processor import QueryProcessor
from ..ui.municipality_selector import MunicipalitySelector
from ..ui.chat_view import ChatView
from ..ui.quick_query_buttons import QuickQueryButtons
from ..ui.styles import COLORS, TEXT_SIZES, SPACING, BORDER_RADIUS


class MunicipalityApp:
    """Aplicación principal para consultar información de municipios."""

    def __init__(self):
        """Inicializa la aplicación."""
        self.data_loader = MunicipalityDataLoader()
        self.query_processor = QueryProcessor()
        self.current_municipality = None

    def main(self, page: ft.Page):
        """
        Función principal de la aplicación.
        
        Params
        ------
        page : ft.Page
            Página de Flet
        """
        # Configuración de la página
        page.title = "Consulta de Municipios - Oaxaca"
        page.bgcolor = COLORS["surface"]
        page.padding = SPACING["lg"]
        page.scroll = ft.ScrollMode.HIDDEN
        
        # Configurar tamaño de ventana
        page.window_width = 1400
        page.window_height = 900
        page.window_min_width = 1000
        page.window_min_height = 700

        # Componentes principales
        self.selector = MunicipalitySelector(
            municipalities=self.data_loader.get_all_municipality_names(),
            on_select=self._on_municipality_selected,
        )
        
        self.chat_view = ChatView(
            on_send_message=self._process_user_message,
        )
        
        self.quick_buttons = QuickQueryButtons(
            on_question_click=self._on_question_selected,
        )
        
        # Barra de título
        title_bar = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.LOCATION_CITY_ROUNDED,
                                size=40,
                                color=COLORS["primary"],
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "Sistema de Consulta de Municipios",
                                        size=TEXT_SIZES["title"],
                                        weight=ft.FontWeight.BOLD,
                                        color=COLORS["text_primary"],
                                    ),
                                    ft.Text(
                                        "Oaxaca, México 🇲🇽",
                                        size=TEXT_SIZES["caption"],
                                        color=COLORS["text_secondary"],
                                    ),
                                ],
                                spacing=0,
                            ),
                        ],
                        spacing=SPACING["md"],
                    ),
                ],
            ),
            bgcolor=COLORS["background"],
            padding=SPACING["lg"],
            border_radius=BORDER_RADIUS["lg"],
        )
        
        # Layout en dos columnas
        # Columna izquierda: Sidebar con Selector y Botones
        left_sidebar = ft.Container(
            content=ft.Column(
                [
                    self.selector,
                    ft.Container(height=SPACING["md"]),
                    self.quick_buttons,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            width=400,
            height=700,
        )
        
        # Columna derecha: Solo Chat
        right_column = ft.Container(
            content=self.chat_view,
            bgcolor=COLORS["background"],
            border_radius=BORDER_RADIUS["lg"],
            padding=SPACING["md"],
            expand=1,
            height=700,
        )
        
        # Layout principal con altura fija
        main_content = ft.Container(
            content=ft.Row(
                [
                    left_sidebar,
                    right_column,
                ],
                spacing=SPACING["lg"],
                expand=True,
            ),
            expand=True,
        )
        
        # Agregar todo a la página
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        title_bar,
                        ft.Container(height=SPACING["md"]),
                        main_content,
                    ],
                    spacing=0,
                ),
                expand=True,
            )
        )
        
        # Mensaje de bienvenida
        self.chat_view.add_welcome_message()

    def _on_municipality_selected(self, municipality: str):
        """
        Maneja la selección de un municipio.
        
        Params
        ------
        municipality : str
            Nombre del municipio seleccionado
        """
        self.current_municipality = municipality
        
        # Obtener el nombre normalizado del municipio
        municipality_norm = self.data_loader.get_municipality_normalized_name(municipality)
        
        if not municipality_norm:
            error_msg = f"⚠️ No se encontró el nombre normalizado para {municipality}"
            self.chat_view.add_message(error_msg, is_user=False)
            return
        
        # Establecer el municipio en el procesador con ambos nombres
        self.query_processor.set_municipality(municipality, municipality_norm)
        
        # Limpiar el chat al seleccionar un nuevo municipio
        self.chat_view.clear_chat()
        
        # Obtener resumen del municipio
        summary = self.data_loader.get_municipality_summary(municipality)
        
        # Agregar mensaje al chat
        self.chat_view.add_message(
            summary,
            is_user=False,
        )

    def _process_user_message(self, message: str) -> str:
        """
        Procesa un mensaje del usuario.
        
        Params
        ------
        message : str
            Mensaje del usuario
            
        Returns
        -------
        str
            Respuesta del sistema
        """
        if not self.current_municipality:
            return "⚠️ Por favor, primero selecciona un municipio de la lista."
        
        # Procesar con el query processor (placeholder)
        response = self.query_processor.process_query(message)
        return response

    def _on_question_selected(self, question: str):
        """
        Maneja la selección de una pregunta predefinida.
        Inserta la pregunta en el campo de texto del chat.
        
        Params
        ------
        question : str
            Texto de la pregunta seleccionada
        """
        self.chat_view.set_input_text(question)

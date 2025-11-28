"""
Componente de selector de municipios con búsqueda.
"""

import flet as ft
from typing import Callable, List
from .styles import COLORS, TEXT_SIZES, SPACING, BORDER_RADIUS, get_text_field_style


class MunicipalitySelector(ft.Container):
    """Control personalizado para seleccionar un municipio."""

    def __init__(self, municipalities: List[str], on_select: Callable[[str], None]):
        super().__init__()
        self.all_municipalities = sorted(municipalities)
        self.filtered_municipalities = self.all_municipalities.copy()
        self.on_select_callback = on_select
        self.selected_municipality = None
        self._is_initialized = False
        
        self.search_field = ft.TextField(
            label="🔍 Buscar municipio",
            hint_text="Escribe el nombre del municipio...",
            on_change=self._on_search_change,
            autofocus=False,
            **get_text_field_style(),
        )

        self.municipality_list = ft.ListView(
            spacing=SPACING["sm"],
            padding=SPACING["md"],
            height=300,
        )

        self.selected_text = ft.Text(
            "Ningún municipio seleccionado",
            size=TEXT_SIZES["body"],
            color=COLORS["text_secondary"],
            italic=True,
        )
        
        self._update_municipality_list()
        
        self.content = ft.Column(
            [
                ft.Text("Selecciona un municipio", size=TEXT_SIZES["subtitle"], weight=ft.FontWeight.BOLD, color=COLORS["text_primary"]),
                ft.Divider(height=1, color=COLORS["divider"]),
                ft.Container(height=SPACING["sm"]),
                self.search_field,
                ft.Container(height=SPACING["sm"]),
                self.selected_text,
                ft.Container(height=SPACING["sm"]),
                ft.Container(content=self.municipality_list, bgcolor=COLORS["surface"], border_radius=BORDER_RADIUS["md"], padding=SPACING["xs"]),
            ],
            spacing=0,
        )
        self.bgcolor = COLORS["background"]
        self.padding = SPACING["lg"]
        self.border_radius = BORDER_RADIUS["lg"]
        self._is_initialized = True

    def _on_search_change(self, e):
        query = self.search_field.value.lower()
        if not query:
            self.filtered_municipalities = self.all_municipalities.copy()
        else:
            self.filtered_municipalities = [m for m in self.all_municipalities if query in m.lower()]
        self._update_municipality_list()

    def _update_municipality_list(self):
        self.municipality_list.controls.clear()
        if not self.filtered_municipalities:
            self.municipality_list.controls.append(
                ft.Text("No se encontraron municipios", size=TEXT_SIZES["body"], color=COLORS["text_secondary"], italic=True)
            )
        else:
            for municipality in self.filtered_municipalities[:50]:
                is_selected = municipality == self.selected_municipality
                self.municipality_list.controls.append(
                    ft.Container(
                        content=ft.Text(municipality, size=TEXT_SIZES["body"], color=COLORS["background"] if is_selected else COLORS["text_primary"], weight=ft.FontWeight.BOLD if is_selected else ft.FontWeight.NORMAL),
                        bgcolor=COLORS["primary"] if is_selected else COLORS["background"],
                        padding=SPACING["md"],
                        border_radius=BORDER_RADIUS["sm"],
                        on_click=lambda e, m=municipality: self._on_municipality_click(m),
                        ink=True,
                    )
                )
        if self._is_initialized:
            self.update()

    def _on_municipality_click(self, municipality: str):
        self.selected_municipality = municipality
        self.selected_text.value = f"✅ Seleccionado: {municipality}"
        self.selected_text.color = COLORS["secondary"]
        self.selected_text.italic = False
        self._update_municipality_list()
        if self.on_select_callback:
            self.on_select_callback(municipality)

    def get_selected_municipality(self) -> str:
        return self.selected_municipality

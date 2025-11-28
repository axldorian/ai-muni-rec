"""
Módulo para cargar y gestionar datos de municipios.
"""

import csv
from pathlib import Path
from typing import List, Dict, Optional


class MunicipalityDataLoader:
    """Clase para cargar y acceder a los datos de municipios."""

    def __init__(self, data_path: str = None, indicators_path: str = None):
        """
        Inicializa el cargador de datos.

        Params
        ------
        data_path : str, optional
            Ruta al archivo CSV con datos municipales
        indicators_path : str, optional
            Ruta al archivo CSV con indicadores (incluye municipio_norm y cve_mun)
        """
        if data_path is None:
            # Ruta por defecto
            base_path = Path(__file__).parent.parent.parent.parent
            data_path = base_path / "data" / "processed" / "dataset_municipal_v2.csv"

        if indicators_path is None:
            base_path = Path(__file__).parent.parent.parent.parent
            indicators_path = base_path / "data" / "processed" / "indicators_municipal_v2.csv"

        self.data_path = Path(data_path)
        self.indicators_path = Path(indicators_path)
        self.municipalities: List[Dict] = []
        self.municipality_names: List[str] = []
        self.municipality_mapping: Dict[str, Dict[str, str]] = {}  # nombre_completo -> {cve_mun, municipio_norm}
        self._load_data()
        self._load_indicators_mapping()

    def _load_data(self):
        """Carga los datos desde el archivo CSV."""
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.municipalities.append(row)
                    self.municipality_names.append(row["municipio"])
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            # Datos de ejemplo si falla la carga
            self.municipalities = []
            self.municipality_names = []

    def _load_indicators_mapping(self):
        """Carga el mapeo de municipios desde el archivo de indicadores."""
        try:
            with open(self.indicators_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    nombre_completo = row["municipio"]
                    self.municipality_mapping[nombre_completo] = {
                        "cve_mun": row["cve_mun"],
                        "municipio_norm": row["municipio_norm"],
                        "municipio": nombre_completo
                    }
        except Exception as e:
            print(f"Error al cargar mapeo de indicadores: {e}")
            self.municipality_mapping = {}

    def get_all_municipality_names(self) -> List[str]:
        """Retorna lista de todos los nombres de municipios."""
        return self.municipality_names.copy()

    def search_municipalities(self, query: str) -> List[str]:
        """
        Busca municipios que coincidan con la query.

        Params
        ------
        query : str
            Texto de búsqueda

        Returns
        -------
        List[str]
            Lista de nombres de municipios que coinciden
        """
        if not query:
            return self.municipality_names

        query_lower = query.lower()
        return [name for name in self.municipality_names if query_lower in name.lower()]

    def get_municipality_data(self, municipality_name: str) -> Optional[Dict]:
        """
        Obtiene todos los datos de un municipio específico.

        Params
        ------
        municipality_name : str
            Nombre del municipio

        Returns
        -------
        Optional[Dict]
            Diccionario con datos del municipio o None si no existe
        """
        for muni in self.municipalities:
            if muni["municipio"].lower() == municipality_name.lower():
                return muni
        return None

    def get_municipality_normalized_name(self, municipality_name: str) -> Optional[str]:
        """
        Obtiene el nombre normalizado de un municipio.

        Params
        ------
        municipality_name : str
            Nombre completo del municipio

        Returns
        -------
        Optional[str]
            Nombre normalizado del municipio o None si no existe
        """
        mapping = self.municipality_mapping.get(municipality_name)
        return mapping["municipio_norm"] if mapping else None

    def get_municipality_code(self, municipality_name: str) -> Optional[str]:
        """
        Obtiene el código del municipio.

        Params
        ------
        municipality_name : str
            Nombre completo del municipio

        Returns
        -------
        Optional[str]
            Código del municipio (cve_mun) o None si no existe
        """
        mapping = self.municipality_mapping.get(municipality_name)
        return mapping["cve_mun"] if mapping else None

    def get_municipality_info(self, municipality_name: str) -> Optional[Dict[str, str]]:
        """
        Obtiene toda la información de mapeo de un municipio.

        Params
        ------
        municipality_name : str
            Nombre completo del municipio

        Returns
        -------
        Optional[Dict[str, str]]
            Diccionario con cve_mun, municipio_norm y municipio, o None si no existe
        """
        return self.municipality_mapping.get(municipality_name)

    def get_municipality_summary(self, municipality_name: str) -> str:
        """
        Genera un resumen básico del municipio.

        Params
        ------
        municipality_name : str
            Nombre del municipio

        Returns
        -------
        str
            Texto con resumen del municipio
        """
        data = self.get_municipality_data(municipality_name)
        if not data:
            return f"No se encontró información para {municipality_name}"

        try:
            # Convertir valores a números para formateo
            def format_number(value):
                """
                Formatea un valor numérico con separador de miles.
                
                Params
                ------
                value : any
                    Valor a formatear
                    
                Returns
                -------
                str
                    Valor formateado con separador de miles
                """
                try:
                    # Intentar convertir a float primero (por si hay decimales)
                    num = float(value)
                    # Si es un número entero, mostrarlo sin decimales
                    if num.is_integer():
                        return f"{int(num):,}"
                    return f"{num:,.2f}"
                except (ValueError, TypeError):
                    return str(value)

            summary = (
                f"Seleccionaste: 📍 {data['municipio']}\n\n"
                f"👥 Población total: {format_number(data.get('pob_total', 'N/A'))} habitantes\n"
                f"👥 Población indígena: {format_number(data.get('pob_indigena', 'N/A'))} habitantes\n"
                f"🏘️ Viviendas: {format_number(data.get('viv', 'N/A'))}\n\n"
                "¿Qué deseas saber?"
            )

            return summary
        except KeyError as e:
            return f"Error al generar resumen: falta el campo {e}"

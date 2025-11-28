"""
Módulo para procesar consultas con Prolog usando PySwip.
"""

from typing import Optional, Dict, Any
from pathlib import Path
from pyswip import Prolog


class QueryProcessor:
    """
    Clase para procesar consultas en lenguaje natural mediante Prolog.
    """

    def __init__(self):
        """Inicializa el procesador de consultas."""
        self.current_municipality: Optional[str] = None
        self.current_municipality_norm: Optional[str] = None
        self.prolog = Prolog()
        self._initialize_prolog()

    def _initialize_prolog(self):
        """Inicializa el motor Prolog cargando el archivo de procesamiento de lenguaje."""
        try:
            # Obtener ruta al archivo Prolog
            base_path = Path(__file__).parent.parent.parent.parent
            prolog_file = base_path / "knowledge" / "Procesamiento_lenguaje.pl"
            
            if not prolog_file.exists():
                raise FileNotFoundError(f"No se encontró el archivo Prolog: {prolog_file}")
            
            # Cargar el archivo Prolog
            self.prolog.consult(str(prolog_file))
            print(f"✅ Prolog inicializado correctamente desde: {prolog_file}")
            
        except Exception as e:
            print(f"❌ Error al inicializar Prolog: {e}")
            raise

    def set_municipality(self, municipality_name: str, municipality_norm: str = None):
        """
        Establece el municipio actual para las consultas.

        Params
        ------
        municipality_name : str
            Nombre completo del municipio
        municipality_norm : str, optional
            Nombre normalizado del municipio (sin acentos, minúsculas)
        """
        self.current_municipality = municipality_name
        self.current_municipality_norm = municipality_norm or municipality_name.lower()

    def process_query(self, query: str) -> str:
        """
        Procesa una consulta en lenguaje natural usando Prolog y retorna una respuesta.

        Params
        ------
        query : str
            Consulta en lenguaje natural

        Returns
        -------
        str
            Respuesta generada por Prolog
        """
        if not self.current_municipality or not self.current_municipality_norm:
            return "⚠️ Por favor, primero selecciona un municipio."

        try:
            # Reemplazar el nombre del municipio en la consulta por el normalizado
            # para que Prolog lo entienda
            query_normalized = self._normalize_query(query)
            
            # Llamar a Prolog
            result = self._query_prolog(query_normalized)
            
            # Formatear la respuesta
            formatted_response = self._format_response(result)
            
            return formatted_response
            
        except Exception as e:
            error_msg = f"❌ Error al procesar la consulta: {str(e)}"
            print(error_msg)
            return error_msg

    def _normalize_query(self, query: str) -> str:
        """
        Normaliza la consulta reemplazando el nombre del municipio por su versión normalizada
        y normalizando niveles y aspectos a formato sin espacios ni acentos.
        
        Params
        ------
        query : str
            Consulta original
            
        Returns
        -------
        str
            Consulta con el nombre normalizado del municipio
        """
        # Reemplazar el nombre completo por el normalizado en la consulta
        query_normalized = query.lower()
        
        # Normalizar nombres de aspectos (quitar espacios, acentos y unir palabras)
        aspectos_map = {
            "marginación": "marginacion",
            "marginacion": "marginacion",
            "rezago social": "rezagosocial",
            "conectividad": "conectividad",
            "servicios básicos": "serviciosbasicos",
            "servicios basicos": "serviciosbasicos",
            "elementos de salud": "elementosdesalud",
            "seguridad social": "seguridadsocial",
            "educación": "educacion",
            "educacion": "educacion",
            "desigualdad": "desigualdad",
            "dependencia económica": "dependenciaeconomica",
            "dependencia economica": "dependenciaeconomica",
            "calidad de vivienda": "calidaddevivienda",
            "seguridad alimentaria": "seguridadalimentaria"
        }
        
        for aspecto_con_formato, aspecto_normalizado in aspectos_map.items():
            query_normalized = query_normalized.replace(aspecto_con_formato, aspecto_normalizado)
        
        # Normalizar niveles de carencia (quitar espacios entre palabras)
        niveles_map = {
            "muy alto": "muyalto",
            "muy bajo": "muybajo",
            "muy alta": "muyalta",
            "muy baja": "muybaja"
        }
        
        for nivel_con_espacio, nivel_sin_espacio in niveles_map.items():
            query_normalized = query_normalized.replace(nivel_con_espacio, nivel_sin_espacio)
        
        # Reemplazar "del municipio" o "el municipio" por el nombre normalizado
        if "del municipio" in query_normalized:
            query_normalized = query_normalized.replace("del municipio", self.current_municipality_norm)
        elif "el municipio" in query_normalized:
            query_normalized = query_normalized.replace("el municipio", self.current_municipality_norm)
        # Si contiene el nombre completo, reemplazarlo
        elif self.current_municipality.lower() in query_normalized:
            query_normalized = query_normalized.replace(
                self.current_municipality.lower(),
                self.current_municipality_norm
            )
        # Si no contiene el nombre, agregar el municipio donde corresponda
        else:
            # Para preguntas que empiezan con "cuales" o "que aspectos"
            if query_normalized.startswith("cuales") or "aspectos" in query_normalized:
                # Buscar "aspectos" y agregar el municipio después
                query_normalized = query_normalized.replace(
                    "aspectos",
                    f"aspectos {self.current_municipality_norm}",
                    1  # Solo reemplazar la primera ocurrencia
                )
            else:
                # Para otras preguntas, agregar al final
                query_normalized = f"{query_normalized} {self.current_municipality_norm}"
        
        return query_normalized

    def _query_prolog(self, query: str) -> Any:
        """
        Ejecuta la consulta en Prolog.
        
        Params
        ------
        query : str
            Consulta normalizada
            
        Returns
        -------
        Any
            Resultado de Prolog
        """
        try:
            # Construir la consulta de Prolog
            prolog_query = f"procesar_consulta('{query}', Resultado)"
            
            # Ejecutar la consulta
            results = list(self.prolog.query(prolog_query))
            
            if results:
                return results[0].get("Resultado", "No se obtuvo respuesta.")
            else:
                return "No se encontró resultado para la consulta."
                
        except Exception as e:
            raise Exception(f"Error en la consulta Prolog: {str(e)}")

    def _format_response(self, result: Any) -> str:
        """
        Formatea la respuesta de Prolog para mostrarla en el chat.
        
        Params
        ------
        result : Any
            Resultado de Prolog
            
        Returns
        -------
        str
            Respuesta formateada
        """
        if isinstance(result, str):
            # Reemplazar el nombre normalizado por el nombre completo en la respuesta
            result = self._replace_normalized_name(result)
            
            # Verificar si es una respuesta estructurada con pipes
            if '|' in result and ':' in result:
                return self._format_pipe_response(result)
            return result
        elif isinstance(result, dict):
            return self._format_dict_response(result)
        elif isinstance(result, list):
            return self._format_list_response(result)
        else:
            return str(result)

    def _format_dict_response(self, data: Dict) -> str:
        """
        Formatea una respuesta en formato diccionario.
        
        Params
        ------
        data : Dict
            Datos del municipio
            
        Returns
        -------
        str
            Respuesta formateada
        """
        lines = [f"📊 Información de {self.current_municipality}\n"]
        for key, value in data.items():
            # Formatear las claves para que sean más legibles
            key_formatted = key.replace("_", " ").capitalize()
            lines.append(f"• {key_formatted}: {value}")
        return "\n".join(lines)

    def _format_list_response(self, data: list) -> str:
        """
        Formatea una respuesta en formato lista.
        
        Params
        ------
        data : list
            Lista de items
            
        Returns
        -------
        str
            Respuesta formateada
        """
        if not data:
            return "No se encontraron resultados."

        lines = [f"📋 Resultados para {self.current_municipality}\n"]
        for item in data:
            if isinstance(item, dict):
                lines.append(self._format_dict_response(item))
            else:
                lines.append(f"• {item}")
        return "\n".join(lines)

    def _replace_normalized_name(self, text: str) -> str:
        """
        Reemplaza el nombre normalizado del municipio por el nombre completo en el texto.
        
        Params
        ------
        text : str
            Texto con posible nombre normalizado
            
        Returns
        -------
        str
            Texto con nombre completo
        """
        if self.current_municipality_norm and self.current_municipality:
            # Reemplazar todas las ocurrencias del nombre normalizado
            text = text.replace(self.current_municipality_norm, self.current_municipality)
        return text

    def _format_pipe_response(self, data: str) -> str:
        """
        Formatea respuestas en formato pipe-separated de Prolog.
        Formato esperado: "municipio|Aspecto1:Nivel1|Aspecto2:Nivel2|..."
        
        Params
        ------
        data : str
            String con formato pipe-separated
            
        Returns
        -------
        str
            Respuesta formateada con emojis y estructura clara
        """
        parts = data.split('|')
        if len(parts) < 2:
            return data
        
        municipio = parts[0]
        
        # Mapeo de niveles a emojis
        nivel_emoji = {
            'Muy alto': '🔴',
            'Alto': '🟠',
            'Medio': '🟡',
            'Bajo': '🟢',
            'Muy bajo': '🔵'
        }
        
        lines = [
            f"📊 Estado de: {self.current_municipality}",
            f"",
            "Indicadores:",
            ""
        ]
        
        # Procesar cada aspecto
        for pair in parts[1:]:
            if ':' in pair:
                aspecto, nivel = pair.split(':', 1)
                emoji = nivel_emoji.get(nivel, '⚪')
                lines.append(f"{emoji} {aspecto}: {nivel}")
        
        return "\n".join(lines)

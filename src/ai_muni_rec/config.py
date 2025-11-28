"""
Configuración de la aplicación web.
"""

import os

# Configuración del servidor
SERVER_CONFIG = {
    "port": int(os.getenv("FLET_PORT", "8080")),
    "host": os.getenv("FLET_HOST", "localhost"),
    "view": os.getenv("FLET_VIEW", "WEB_BROWSER"),  # WEB_BROWSER o FLET_APP
}

# Configuración de la aplicación
APP_CONFIG = {
    "title": "Sistema de Consulta de Municipios - Oaxaca",
    "window_width": 1200,
    "window_height": 800,
    "window_min_width": 800,
    "window_min_height": 600,
}

# Rutas de datos
DATA_PATHS = {
    "municipal_dataset": "data/processed/dataset_municipal_v2.csv",
    "municipalities_list": "data/processed/municipios.txt",
}

# Configuración de Prolog (para futura integración)
PROLOG_CONFIG = {
    "facts_file": "knowledge/facts.pl",
    "rules_file": "knowledge/rules.pl",
    "queries_file": "knowledge/queries.pl",
    "utils_file": "knowledge/utils.pl",
}

def get_server_url():
    """Retorna la URL del servidor."""
    host = SERVER_CONFIG["host"]
    port = SERVER_CONFIG["port"]
    return f"http://{host}:{port}"

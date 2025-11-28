#!/usr/bin/env python3
"""
Script rápido para probar consultas específicas.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai_muni_rec.core.data_loader import MunicipalityDataLoader
from ai_muni_rec.core.query_processor import QueryProcessor


def test_queries():
    """Prueba consultas específicas."""
    
    print("Inicializando...")
    data_loader = MunicipalityDataLoader()
    query_processor = QueryProcessor()
    
    # Seleccionar municipio de prueba
    municipio = "Abejones"
    info = data_loader.get_municipality_info(municipio)
    
    if not info:
        print(f"❌ No se encontró {municipio}")
        return
    
    print(f"\n✅ Municipio: {info['municipio']}")
    print(f"   Normalizado: {info['municipio_norm']}")
    print(f"   Código: {info['cve_mun']}\n")
    
    # Configurar procesador
    query_processor.set_municipality(info['municipio'], info['municipio_norm'])
    
    # Lista de consultas a probar
    consultas = [
        "¿Cuál es el estado del municipio?",
        "¿Cuál es el estado de educacion del municipio?",
        "¿Qué prioridad tiene marginacion del municipio?",
        "¿Cuáles aspectos del municipio tienen nivel alto?",
        "¿Qué aspectos del municipio requieren prioridad alta?",
        "¿Cuáles aspectos del municipio tienen nivel muy alto?",
    ]
    
    for i, consulta in enumerate(consultas, 1):
        print(f"\n{'='*60}")
        print(f"Consulta {i}: {consulta}")
        print('='*60)
        
        try:
            # Mostrar consulta normalizada
            query_norm = query_processor._normalize_query(consulta)
            print(f"Normalizada: {query_norm}\n")
            
            # Procesar consulta
            respuesta = query_processor.process_query(consulta)
            print(f"Respuesta:\n{respuesta}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    test_queries()

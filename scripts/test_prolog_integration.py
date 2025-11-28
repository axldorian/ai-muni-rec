#!/usr/bin/env python3
"""
Script de prueba para la integración Prolog-Python.
Prueba el QueryProcessor sin necesidad de la interfaz gráfica.
"""

from pathlib import Path
import sys

# Agregar el directorio src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai_muni_rec.core.data_loader import MunicipalityDataLoader
from ai_muni_rec.core.query_processor import QueryProcessor


def test_integration():
    """Prueba la integración completa."""
    
    print("=" * 60)
    print("PRUEBA DE INTEGRACIÓN PROLOG-PYTHON")
    print("=" * 60)
    print()
    
    # 1. Inicializar componentes
    print("1️⃣  Inicializando componentes...")
    try:
        data_loader = MunicipalityDataLoader()
        query_processor = QueryProcessor()
        print("   ✅ Componentes inicializados correctamente\n")
    except Exception as e:
        print(f"   ❌ Error al inicializar: {e}\n")
        return
    
    # 2. Seleccionar un municipio de prueba
    municipio_prueba = "Abejones"
    print(f"2️⃣  Seleccionando municipio: {municipio_prueba}")
    
    # Obtener información del municipio
    muni_info = data_loader.get_municipality_info(municipio_prueba)
    if not muni_info:
        print(f"   ❌ No se encontró el municipio {municipio_prueba}\n")
        return
    
    print(f"   📍 Municipio: {muni_info['municipio']}")
    print(f"   🔤 Normalizado: {muni_info['municipio_norm']}")
    print(f"   🔢 Código: {muni_info['cve_mun']}\n")
    
    # Establecer municipio en el procesador
    query_processor.set_municipality(
        muni_info['municipio'],
        muni_info['municipio_norm']
    )
    
    # 3. Probar diferentes tipos de consultas
    print("3️⃣  Probando consultas...\n")
    
    consultas = [
        "¿Cuál es el estado del municipio?",
        "¿Cuál es el estado de educación?",
        "¿Qué prioridad tiene marginación?",
        "¿Cuáles aspectos tienen nivel alto?",
    ]
    
    for i, consulta in enumerate(consultas, 1):
        print(f"   Consulta {i}: {consulta}")
        print("   " + "-" * 55)
        try:
            respuesta = query_processor.process_query(consulta)
            print(f"   Respuesta:\n   {respuesta}\n")
        except Exception as e:
            print(f"   ❌ Error: {e}\n")
        print()
    
    # 4. Mostrar estadísticas
    print("4️⃣  Estadísticas:")
    print(f"   • Total de municipios: {len(data_loader.get_all_municipality_names())}")
    print(f"   • Municipios con mapeo: {len(data_loader.municipality_mapping)}")
    print()
    
    print("=" * 60)
    print("PRUEBA COMPLETADA")
    print("=" * 60)


def test_municipality_mapping():
    """Prueba solo el mapeo de municipios."""
    
    print("=" * 60)
    print("PRUEBA DE MAPEO DE MUNICIPIOS")
    print("=" * 60)
    print()
    
    data_loader = MunicipalityDataLoader()
    
    # Probar algunos municipios
    test_municipalities = [
        "Abejones",
        "Oaxaca de Juárez",
        "Santa María del Tule",
        "San Pablo Villa de Mitla"
    ]
    
    for muni in test_municipalities:
        info = data_loader.get_municipality_info(muni)
        if info:
            print(f"✅ {muni}")
            print(f"   Normalizado: {info['municipio_norm']}")
            print(f"   Código: {info['cve_mun']}")
        else:
            print(f"❌ {muni} - No encontrado")
        print()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Prueba la integración Prolog-Python"
    )
    parser.add_argument(
        "--mapping-only",
        action="store_true",
        help="Probar solo el mapeo de municipios (sin Prolog)"
    )
    
    args = parser.parse_args()
    
    if args.mapping_only:
        test_municipality_mapping()
    else:
        test_integration()

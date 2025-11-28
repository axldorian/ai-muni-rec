# Sistema de Consulta de Municipios de Oaxaca 🌄

## Descripción

Aplicación web interactiva para consultar información detallada sobre los 570 municipios de Oaxaca. 

Desarrollada con **Flet** para la interfaz y **Prolog** para el procesamiento de lenguaje natural (PLN), ofreciendo una experiencia moderna e inteligente para explorar indicadores municipales.

## ✨ Características

- 🌐 **Aplicación Web**: Funciona en tu navegador
- 💬 **Chat Interactivo**: Interfaz conversacional intuitiva
- 🧠 **PLN con Prolog**: Procesamiento de lenguaje natural inteligente
- 📊 **570 Municipios**: Base de datos completa de Oaxaca
- 🔍 **Consultas Inteligentes**: Entiende preguntas en lenguaje natural

## 🚀 Inicio Rápido

### Requisitos

- Python >= 3.12
- UV (gestor de paquetes)

### Instalación

```bash
# Instalar dependencias
uv sync
```

### Ejecución

```bash
uv run app
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8550`

## 📖 Uso

1. **Selecciona un municipio**: Usa la búsqueda o lista
2. **Explora información**: Click en preguntas de consulta rápida
3. **Pregunta libremente**: Escribe en el chat
4. **Cambia de municipio**: Selecciona otro en cualquier momento

## 📁 Estructura del Proyecto

```
ai-muni-rec/
├── src/ai_muni_rec/
│   ├── main.py                 # Punto de entrada
│   ├── config.py               # Configuración
│   ├── core/                   # Lógica de negocio
│   │   ├── data_loader.py      # Carga de datos
│   │   └── query_processor.py  # Procesador de consultas
│   └── ui/                     # Interfaz de usuario
│       ├── app.py              # Aplicación principal
│       ├── styles.py           # Diseño y estilos
│       ├── chat_view.py        # Componente de chat
│       ├── municipality_selector.py  # Selector
│       └── quick_query_buttons.py    # Botones rápidos
├── data/processed/             # Datos municipales
├── knowledge/                  # Base de conocimiento Prolog
└── docs/                       # Documentación extendida
```

## 🔌 Integración con Prolog

El sistema utiliza **PySwip** para integrar el procesamiento de lenguaje natural de Prolog con la interfaz de Python/Flet.

### Cómo funciona:

1. **Selección de Municipio**: Cuando seleccionas un municipio (ej: "Abejones"), el sistema:
   - Carga el nombre completo: "Abejones"
   - Obtiene el nombre normalizado: "abejones"
   - Obtiene el código: "20001"

2. **Procesamiento de Consultas**: Al escribir una pregunta:
   - Se normaliza el texto (minúsculas, sin acentos)
   - Se envía a Prolog con el nombre normalizado del municipio
   - Prolog procesa la consulta usando `Procesamiento_lenguaje.pl`
   - La respuesta se formatea y muestra en el chat

3. **Ejemplos de consultas**:
   ```
   ¿Cuál es el estado del municipio?
   ¿Qué prioridad tiene educación?
   ¿Cuáles aspectos tienen nivel alto?
   ¿Cuál es el estado de marginación?
   ```

### Archivos clave:

- `knowledge/Procesamiento_lenguaje.pl`: Motor de PLN en Prolog
- `src/ai_muni_rec/core/query_processor.py`: Interfaz Python-Prolog
- `src/ai_muni_rec/core/data_loader.py`: Mapeo de nombres de municipios
- `knowledge/INTEGRACION_PROLOG_PYTHON.md`: Documentación detallada

### Probar la integración:

```bash
# Prueba completa con Prolog
python scripts/test_prolog_integration.py

# Solo prueba el mapeo de municipios (sin Prolog)
python scripts/test_prolog_integration.py --mapping-only
```

## 🛠️ Desarrollo

### Estructura de datos:

El sistema usa dos archivos CSV principales:
- `data/processed/dataset_municipal_v2.csv`: Datos demográficos y socioeconómicos
- `data/processed/indicators_municipal_v2.csv`: Indicadores y nombres normalizados

### Agregar nuevas consultas:

1. Edita `knowledge/Procesamiento_lenguaje.pl`
2. Agrega nuevas reglas DCG para el tipo de pregunta
3. No requiere cambios en el código Python

### Dependencias principales:

- **Flet**: Framework de UI multiplataforma
- **PySwip**: Interface Python-Prolog
- **Pandas**: Análisis de datos (notebooks)
- **SWI-Prolog**: Motor de Prolog (debe estar instalado en el sistema)

### Instalar SWI-Prolog:

```bash
# Ubuntu/Debian
sudo apt-get install swi-prolog

# macOS
brew install swi-prolog

# Verificar instalación
swipl --version
```

## 📄 Licencia

Proyecto educativo para el curso de maestría.
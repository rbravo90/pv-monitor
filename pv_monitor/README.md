# PV Monitor

Sistema de monitoreo remoto de plantas fotovoltaicas.

**Extensión de la memoria de título:**  
*Desarrollo de un sistema de monitoreo remoto de plantas fotovoltaicas*  
Rodrigo Alfonso Bravo Moreno (2020) – Universidad de Chile  
Profesor Guía: Juan Peypouquet

## Características

- Modelo de generación con factor de pérdida + modelo térmico de Sandia
- Extrapolación de velocidad de viento a la altura de los módulos (perfil logarítmico)
- Clasificación de cielo despejado (Engerer)
- Residual clear-sky activo
- Modelo de degradación lineal + Time-to-Threshold (predicción de fallas)
- Cálculo de Active Performance Ratio y otros KPIs

## Estructura del proyecto

```text
pv_monitor/
├── config/           # Configuración de planta y umbrales
├── data/             # Datos crudos, procesados y de ejemplo
├── src/              # Código fuente principal
├── notebooks/        # Exploración y validación
├── scripts/          # Pipelines y generación de reportes
├── tests/            # Tests unitarios
├── requirements.txt
└── README.md
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

## Uso rápido

```python
from src.generation_model import expected_power
from src.wind_extrapolation import logarithmic_profile
# ... etc
```

## Próximos pasos

1. Completar implementación de clearsky (Engerer completo)
2. Pipeline de carga de datos satelitales (Solcast / Merra)
3. Script de reporte mensual
4. Tests unitarios
5. Notebook de validación con datos de la planta piloto

## Autor

Rodrigo Alfonso Bravo Moreno  
Extensiones desarrolladas en colaboración con Grok (xAI) – 2026

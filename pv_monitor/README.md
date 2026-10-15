# PV Monitor

Aplicación gratuita para monitoreo, optimización y predicción de fallas en sistemas fotovoltaicos de **pequeña y mediana escala** (domiciliarios, edificios, comunidades, galpones, etc.) en Chile.

## Funcionalidades principales

- Mapa interactivo de Chile para ubicar plantas
- Cálculo de producción energética según parámetros de la planta
- Optimización de inclinación y azimut
- Mapa de calor de potencial solar
- Cuentas de usuario asociadas a correo
- Creación y gestión de plantas FV
- Monitoreo del estado de la planta
- Sistema de alertas por detección y pronóstico de fallas

## Stack

- **Frontend**: Next.js + Tailwind + Leaflet
- **Backend**: FastAPI (Python)
- **Base de datos**: PostgreSQL / Supabase
- **Autenticación**: Supabase Auth o Firebase
- **Datos**: APIs gratuitas (Ministerio de Energía, DMC, etc.)

## Estructura

```text
├── backend/          # API FastAPI
├── frontend/         # Aplicación Next.js
├── pv_monitor/       # Código original de modelos (factor de pérdida, residual, etc.)
└── docs/
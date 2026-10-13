#!/usr/bin/env python
"""
Pipeline principal de monitoreo y predicción de fallas.
"""

from pathlib import Path
import yaml
import pandas as pd

# Ajustar path para importar desde src
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.generation_model import expected_power
from src.residual import clearsky_active_residual
from src.degradation import linear_degradation_fit, time_to_threshold
from src.kpis import active_performance_ratio


def load_config(path: str = "config/config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    cfg = load_config()
    print("Configuración cargada:", cfg["plant"]["name"])
    print("Listo para conectar datos reales o sintéticos.")
    # Aquí se conectará la carga de datos y el pipeline completo


if __name__ == "__main__":
    main()

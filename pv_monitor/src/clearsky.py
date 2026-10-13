"""
Clasificación de cielo despejado (método de Engerer)
y construcción del conjunto activo.
"""

from __future__ import annotations
import numpy as np
import pandas as pd


def clearsky_mask(
    kt: pd.Series | np.ndarray,
    dhi: pd.Series | np.ndarray | None = None,
    dni: pd.Series | np.ndarray | None = None,
    kt_threshold: float = 0.9,
    variability_threshold: float = 0.10,
) -> np.ndarray:
    """
    Máscara booleana de cielo despejado (simplificación del método de Engerer).

    Criterios básicos:
    - Kt > kt_threshold
    - (opcional) baja variabilidad de DNI
    """
    mask = np.asarray(kt) > kt_threshold

    if dni is not None:
        # Variabilidad relativa simple (puede refinarse)
        dni_arr = np.asarray(dni)
        # Ejemplo: diferencia relativa con valor vecino
        # (en la memoria original se usa ΔDNI ≤ 10 %)
        pass  # placeholder para implementación completa

    return mask


def active_mask(
    p_med: pd.Series | np.ndarray,
    p_esp: pd.Series | np.ndarray,
    p_threshold: float,
) -> np.ndarray:
    """
    Conjunto activo J: potencia medida > 0 y potencia esperada > umbral.
    """
    p_med = np.asarray(p_med)
    p_esp = np.asarray(p_esp)
    return (p_med > 0) & (p_esp > p_threshold)

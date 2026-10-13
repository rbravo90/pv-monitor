"""
Modelo de degradación lineal (y opcionalmente exponencial)
+ cálculo de Time-to-Threshold (TTF).
"""

from __future__ import annotations
import numpy as np
import pandas as pd
from scipy import stats


def linear_degradation_fit(
    residual_cs: pd.Series,
    min_points: int = 30,
) -> dict:
    """
    Ajuste lineal: r_CS(t) = α + β t + ε

    Returns
    -------
    dict con alpha, beta, r_value, p_value, std_err, n_points
    """
    s = residual_cs.dropna()
    if len(s) < min_points:
        raise ValueError(f"Se necesitan al menos {min_points} puntos válidos")

    # Convertir índice temporal a días desde el primer punto
    t = (s.index - s.index[0]).total_seconds() / 86400.0  # días
    r = s.values

    slope, intercept, r_value, p_value, std_err = stats.linregress(t, r)

    return {
        "alpha": intercept,
        "beta": slope,
        "r_value": r_value,
        "p_value": p_value,
        "std_err": std_err,
        "n_points": len(s),
        "t0": s.index[0],
    }


def time_to_threshold(
    current_residual: float,
    beta: float,
    residual_crit: float = 0.05,
    current_time: pd.Timestamp | None = None,
) -> float | None:
    """
    Tiempo estimado (en días) hasta alcanzar residual_crit.

    t_falla = (r_crit - r_actual) / β
    """
    if beta <= 0:
        return None  # no hay degradación positiva

    days = (residual_crit - current_residual) / beta
    return max(days, 0.0)

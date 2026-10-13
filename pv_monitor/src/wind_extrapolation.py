"""
Extrapolación de velocidad de viento a la altura de los módulos.
Modelos: perfil logarítmico (recomendado) y ley de potencia.
"""

from __future__ import annotations
import numpy as np
import pandas as pd


def logarithmic_profile(
    wind_speed_ref: float | np.ndarray | pd.Series,
    height_ref: float = 10.0,
    height_target: float = 2.0,
    roughness_length: float = 0.03,
) -> float | np.ndarray | pd.Series:
    """
    Perfil logarítmico de velocidad de viento.

    v(z) = v(z_r) * ln(z / z0) / ln(z_r / z0)

    Parameters
    ----------
    wind_speed_ref : velocidad a la altura de referencia (m/s)
    height_ref : altura de referencia (m), normalmente 10 m
    height_target : altura de los módulos (m)
    roughness_length : longitud de rugosidad z0 (m)

    Returns
    -------
    Velocidad estimada a height_target (m/s)
    """
    if height_target <= 0 or height_ref <= 0 or roughness_length <= 0:
        raise ValueError("Alturas y z0 deben ser positivos")

    ratio = np.log(height_target / roughness_length) / np.log(height_ref / roughness_length)
    return wind_speed_ref * ratio


def power_law_profile(
    wind_speed_ref: float | np.ndarray | pd.Series,
    height_ref: float = 10.0,
    height_target: float = 2.0,
    exponent: float = 0.14,
) -> float | np.ndarray | pd.Series:
    """
    Ley de potencia (Hellmann).

    v(z) = v(z_r) * (z / z_r)^α
    """
    if height_target <= 0 or height_ref <= 0:
        raise ValueError("Alturas deben ser positivas")

    return wind_speed_ref * (height_target / height_ref) ** exponent

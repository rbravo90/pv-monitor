"""
Modelo de generación fotovoltaica con factor de pérdida
+ modelo térmico de Sandia (King et al., 2004).

Basado en la memoria de Rodrigo Bravo Moreno (2020).
"""

from __future__ import annotations
import numpy as np
import pandas as pd
from .wind_extrapolation import logarithmic_profile


def module_temperature_sandia(
    poa: float | np.ndarray | pd.Series,
    temp_air: float | np.ndarray | pd.Series,
    wind_speed: float | np.ndarray | pd.Series,
    a: float = -3.56,
    b: float = -0.0750,
) -> float | np.ndarray | pd.Series:
    """
    Temperatura de la cara trasera del módulo (Sandia).

    Tm = Gpoa * exp(a + b * WS) + Ta
    """
    return poa * np.exp(a + b * wind_speed) + temp_air


def expected_power(
    poa: float | np.ndarray | pd.Series,
    temp_air: float | np.ndarray | pd.Series,
    wind_speed_10m: float | np.ndarray | pd.Series,
    p_sn: float,
    f_fv: float = 0.85,
    kappa: float = -0.004,
    t_r: float = 25.0,
    module_height: float = 2.0,
    roughness_length: float = 0.03,
    sandia_a: float = -3.56,
    sandia_b: float = -0.0750,
    g_stc: float = 1000.0,
) -> float | np.ndarray | pd.Series:
    """
    Potencia esperada (modelo con factor de pérdida).

    P_esp = P_sn * f_fv * (Gpoa / Gstc) * [1 + κ (Tm - Tr)]
    """
    # Extrapolación de viento a altura de módulos
    ws_module = logarithmic_profile(
        wind_speed_10m,
        height_ref=10.0,
        height_target=module_height,
        roughness_length=roughness_length,
    )

    tm = module_temperature_sandia(poa, temp_air, ws_module, a=sandia_a, b=sandia_b)

    p_esp = p_sn * f_fv * (poa / g_stc) * (1.0 + kappa * (tm - t_r))
    return np.maximum(p_esp, 0.0)  # no permitir potencia negativa

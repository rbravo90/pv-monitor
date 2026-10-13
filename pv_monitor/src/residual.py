"""
Cálculo del residual relativo y residual clear-sky activo.
"""

from __future__ import annotations
import numpy as np
import pandas as pd


def relative_residual(
    p_med: float | np.ndarray | pd.Series,
    p_esp: float | np.ndarray | pd.Series,
) -> float | np.ndarray | pd.Series:
    """
    r(t) = 1 - P_med / P_esp
    """
    p_esp = np.asarray(p_esp)
    p_med = np.asarray(p_med)

    with np.errstate(divide="ignore", invalid="ignore"):
        r = 1.0 - p_med / p_esp
        r = np.where(p_esp > 0, r, np.nan)
    return r


def clearsky_active_residual(
    p_med: pd.Series,
    p_esp: pd.Series,
    clearsky_mask: np.ndarray,
    active_mask: np.ndarray,
) -> pd.Series:
    """
    Residual solo en instantes clear-sky y activos (r_CS).
    """
    r = relative_residual(p_med, p_esp)
    mask = clearsky_mask & active_mask
    r_cs = pd.Series(np.where(mask, r, np.nan), index=p_med.index)
    return r_cs

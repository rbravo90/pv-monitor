"""
Cálculo de KPIs, incluyendo Active Performance Ratio.
"""

from __future__ import annotations
import numpy as np
import pandas as pd


def performance_ratio(
    p_med: pd.Series | np.ndarray,
    p_esp: pd.Series | np.ndarray,
) -> pd.Series | np.ndarray:
    """
    PR = P_med / P_esp
    """
    with np.errstate(divide="ignore", invalid="ignore"):
        pr = np.asarray(p_med) / np.asarray(p_esp)
        pr = np.where(np.asarray(p_esp) > 0, pr, np.nan)
    return pr


def active_performance_ratio(
    p_med: pd.Series,
    p_esp: pd.Series,
    active_mask: np.ndarray,
) -> float:
    """
    Active PR: promedio de PR solo en instantes activos.
    """
    pr = performance_ratio(p_med, p_esp)
    pr_active = pr[active_mask]
    return float(np.nanmean(pr_active))

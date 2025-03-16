"""Warhammer Fantasy Roleplay 1st edition StatBlocks."""
from ttrpg_dice import d, statblock


@statblock
class Warhammer:
    """WRFP1e StatBlock Base."""

    M = d(20) # No tests, but > 20 not plausible
    WS = d(100)
    BS = d(100)
    S = d(10)
    T = d(10)
    W = d(100)
    I = d(100)  # noqa: E741
    A = d(20) # No tests, but > 20 not plausible
    Dex = d(100)
    Ld = d(100)
    Int = d(100)
    Cl = d(100)
    WP = d(100)
    Fel = d(100)

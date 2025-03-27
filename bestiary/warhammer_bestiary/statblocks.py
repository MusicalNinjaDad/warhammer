"""Warhammer Fantasy Roleplay 1st edition StatBlocks."""

from functools import partial
from textwrap import indent

from ttrpg_dice import d, statblock


@statblock
class Warhammer:
    """WRFP1e StatBlock Base."""

    M = d(20)  # No tests, but > 20 not plausible
    WS = d(100)
    BS = d(100)
    S = d(10)
    T = d(10)
    W = d(100)
    I = d(100)  # noqa: E741
    A = d(20)  # No tests, but > 20 not plausible
    Dex = d(100)
    Ld = d(100)
    Int = d(100)
    Cl = d(100)
    WP = d(100)
    Fel = d(100)


def generate_class(beast: str, statblocks: dict[str, dict[str, int | str]]) -> list[str]:
    """Create a Warhammer StatBlock from a key, value pair of scraped results."""
    indented = partial(indent, prefix="    ")

    def safe(s: str) -> str:
        return s.replace(" ", "_")

    def classdef(name: str, stats: dict):
        return [f"class {safe(name)}(Warhammer):"] + [indented(f"{stat} = {val}") for stat, val in stats.items()] + [""]

    if len(statblocks) == 1:
        stats = next(iter(statblocks.values()))
        return classdef(beast, stats)

    return [f"class {safe(beast)}:"] + [
        indented(line) for name, stats in statblocks.items() for line in classdef(name, stats)
    ]

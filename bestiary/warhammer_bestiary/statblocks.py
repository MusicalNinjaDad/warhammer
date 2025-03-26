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

def generate_class(beast: str, statblocks: dict[str, dict[str, int | str]]) -> list[str]:
    """Create a Warhammer StatBlock froma key, value pair of scraped results."""
    if len(statblocks) == 1:
        return [f"class {beast}(Warhammer):"] + [
            f"    {stat} = {val}" for stat, val in statblocks["Basic Profile"].items()
        ]
    pyclass = [f"class {beast}:"]
    for name, stats in statblocks.items():
        pyclass.append(f"    class {name.replace(" ", "_")}(Warhammer):")
        for stat, val in stats.items():
            pyclass.append(f"        {stat} = {val}")
        pyclass.append("")
    return pyclass[:-1]
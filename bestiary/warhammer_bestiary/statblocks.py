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


def generate_class(name: str, value: dict[str, dict | int | str] | int | str) -> list[str]:
    """Create a Warhammer StatBlock from a key, value pair of scraped results."""
    indented = partial(indent, prefix="    ")

    def safe(s: str) -> str:
        return s.replace(" ", "_")

    match value:
        case dict():
            if len(value) == 1:
                # Ignore the profile name for single profile beasts and profile groupings with only one entry.
                value = next(iter(value.values()))
            match next(iter(value.values())):
                # lookahead to the first entry
                case dict():
                    is_grouping = True
                    base = ""
                case _:
                    is_grouping = False
                    base = "(Warhammer)"
            return (
                [f"class {safe(name)}{base}:"]
                + [indented(line) for profile_or_stat in value.items() for line in generate_class(*profile_or_stat)]
                + ([""] if not is_grouping else [])
            )
        case _:
            return [f"{name} = {value}"]

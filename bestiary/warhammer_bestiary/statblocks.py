"""Warhammer Fantasy Roleplay 1st edition StatBlocks."""

import re
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

    def safe(s: str, *, identifier: bool = False) -> str:
        s.strip().removeprefix("+")
        s = s.encode("ascii", errors="ignore").decode().strip().replace(" ", "_")
        return s if not identifier or s.isidentifier() else "".join(c if c.isalnum() or c == "_" else "" for c in s)

    safename = safe(name, identifier=True)

    match value:
        case dict():
            # Ignore the profile / group name if it is the only one:
            # use the higher-level identifier and grab the relevant stats from down the tree
            if len(value) == 1:
                return generate_class(name, next(iter(value.values())))

            match next(iter(value.values())):  # lookahead to the first entry
                case dict():
                    is_grouping = True
                    base = ""
                case _:
                    is_grouping = False
                    base = "(Warhammer)"
            return (
                [f"class {safename}{base}:"]
                + [indented(line) for profile_or_stat in value.items() for line in generate_class(*profile_or_stat)]
                + ([""] if not is_grouping else [])  # blank line after each profile but no double lines after groups
            )

        case int():
            return [f"{safename} = {value}"]

        case str():
            safevalue = safe(value).lower()

            if "d" in safevalue:  # Assume valid ndx dice notation
                return [f'{safename} = d.from_str("{safevalue}")']

            try:
                numericalvalue = int(safevalue)  # maybe we just had some wierd symbol after the value
            except ValueError:
                try:
                    numericalvalue = int(re.search(r"\d+", safevalue).group())  # get the first number (e.g. "3-5" -> 3)
                except AttributeError:  # if no digits are present: 'NoneType' object has no attribute 'group'
                    numericalvalue = 0
            return [f"{safename} = {numericalvalue}"]

        case _:
            msg = f"Cannot process {name} = {value:r}"
            raise TypeError(msg)

if __name__ == "__main__":
    import json

    from warhammer_bestiary.scraper import BEASTFILE, NPCFILE
    
    npcs: dict = json.loads(NPCFILE.read_text())
    beasts: dict[str,dict] = json.loads(BEASTFILE.read_text())

    _ = beasts["Chaos Beastman"].pop("Special Rules") # belongs in careers

    beast_classes = BEASTFILE.with_suffix(".py")
    npc_classes = NPCFILE.with_suffix(".py")

    beast_classes.write_text(
        "\n".join(line for beast, stats in beasts.items() if stats for line in generate_class(beast, stats)),
    )

    npc_classes.write_text(
        "\n".join(line for npc, stats in npcs.items() if stats for line in generate_class(npc, stats)),
    )
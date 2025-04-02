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

type StatsDict = dict[str, StatsValue]
type StatsValue = int | str

def generate_class(name: str, value: dict[str, StatsDict] | StatsDict | StatsValue) -> list[str]:
    """Create a Warhammer StatBlock from a key, value pair of scraped results."""
    indented = partial(indent, prefix="    ")

    def safe(s: str, *, identifier: bool = False) -> str:
        s.strip().removeprefix("+")
        s = s.encode("ascii", errors="ignore").decode().strip().replace(" ", "_")
        return s if not identifier or s.isidentifier() else "".join(c if c.isalnum() or c == "_" else "" for c in s)

    safename = safe(name, identifier=True)

    match value:
        case dict():
            if _single_entry_dict_needs_flattening := len(value) == 1:
                entry_name, entry_values = next(iter(value.items())) 
                best_valid_name = safename if safename else entry_name
                return generate_class(best_valid_name, entry_values)

            dict_of_what = next(iter(value.values()))
            match dict_of_what:
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
            
            # get the first number (e.g. "13-25" -> 13)
            numbers_in_string = re.search(r"\d+", safevalue)
            try:
                numericalvalue = int(numbers_in_string.group(0))
            except AttributeError:  # if no numbers are present: 'NoneType' object has no attribute 'group'
                numericalvalue = 0
            return [f"{safename} = {numericalvalue}"]

        case _:
            msg = f"Cannot process {name} = {value:r}"
            raise TypeError(msg)

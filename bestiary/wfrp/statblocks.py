"""Warhammer Fantasy Roleplay 1st edition StatBlocks."""

import re
from enum import Enum, auto
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


class ClassOrInstance(Enum):  # noqa: D101
    classes = auto()
    instances = auto()


def generate_class(  # noqa: C901, PLR0912
    name: str,
    value: dict[str, StatsDict] | StatsDict | StatsValue,
    generate: ClassOrInstance,
) -> list[str]:
    """Create a Warhammer StatBlock from a key, value pair of scraped results."""
    indented = partial(indent, prefix="    ")

    def safe(s: str, *, identifier: bool = False) -> str:
        s = s.strip().removeprefix("+")
        s = s.encode("ascii", errors="ignore").decode().strip().replace(" ", "_")
        return s if not identifier or s.isidentifier() else "".join(c if c.isalnum() or c == "_" else "" for c in s)

    safename = safe(name, identifier=True)

    match value:
        case dict():
            if _single_entry_dict_needs_flattening := len(value) == 1:
                entry_name, entry_values = next(iter(value.items()))
                best_valid_name = safename or entry_name
                return generate_class(name=best_valid_name, value=entry_values, generate=generate)

            first_value = next(iter(value.values()))
            is_grouping = isinstance(first_value, dict)
            match is_grouping, generate:
                case True, _:
                    first_line = [f"class {safename}:"]
                    last_lines = []
                case False, ClassOrInstance.classes:
                    first_line = [f"class {safename}(Warhammer):"]
                    last_lines = [""]
                case False, ClassOrInstance.instances:
                    first_line = [f"{safename} = Warhammer("]
                    last_lines = [")", ""]
                case _:
                    msg = f"Cannot generate a {generate}"
                    raise ValueError(msg)
            return (
                first_line
                + [
                    indented(line)
                    for profile_or_stat in value.items()
                    for line in generate_class(*profile_or_stat, generate=generate)
                ]
                + last_lines
            )

        case int():
            statvalue = value

        case str():
            safevalue = safe(value).lower()

            if "d" in safevalue:  # Assume valid ndx dice notation
                statvalue = f'd.from_str("{safevalue}")'

            else:  # get the first number (e.g. "13-25" -> 13)
                numbers_in_string = re.search(r"\d+", safevalue)
                statvalue = 0 if numbers_in_string is None else int(numbers_in_string.group(0))
                    

    match generate:
        case ClassOrInstance.instances:
            return [f"{safename}={statvalue},"]
        case ClassOrInstance.classes:
            return [f"{safename} = {statvalue}"]
        case _:
            msg = f"Cannot generate a {generate}"
            raise ValueError(msg)

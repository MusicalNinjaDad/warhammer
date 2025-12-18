"""
Create Warhammer Fantasy Roleplay 1st edition StatBlocks from scraped info.

Run as a module with `python -m wfrp.gen_statblocks`
"""

if __name__ == "__main__":
    import json

    from .scraper import BEASTFILE, CAREERFILE, NPCFILE
    from .statblocks import ClassOrInstance, generate_class

    npcs: dict = json.loads(NPCFILE.read_text())
    beasts: dict[str, dict] = json.loads(BEASTFILE.read_text())
    careers: dict[str, dict] = json.loads(CAREERFILE.read_text())

    careers["Chaos Beastman"] = beasts["Chaos Beastman"].pop("Special Rules")  # belongs in careers
    npcs["Soldiers"] = beasts.pop("Soldiers") # belongs in NPCs

    beast_classes = BEASTFILE.with_suffix(".py")
    npc_classes = NPCFILE.with_suffix(".py")
    career_classes = CAREERFILE.with_suffix(".py")

    imports = [
        "# ruff: noqa: RUF100, D100, D101, D106, E741, N801, N999",
        "from ttrpg_dice import d  # noqa: F401",
        "",
        "from .statblocks import Warhammer",
        "",
    ]

    beast_classes.write_text(
        "\n".join(
            [
                *imports,
                "",
                *(
                    line
                    for beast, stats in beasts.items()
                    if stats
                    for line in generate_class(beast, stats, generate=ClassOrInstance.classes)
                ),
            ],
        ),
    )

    npc_classes.write_text(
        "\n".join(
            [
                *imports,
                "",
                *(
                    line
                    for npc, stats in npcs.items()
                    if stats
                    for line in generate_class(npc, stats, generate=ClassOrInstance.classes)
                ),
            ],
        ),
    )

    career_classes.write_text(
        "\n".join(
            [
                *imports,
                *(
                    line
                    for career, stats in careers.items()
                    if stats
                    for line in generate_class(career, stats, generate=ClassOrInstance.instances)
                ),
            ],
        ),
    )

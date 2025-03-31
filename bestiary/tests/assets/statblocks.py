from dataclasses import dataclass


@dataclass
class StatBlockTestCase:
    beast: str
    stats: dict[str, int | str]
    statblock_class: list[str]


amoeba = StatBlockTestCase(
    beast="Amoeba",
    stats={
        "": {
            "Basic Profile": {
                "M": 4,
                "WS": 33,
                "BS": 0,
                "S": 3,
                "T": 5,
                "W": 11,
                "I": 30,
                "A": 3,
                "Dex": 0,
                "Ld": 0,
                "Int": 0,
                "Cl": 0,
                "WP": 0,
                "Fel": 0,
            },
        },
    },
    statblock_class=[
        "class Amoeba(Warhammer):",
        "    M = 4",
        "    WS = 33",
        "    BS = 0",
        "    S = 3",
        "    T = 5",
        "    W = 11",
        "    I = 30",
        "    A = 3",
        "    Dex = 0",
        "    Ld = 0",
        "    Int = 0",
        "    Cl = 0",
        "    WP = 0",
        "    Fel = 0",
        "",
    ],
)

thugs = StatBlockTestCase(
    beast="Thugs",
    stats={
        "Thug": {
            "Basic Profile": {
                "M": 4,
                "WS": 31,
                "BS": 25,
                "S": 3,
                "T": 4,
                "W": 7,
                "I": 30,
                "A": 1,
                "Dex": 29,
                "Ld": 29,
                "Int": 29,
                "Cl": 29,
                "WP": 29,
                "Fel": 29,
            },
        },
        "Teamsters or Stevedores": {
            "Basic Profile": {
                "M": 4,
                "WS": 33,
                "BS": 25,
                "S": 3,
                "T": 4,
                "W": 8,
                "I": 30,
                "A": 1,
                "Dex": 34,
                "Ld": 28,
                "Int": 33,
                "Cl": 30,
                "WP": 32,
                "Fel": 29,
            },
        },
    },
    statblock_class=[
        "class Thugs:",
        "    class Thug(Warhammer):",
        "        M = 4",
        "        WS = 31",
        "        BS = 25",
        "        S = 3",
        "        T = 4",
        "        W = 7",
        "        I = 30",
        "        A = 1",
        "        Dex = 29",
        "        Ld = 29",
        "        Int = 29",
        "        Cl = 29",
        "        WP = 29",
        "        Fel = 29",
        "",
        "    class Teamsters_or_Stevedores(Warhammer):",
        "        M = 4",
        "        WS = 33",
        "        BS = 25",
        "        S = 3",
        "        T = 4",
        "        W = 8",
        "        I = 30",
        "        A = 1",
        "        Dex = 34",
        "        Ld = 28",
        "        Int = 33",
        "        Cl = 30",
        "        WP = 32",
        "        Fel = 29",
        "",
    ],
)

soldiers = StatBlockTestCase(
    beast="Soldiers",
    stats={
        "Generic Soldier": {
            "Basic Profile": {
                "M": 4,
                "WS": 43,
                "BS": 35,
                "S": 3,
                "T": 3,
                "W": 8,
                "I": 40,
                "A": 1,
                "Dex": 29,
                "Ld": 39,
                "Int": 29,
                "Cl": 29,
                "WP": 29,
                "Fel": 29,
            },
        },
        "The Imperial Guard": {
            "Cavalry Officer": {
                "M": 4,
                "WS": 65,
                "BS": 50,
                "S": 5,
                "T": 5,
                "W": 13,
                "I": 50,
                "A": 3,
                "Dex": 49,
                "Ld": 69,
                "Int": 39,
                "Cl": 69,
                "WP": 40,
                "Fel": 50,
            },
            "Cavalryman": {
                "M": 4,
                "WS": 50,
                "BS": 38,
                "S": 4,
                "T": 4,
                "W": 11,
                "I": 50,
                "A": 3,
                "Dex": 39,
                "Ld": 39,
                "Int": 29,
                "Cl": 40,
                "WP": 29,
                "Fel": 30,
            },
            "Officer": {
                "M": 4,
                "WS": 60,
                "BS": 45,
                "S": 5,
                "T": 5,
                "W": 13,
                "I": 60,
                "A": 3,
                "Dex": 49,
                "Ld": 69,
                "Int": 40,
                "Cl": 60,
                "WP": 40,
                "Fel": 50,
            },
            "Soldier": {
                "M": 4,
                "WS": "50♦",
                "BS": "40♦",
                "S": 4,
                "T": 4,
                "W": 11,
                "I": 50,
                "A": 2,
                "Dex": 39,
                "Ld": 39,
                "Int": 29,
                "Cl": 40,
                "WP": 29,
                "Fel": 30,
            },
            "Mercenary Captain": {
                "M": 4,
                "WS": 55,
                "BS": 45,
                "S": 4,
                "T": 4,
                "W": 11,
                "I": 55,
                "A": 2,
                "Dex": 39,
                "Ld": 55,
                "Int": 39,
                "Cl": 50,
                "WP": 35,
                "Fel": 45,
            },
            "Mercenary Soldier": {
                "M": 4,
                "WS": 45,
                "BS": 35,
                "S": 3,
                "T": 4,
                "W": 8,
                "I": 45,
                "A": 2,
                "Dex": 29,
                "Ld": 39,
                "Int": 29,
                "Cl": 35,
                "WP": 25,
                "Fel": 30,
            },
            "Templar": {
                "M": 4,
                "WS": 70,
                "BS": 55,
                "S": 5,
                "T": 5,
                "W": 15,
                "I": 70,
                "A": 3,
                "Dex": 59,
                "Ld": 59,
                "Int": 50,
                "Cl": 65,
                "WP": 60,
                "Fel": 59,
            },
            "Halfling Infantry": {
                "M": 3,
                "WS": 38,
                "BS": 45,
                "S": 3,
                "T": 3,
                "W": 8,
                "I": 60,
                "A": 2,
                "Dex": 49,
                "Ld": 30,
                "Int": 29,
                "Cl": 34,
                "WP": 55,
                "Fel": 53,
            },
        },
        "Standing Armies In The Empire": {
            "Sergeant": {
                "M": 4,
                "WS": 50,
                "BS": 30,
                "S": 4,
                "T": 4,
                "W": 11,
                "I": 50,
                "A": 2,
                "Dex": 39,
                "Ld": 55,
                "Int": 40,
                "Cl": 50,
                "WP": 35,
                "Fel": 40,
            },
            "Soldier": {
                "M": 4,
                "WS": 45,
                "BS": 30,
                "S": 3,
                "T": 3,
                "W": 7,
                "I": 40,
                "A": 1,
                "Dex": 29,
                "Ld": 39,
                "Int": 29,
                "Cl": 29,
                "WP": 25,
                "Fel": 30,
            },
            "Pikeman": {
                "M": 4,
                "WS": 45,
                "BS": 30,
                "S": 3,
                "T": 3,
                "W": 7,
                "I": 40,
                "A": 1,
                "Dex": 29,
                "Ld": 40,
                "Int": 29,
                "Cl": 30,
                "WP": 26,
                "Fel": 29,
            },
            "Mercenary Crossbowman": {
                "M": 4,
                "WS": 40,
                "BS": 50,
                "S": 3,
                "T": 4,
                "W": 9,
                "I": 45,
                "A": 2,
                "Dex": 39,
                "Ld": 39,
                "Int": 29,
                "Cl": 35,
                "WP": 30,
                "Fel": 35,
            },
            "Gunnery Captain": {
                "M": 4,
                "WS": 54,
                "BS": 30,
                "S": 3,
                "T": 3,
                "W": 9,
                "I": 45,
                "A": 1,
                "Dex": 29,
                "Ld": 50,
                "Int": 29,
                "Cl": 30,
                "WP": 26,
                "Fel": 32,
            },
        },
    },
    statblock_class=[
        "class Soldiers:",
        "    class Generic_Soldier(Warhammer):",
        "        M = 4",
        "        WS = 43",
        "        BS = 35",
        "        S = 3",
        "        T = 3",
        "        W = 8",
        "        I = 40",
        "        A = 1",
        "        Dex = 29",
        "        Ld = 39",
        "        Int = 29",
        "        Cl = 29",
        "        WP = 29",
        "        Fel = 29",
        "",
        "    class The_Imperial_Guard:",
        "        class Cavalry_Officer(Warhammer):",
        "            M = 4",
        "            WS = 65",
        "            BS = 50",
        "            S = 5",
        "            T = 5",
        "            W = 13",
        "            I = 50",
        "            A = 3",
        "            Dex = 49",
        "            Ld = 69",
        "            Int = 39",
        "            Cl = 69",
        "            WP = 40",
        "            Fel = 50",
        "",
        "        class Cavalryman(Warhammer):",
        "            M = 4",
        "            WS = 50",
        "            BS = 38",
        "            S = 4",
        "            T = 4",
        "            W = 11",
        "            I = 50",
        "            A = 3",
        "            Dex = 39",
        "            Ld = 39",
        "            Int = 29",
        "            Cl = 40",
        "            WP = 29",
        "            Fel = 30",
        "",
        "        class Officer(Warhammer):",
        "            M = 4",
        "            WS = 60",
        "            BS = 45",
        "            S = 5",
        "            T = 5",
        "            W = 13",
        "            I = 60",
        "            A = 3",
        "            Dex = 49",
        "            Ld = 69",
        "            Int = 40",
        "            Cl = 60",
        "            WP = 40",
        "            Fel = 50",
        "",
        "        class Soldier(Warhammer):",
        "            M = 4",
        "            WS = 50",
        "            BS = 40",
        "            S = 4",
        "            T = 4",
        "            W = 11",
        "            I = 50",
        "            A = 2",
        "            Dex = 39",
        "            Ld = 39",
        "            Int = 29",
        "            Cl = 40",
        "            WP = 29",
        "            Fel = 30",
        "",
        "        class Mercenary_Captain(Warhammer):",
        "            M = 4",
        "            WS = 55",
        "            BS = 45",
        "            S = 4",
        "            T = 4",
        "            W = 11",
        "            I = 55",
        "            A = 2",
        "            Dex = 39",
        "            Ld = 55",
        "            Int = 39",
        "            Cl = 50",
        "            WP = 35",
        "            Fel = 45",
        "",
        "        class Mercenary_Soldier(Warhammer):",
        "            M = 4",
        "            WS = 45",
        "            BS = 35",
        "            S = 3",
        "            T = 4",
        "            W = 8",
        "            I = 45",
        "            A = 2",
        "            Dex = 29",
        "            Ld = 39",
        "            Int = 29",
        "            Cl = 35",
        "            WP = 25",
        "            Fel = 30",
        "",
        "        class Templar(Warhammer):",
        "            M = 4",
        "            WS = 70",
        "            BS = 55",
        "            S = 5",
        "            T = 5",
        "            W = 15",
        "            I = 70",
        "            A = 3",
        "            Dex = 59",
        "            Ld = 59",
        "            Int = 50",
        "            Cl = 65",
        "            WP = 60",
        "            Fel = 59",
        "",
        "        class Halfling_Infantry(Warhammer):",
        "            M = 3",
        "            WS = 38",
        "            BS = 45",
        "            S = 3",
        "            T = 3",
        "            W = 8",
        "            I = 60",
        "            A = 2",
        "            Dex = 49",
        "            Ld = 30",
        "            Int = 29",
        "            Cl = 34",
        "            WP = 55",
        "            Fel = 53",
        "",
        "    class Standing_Armies_In_The_Empire:",
        "        class Sergeant(Warhammer):",
        "            M = 4",
        "            WS = 50",
        "            BS = 30",
        "            S = 4",
        "            T = 4",
        "            W = 11",
        "            I = 50",
        "            A = 2",
        "            Dex = 39",
        "            Ld = 55",
        "            Int = 40",
        "            Cl = 50",
        "            WP = 35",
        "            Fel = 40",
        "",
        "        class Soldier(Warhammer):",
        "            M = 4",
        "            WS = 45",
        "            BS = 30",
        "            S = 3",
        "            T = 3",
        "            W = 7",
        "            I = 40",
        "            A = 1",
        "            Dex = 29",
        "            Ld = 39",
        "            Int = 29",
        "            Cl = 29",
        "            WP = 25",
        "            Fel = 30",
        "",
        "        class Pikeman(Warhammer):",
        "            M = 4",
        "            WS = 45",
        "            BS = 30",
        "            S = 3",
        "            T = 3",
        "            W = 7",
        "            I = 40",
        "            A = 1",
        "            Dex = 29",
        "            Ld = 40",
        "            Int = 29",
        "            Cl = 30",
        "            WP = 26",
        "            Fel = 29",
        "",
        "        class Mercenary_Crossbowman(Warhammer):",
        "            M = 4",
        "            WS = 40",
        "            BS = 50",
        "            S = 3",
        "            T = 4",
        "            W = 9",
        "            I = 45",
        "            A = 2",
        "            Dex = 39",
        "            Ld = 39",
        "            Int = 29",
        "            Cl = 35",
        "            WP = 30",
        "            Fel = 35",
        "",
        "        class Gunnery_Captain(Warhammer):",
        "            M = 4",
        "            WS = 54",
        "            BS = 30",
        "            S = 3",
        "            T = 3",
        "            W = 9",
        "            I = 45",
        "            A = 1",
        "            Dex = 29",
        "            Ld = 50",
        "            Int = 29",
        "            Cl = 30",
        "            WP = 26",
        "            Fel = 32",
        "",
    ],
)
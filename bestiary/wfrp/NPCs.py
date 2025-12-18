# ruff: noqa: RUF100, D100, D101, D106, E741, N801, N999
from ttrpg_dice import d  # noqa: F401

from .statblocks import Warhammer


class Artisans_Apprentice(Warhammer):
    M = 4
    WS = 31
    BS = 25
    S = 3
    T = 3
    W = 6
    I = 40
    A = 1
    Dex = 39
    Ld = 29
    Int = 29
    Cl = 29
    WP = 29
    Fel = 29

class Beggar:
    class Profile_1(Warhammer):
        M = 4
        WS = 31
        BS = 35
        S = 3
        T = 4
        W = 6
        I = 30
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class Profile_2(Warhammer):
        M = 4
        WS = 33
        BS = 35
        S = 3
        T = 4
        W = 7
        I = 30
        A = 1
        Dex = 30
        Ld = 28
        Int = 34
        Cl = 32
        WP = 32
        Fel = 30

class Boatman:
    class Boatman(Warhammer):
        M = 4
        WS = 31
        BS = 35
        S = 3
        T = 3
        W = 7
        I = 40
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 39
        WP = 29
        Fel = 29

    class Boatman_Captain(Warhammer):
        M = 4
        WS = 40
        BS = 40
        S = 3
        T = 4
        W = 9
        I = 40
        A = 2
        Dex = 30
        Ld = 30
        Int = 30
        Cl = 30
        WP = 30
        Fel = 30

class Bodyguard:
    class Profile_1(Warhammer):
        M = 4
        WS = 41
        BS = 25
        S = 4
        T = 3
        W = 8
        I = 40
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class Profile_2(Warhammer):
        M = 4
        WS = 53
        BS = 25
        S = 4
        T = 3
        W = 8
        I = 45
        A = 2
        Dex = 32
        Ld = 25
        Int = 33
        Cl = 30
        WP = 32
        Fel = 30

class Bounty_Hunter(Warhammer):
    M = 4
    WS = 40
    BS = 40
    S = 3
    T = 3
    W = 9
    I = 40
    A = 2
    Dex = 30
    Ld = 30
    Int = 30
    Cl = 40
    WP = 25
    Fel = 30

class Bunko_Artist(Warhammer):
    M = 4
    WS = 43
    BS = 25
    S = 3
    T = 3
    W = 7
    I = 30
    A = 1
    Dex = 39
    Ld = 29
    Int = 29
    Cl = 29
    WP = 29
    Fel = 40

class Charlatan(Warhammer):
    M = 4
    WS = 43
    BS = 35
    S = 3
    T = 4
    W = 9
    I = 40
    A = 1
    Dex = 59
    Ld = 39
    Int = 43
    Cl = 38
    WP = 40
    Fel = 59

class Coachman(Warhammer):
    M = 4
    WS = 42
    BS = 42
    S = 3
    T = 3
    W = 6
    I = 40
    A = 1
    Dex = 29
    Ld = 29
    Int = 29
    Cl = 40
    WP = 30
    Fel = 32

class Cook:
    class Human_Cook(Warhammer):
        M = 4
        WS = 31
        BS = 25
        S = 3
        T = 3
        W = 7
        I = 30
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 39
        Fel = 29

    class Halfling_Cook(Warhammer):
        M = 3
        WS = 25
        BS = 31
        S = 2
        T = 2
        W = 5
        I = 50
        A = 1
        Dex = 39
        Ld = 19
        Int = 29
        Cl = 19
        WP = 39
        Fel = 39

class Dwarven_Engineer(Warhammer):
    M = 3
    WS = 50
    BS = 30
    S = 3
    T = 4
    W = 7
    I = 20
    A = 1
    Dex = 20
    Ld = 45
    Int = 30
    Cl = 50
    WP = 50
    Fel = 20

class Exciseman(Warhammer):
    M = 4
    WS = 40
    BS = 30
    S = 3
    T = 3
    W = 8
    I = 40
    A = 1
    Dex = 30
    Ld = 30
    Int = 40
    Cl = 40
    WP = 25
    Fel = 25

class Fisherman(Warhammer):
    M = 4
    WS = 30
    BS = 25
    S = 4
    T = 3
    W = 7
    I = 30
    A = 1
    Dex = 45
    Ld = 30
    Int = 25
    Cl = 30
    WP = 30
    Fel = 30

class Gambler(Warhammer):
    M = 4
    WS = 30
    BS = 40
    S = 3
    T = 3
    W = 8
    I = 40
    A = 1
    Dex = 45
    Ld = 30
    Int = 40
    Cl = 25
    WP = 25
    Fel = 40

class Grave_Robber(Warhammer):
    M = 4
    WS = 40
    BS = 40
    S = 3
    T = 3
    W = 7
    I = 40
    A = 1
    Dex = 25
    Ld = 25
    Int = 30
    Cl = 40
    WP = 30
    Fel = 25

class Herbalist(Warhammer):
    M = 4
    WS = 31
    BS = 25
    S = 3
    T = 3
    W = 6
    I = 30
    A = 1
    Dex = 29
    Ld = 29
    Int = 29
    Cl = 29
    WP = 29
    Fel = 29

class High_Elf_Mage(Warhammer):
    M = 4
    WS = 51
    BS = 44
    S = 4
    T = 4
    W = 12
    I = 100
    A = 1
    Dex = 96
    Ld = 83
    Int = 100
    Cl = 100
    WP = 100
    Fel = 43

class Hunter(Warhammer):
    M = 4
    WS = 30
    BS = 50
    S = 4
    T = 3
    W = 8
    I = 40
    A = 1
    Dex = 30
    Ld = 25
    Int = 30
    Cl = 30
    WP = 40
    Fel = 25

class Judicial_Champion(Warhammer):
    M = 4
    WS = 70
    BS = 30
    S = 4
    T = 4
    W = 12
    I = 50
    A = 3
    Dex = 40
    Ld = 30
    Int = 40
    Cl = 50
    WP = 30
    Fel = 25

class Labourer(Warhammer):
    M = 4
    WS = 30
    BS = 25
    S = 3
    T = 4
    W = 7
    I = 30
    A = 1
    Dex = 30
    Ld = 25
    Int = 30
    Cl = 30
    WP = 30
    Fel = 30

class Marine:
    class Marine(Warhammer):
        M = 4
        WS = 40
        BS = 40
        S = 4
        T = 3
        W = 8
        I = 30
        A = 2
        Dex = 25
        Ld = 30
        Int = 30
        Cl = 40
        WP = 30
        Fel = 30

    class Marine_Sergeant(Warhammer):
        M = 4
        WS = 50
        BS = 40
        S = 4
        T = 4
        W = 10
        I = 40
        A = 3
        Dex = 30
        Ld = 40
        Int = 30
        Cl = 40
        WP = 30
        Fel = 30

class Noble(Warhammer):
    M = 4
    WS = 31
    BS = 25
    S = 3
    T = 3
    W = 6
    I = 30
    A = 1
    Dex = 29
    Ld = 39
    Int = 29
    Cl = 39
    WP = 29
    Fel = 39

class Pedlar(Warhammer):
    M = 4
    WS = 40
    BS = 40
    S = 4
    T = 3
    W = 8
    I = 40
    A = 1
    Dex = 30
    Ld = 25
    Int = 25
    Cl = 40
    WP = 30
    Fel = 40

class Physician(Warhammer):
    M = 4
    WS = 31
    BS = 25
    S = 3
    T = 4
    W = 8
    I = 40
    A = 1
    Dex = 49
    Ld = 39
    Int = 49
    Cl = 39
    WP = 39
    Fel = 29

class Pirate(Warhammer):
    M = 4
    WS = 50
    BS = 40
    S = 4
    T = 4
    W = 10
    I = 45
    A = 2
    Dex = 45
    Ld = 50
    Int = 30
    Cl = 50
    WP = 45
    Fel = 30

class Pit_Fighter(Warhammer):
    M = 4
    WS = 50
    BS = 30
    S = 4
    T = 4
    W = 8
    I = 40
    A = 1
    Dex = 40
    Ld = 25
    Int = 30
    Cl = 40
    WP = 30
    Fel = 25

class Prospector(Warhammer):
    M = 4
    WS = 40
    BS = 40
    S = 4
    T = 4
    W = 8
    I = 30
    A = 2
    Dex = 25
    Ld = 30
    Int = 30
    Cl = 40
    WP = 25
    Fel = 30

class Roadwarden:
    class Roadwarden(Warhammer):
        M = 4
        WS = 41
        BS = 35
        S = 3
        T = 3
        W = 7
        I = 30
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class Roadwarden_Sergeant(Warhammer):
        M = 4
        WS = 51
        BS = 45
        S = 4
        T = 4
        W = 9
        I = 40
        A = 2
        Dex = 29
        Ld = 39
        Int = 29
        Cl = 39
        WP = 29
        Fel = 29

class Scholar(Warhammer):
    M = 4
    WS = 40
    BS = 35
    S = 3
    T = 3
    W = 8
    I = 65
    A = 1
    Dex = 40
    Ld = 25
    Int = 60
    Cl = 40
    WP = 60
    Fel = 40

class Servant(Warhammer):
    M = 4
    WS = 31
    BS = 25
    S = 3
    T = 3
    W = 6
    I = 30
    A = 1
    Dex = 29
    Ld = 29
    Int = 29
    Cl = 29
    WP = 29
    Fel = 29

class Smuggler(Warhammer):
    M = 4
    WS = 40
    BS = 40
    S = 3
    T = 3
    W = 8
    I = 40
    A = 1
    Dex = 30
    Ld = 30
    Int = 30
    Cl = 30
    WP = 30
    Fel = 30

class Spellcaster(Warhammer):
    M = 4
    WS = 23
    BS = 25
    S = 3
    T = 3
    W = 5
    I = 30
    A = 1
    Dex = 29
    Ld = 29
    Int = 39
    Cl = 29
    WP = 29
    Fel = 29

class Thief(Warhammer):
    M = 4
    WS = 43
    BS = 35
    S = 3
    T = 3
    W = 7
    I = 30
    A = 1
    Dex = 39
    Ld = 29
    Int = 29
    Cl = 29
    WP = 29
    Fel = 39

class Thugs:
    class Thug(Warhammer):
        M = 4
        WS = 31
        BS = 25
        S = 3
        T = 4
        W = 7
        I = 30
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class Teamsters_or_Stevedores(Warhammer):
        M = 4
        WS = 33
        BS = 25
        S = 3
        T = 4
        W = 8
        I = 30
        A = 1
        Dex = 34
        Ld = 28
        Int = 33
        Cl = 30
        WP = 32
        Fel = 29

class TollKeeper:
    class TollKeeper(Warhammer):
        M = 4
        WS = 31
        BS = 25
        S = 3
        T = 3
        W = 6
        I = 30
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class LockKeeper(Warhammer):
        M = 4
        WS = 40
        BS = 40
        S = 3
        T = 3
        W = 8
        I = 40
        A = 1
        Dex = 30
        Ld = 30
        Int = 30
        Cl = 30
        WP = 30
        Fel = 30

class Townsperson:
    class Townsperson_Poor(Warhammer):
        M = 4
        WS = 23
        BS = 25
        S = 3
        T = 3
        W = 5
        I = 30
        A = 1
        Dex = 30
        Ld = 29
        Int = 28
        Cl = 32
        WP = 30
        Fel = 30

    class Townsperson_Wealthy(Warhammer):
        M = 4
        WS = 23
        BS = 25
        S = 3
        T = 3
        W = 5
        I = 30
        A = 1
        Dex = 30
        Ld = 34
        Int = 36
        Cl = 32
        WP = 30
        Fel = 39

class Tutor(Warhammer):
    M = 3
    WS = 36
    BS = 32
    S = 3
    T = 3
    W = 6
    I = 58
    A = 1
    Dex = 34
    Ld = 30
    Int = 68
    Cl = 36
    WP = 50
    Fel = 29

class Watchman:
    class Watchman(Warhammer):
        M = 4
        WS = 41
        BS = 25
        S = 4
        T = 3
        W = 7
        I = 40
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class Watch_Sergeant(Warhammer):
        M = 4
        WS = 51
        BS = 35
        S = 4
        T = 3
        W = 8
        I = 40
        A = 2
        Dex = 29
        Ld = 39
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

class Yokel:
    class Profile_1(Warhammer):
        M = 4
        WS = 31
        BS = 25
        S = 4
        T = 4
        W = 6
        I = 30
        A = 1
        Dex = 29
        Ld = 29
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class Profile_2(Warhammer):
        M = 4
        WS = 33
        BS = 25
        S = 3
        T = 3
        W = 7
        I = 30
        A = 1
        Dex = 30
        Ld = 30
        Int = 32
        Cl = 28
        WP = 26
        Fel = 30

class Soldiers:
    class Generic_Soldier(Warhammer):
        M = 4
        WS = 43
        BS = 35
        S = 3
        T = 3
        W = 8
        I = 40
        A = 1
        Dex = 29
        Ld = 39
        Int = 29
        Cl = 29
        WP = 29
        Fel = 29

    class The_Imperial_Guard:
        class Cavalry_Officer(Warhammer):
            M = 4
            WS = 65
            BS = 50
            S = 5
            T = 5
            W = 13
            I = 50
            A = 3
            Dex = 49
            Ld = 69
            Int = 39
            Cl = 69
            WP = 40
            Fel = 50

        class Cavalryman(Warhammer):
            M = 4
            WS = 50
            BS = 38
            S = 4
            T = 4
            W = 11
            I = 50
            A = 3
            Dex = 39
            Ld = 39
            Int = 29
            Cl = 40
            WP = 29
            Fel = 30

        class Officer(Warhammer):
            M = 4
            WS = 60
            BS = 45
            S = 5
            T = 5
            W = 13
            I = 60
            A = 3
            Dex = 49
            Ld = 69
            Int = 40
            Cl = 60
            WP = 40
            Fel = 50

        class Soldier(Warhammer):
            M = 4
            WS = 50
            BS = 40
            S = 4
            T = 4
            W = 11
            I = 50
            A = 2
            Dex = 39
            Ld = 39
            Int = 29
            Cl = 40
            WP = 29
            Fel = 30

        class Mercenary_Captain(Warhammer):
            M = 4
            WS = 55
            BS = 45
            S = 4
            T = 4
            W = 11
            I = 55
            A = 2
            Dex = 39
            Ld = 55
            Int = 39
            Cl = 50
            WP = 35
            Fel = 45

        class Mercenary_Soldier(Warhammer):
            M = 4
            WS = 45
            BS = 35
            S = 3
            T = 4
            W = 8
            I = 45
            A = 2
            Dex = 29
            Ld = 39
            Int = 29
            Cl = 35
            WP = 25
            Fel = 30

        class Templar(Warhammer):
            M = 4
            WS = 70
            BS = 55
            S = 5
            T = 5
            W = 15
            I = 70
            A = 3
            Dex = 59
            Ld = 59
            Int = 50
            Cl = 65
            WP = 60
            Fel = 59

        class Halfling_Infantry(Warhammer):
            M = 3
            WS = 38
            BS = 45
            S = 3
            T = 3
            W = 8
            I = 60
            A = 2
            Dex = 49
            Ld = 30
            Int = 29
            Cl = 34
            WP = 55
            Fel = 53

    class Standing_Armies_In_The_Empire:
        class Sergeant(Warhammer):
            M = 4
            WS = 50
            BS = 30
            S = 4
            T = 4
            W = 11
            I = 50
            A = 2
            Dex = 39
            Ld = 55
            Int = 40
            Cl = 50
            WP = 35
            Fel = 40

        class Soldier(Warhammer):
            M = 4
            WS = 45
            BS = 30
            S = 3
            T = 3
            W = 7
            I = 40
            A = 1
            Dex = 29
            Ld = 39
            Int = 29
            Cl = 29
            WP = 25
            Fel = 30

        class Pikeman(Warhammer):
            M = 4
            WS = 45
            BS = 30
            S = 3
            T = 3
            W = 7
            I = 40
            A = 1
            Dex = 29
            Ld = 40
            Int = 29
            Cl = 30
            WP = 26
            Fel = 29

        class Mercenary_Crossbowman(Warhammer):
            M = 4
            WS = 40
            BS = 50
            S = 3
            T = 4
            W = 9
            I = 45
            A = 2
            Dex = 39
            Ld = 39
            Int = 29
            Cl = 35
            WP = 30
            Fel = 35

        class Gunnery_Captain(Warhammer):
            M = 4
            WS = 54
            BS = 30
            S = 3
            T = 3
            W = 9
            I = 45
            A = 1
            Dex = 29
            Ld = 50
            Int = 29
            Cl = 30
            WP = 26
            Fel = 32

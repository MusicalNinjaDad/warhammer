# ruff: noqa: RUF100, D100, D101, D106, E741, N801, N999
from ttrpg_dice import d  # noqa: F401

from .statblocks import Warhammer


class Amoeba(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 3
    T = 5
    W = 11
    I = 30
    A = 3
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Amphisbaena(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 4
    T = 3
    W = 11
    I = 60
    A = 1
    Dex = 0
    Ld = 14
    Int = 5
    Cl = 43
    WP = 43
    Fel = 0

class Basilisk(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 5
    T = 4
    W = 11
    I = 30
    A = 3
    Dex = 0
    Ld = 14
    Int = 14
    Cl = 14
    WP = 14
    Fel = 0

class Bat(Warhammer):
    M = 0
    WS = 59
    BS = 0
    S = 0
    T = 1
    W = 1
    I = 30
    A = 1
    Dex = 0
    Ld = 14
    Int = 5
    Cl = 29
    WP = 29
    Fel = 0

class Bear(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 4
    T = 4
    W = 11
    I = 30
    A = 2
    Dex = 0
    Ld = 24
    Int = 10
    Cl = 24
    WP = 24
    Fel = 0

class Beast_Of_Nurgle(Warhammer):
    M = 3
    WS = 30
    BS = 0
    S = 3
    T = 5
    W = 15
    I = 30
    A = d.from_str("d6")
    Dex = 6
    Ld = 24
    Int = 10
    Cl = 89
    WP = 98
    Fel = 0

class Black_Orc(Warhammer):
    M = 4
    WS = 33
    BS = 25
    S = 4
    T = 4
    W = 7
    I = 30
    A = 1
    Dex = 18
    Ld = 29
    Int = 18
    Cl = 29
    WP = 29
    Fel = 14

class Bloodletter(Warhammer):
    M = 4
    WS = 50
    BS = 42
    S = 4
    T = 3
    W = 5
    I = 60
    A = 2
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 1

class Bloodsedge(Warhammer):
    M = 0
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 5
    I = 60
    A = 1
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 20
    Fel = 0

class Bloodthirster(Warhammer):
    M = 6
    WS = 90
    BS = 93
    S = 7
    T = 7
    W = 39
    I = 100
    A = 10
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 1

class Boar(Warhammer):
    M = 7
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 11
    I = 30
    A = 1
    Dex = 0
    Ld = 10
    Int = 14
    Cl = 14
    WP = 14
    Fel = 0

class Bog_Octopus(Warhammer):
    M = 3
    WS = 33
    BS = 0
    S = 8
    T = 8
    W = 17
    I = 60
    A = 8
    Dex = 0
    Ld = 66
    Int = 2
    Cl = 66
    WP = 66
    Fel = 0

class Carnivorous_Snapper(Warhammer):
    M = 7
    WS = 33
    BS = 0
    S = 4
    T = 5
    W = 17
    I = 10
    A = 2
    Dex = 0
    Ld = 10
    Int = 5
    Cl = 66
    WP = 89
    Fel = 0

class Carrion(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 11
    I = 40
    A = 3
    Dex = 0
    Ld = 29
    Int = 10
    Cl = 29
    WP = 29
    Fel = 0

class Cat(Warhammer):
    M = 8
    WS = 41
    BS = 0
    S = 1
    T = 1
    W = 2
    I = 30
    A = 3
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 43
    WP = 43
    Fel = 0

class Chameleoleech(Warhammer):
    M = 3
    WS = 33
    BS = 0
    S = 2
    T = 2
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 14
    Int = 2
    Cl = 14
    WP = 14
    Fel = 0

class Chaos_Beastman(Warhammer):
    M = 4
    WS = 41
    BS = 25
    S = 3
    T = 4
    W = 11
    I = 30
    A = 1
    Dex = 30
    Ld = 29
    Int = 24
    Cl = 29
    WP = 24
    Fel = 10

class Chimera(Warhammer):
    M = 5
    WS = 41
    BS = 0
    S = 6
    T = 6
    W = 41
    I = 30
    A = 6
    Dex = 0
    Ld = 89
    Int = 14
    Cl = 89
    WP = 89
    Fel = 0

class Cold_One(Warhammer):
    M = 8
    WS = 33
    BS = 0
    S = 4
    T = 4
    W = 11
    I = 10
    A = 2
    Dex = 0
    Ld = 6
    Int = 14
    Cl = 66
    WP = 66
    Fel = 0

class Cold_One_Warhound(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 5
    I = 20
    A = 2
    Dex = 0
    Ld = 6
    Int = 14
    Cl = 66
    WP = 66
    Fel = 0

class Daemonette(Warhammer):
    M = 4
    WS = 57
    BS = 42
    S = 4
    T = 3
    W = 5
    I = 60
    A = 3
    Dex = 10
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 89

class Daemonic_Steed(Warhammer):
    M = 8
    WS = 33
    BS = 0
    S = 4
    T = 3
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 10
    WP = 10
    Fel = 0

class Discs(Warhammer):
    M = 12
    WS = 35
    BS = 0
    S = 3
    T = 3
    W = 11
    I = 30
    A = 1
    Dex = 0
    Ld = 90
    Int = 90
    Cl = 90
    WP = 90
    Fel = 0

class Dog(Warhammer):
    M = 6
    WS = 41
    BS = 0
    S = 2
    T = 2
    W = 2
    I = 30
    A = 1
    Dex = 0
    Ld = 43
    Int = 14
    Cl = 43
    WP = 43
    Fel = 0

class Doppelganger(Warhammer):
    M = 4
    WS = 41
    BS = 33
    S = 4
    T = 3
    W = 11
    I = 30
    A = 2
    Dex = 33
    Ld = 43
    Int = 29
    Cl = 29
    WP = 29
    Fel = 10

class Dragon(Warhammer):
    M = 6
    WS = 59
    BS = 0
    S = 7
    T = 7
    W = 59
    I = 30
    A = 6
    Dex = 0
    Ld = 89
    Int = 41
    Cl = 89
    WP = 89
    Fel = 24

class Dragon_Turtle(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 4
    T = 4
    W = 17
    I = 30
    A = 2
    Dex = 0
    Ld = 29
    Int = 10
    Cl = 29
    WP = 29
    Fel = 0

class Dryad(Warhammer):
    M = 5
    WS = 39
    BS = 29
    S = 4
    T = 4
    W = 58
    I = 39
    A = 2
    Dex = 36
    Ld = 75
    Int = 45
    Cl = 89
    WP = 89
    Fel = 30

class Dwarf(Warhammer):
    M = 3
    WS = 41
    BS = 25
    S = 3
    T = 4
    W = 7
    I = 20
    A = 1
    Dex = 24
    Ld = 66
    Int = 29
    Cl = 66
    WP = 66
    Fel = 24

class Eagle(Warhammer):
    M = 2
    WS = 67
    BS = 0
    S = 5
    T = 4
    W = 17
    I = 50
    A = 2
    Dex = 0
    Ld = 43
    Int = 29
    Cl = 43
    WP = 43
    Fel = 0

class Elementals(Warhammer):
    M = 9
    WS = 90
    BS = 90
    S = 9
    T = 9
    W = 90
    I = 90
    A = 9
    Dex = 90
    Ld = 90
    Int = 90
    Cl = 90
    WP = 90
    Fel = 0

class Elf(Warhammer):
    M = 4
    WS = 41
    BS = 34
    S = 3
    T = 3
    W = 7
    I = 60
    A = 1
    Dex = 43
    Ld = 43
    Int = 66
    Cl = 66
    WP = 43
    Fel = 43

class Fen_Worm(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 6
    T = 4
    W = 17
    I = 30
    A = 4
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 10
    WP = 10
    Fel = 0

class Fiend_Of_Slaanesh(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 5
    I = 30
    A = 3
    Dex = 0
    Ld = 43
    Int = 14
    Cl = 43
    WP = 43
    Fel = 0

class Fimir(Warhammer):
    M = 4
    WS = 33
    BS = 9
    S = 4
    T = 3
    W = 11
    I = 20
    A = 1
    Dex = 18
    Ld = 18
    Int = 14
    Cl = 18
    WP = 18
    Fel = 11

class Flamer(Warhammer):
    M = 9
    WS = 35
    BS = 45
    S = 5
    T = 4
    W = 11
    I = 40
    A = 2
    Dex = 0
    Ld = 90
    Int = 0
    Cl = 90
    WP = 90
    Fel = 0

class Fleshhound(Warhammer):
    M = 10
    WS = 49
    BS = 0
    S = 5
    T = 4
    W = 11
    I = 60
    A = 1
    Dex = 0
    Ld = 10
    Int = 14
    Cl = 89
    WP = 89
    Fel = 0

class Fox(Warhammer):
    M = 5
    WS = 33
    BS = 0
    S = 1
    T = 2
    W = 2
    I = 40
    A = 1
    Dex = 0
    Ld = 14
    Int = 14
    Cl = 14
    WP = 14
    Fel = 0

class Frog(Warhammer):
    M = 3
    WS = 0
    BS = 0
    S = 1
    T = 1
    W = 1
    I = 30
    A = 0
    Dex = 0
    Ld = 6
    Int = 6
    Cl = 6
    WP = 6
    Fel = 0

class Ghost(Warhammer):
    M = 4
    WS = 25
    BS = 0
    S = 0
    T = 3
    W = 17
    I = 30
    A = 1
    Dex = 0
    Ld = 18
    Int = 18
    Cl = 18
    WP = 18
    Fel = 29

class Ghoul(Warhammer):
    M = 4
    WS = 25
    BS = 0
    S = 3
    T = 4
    W = 5
    I = 30
    A = 2
    Dex = 43
    Ld = 6
    Int = 18
    Cl = 43
    WP = 43
    Fel = 0

class Giant(Warhammer):
    M = 6
    WS = 33
    BS = 25
    S = 7
    T = 7
    W = 36
    I = 20
    A = 5
    Dex = 14
    Ld = 24
    Int = 14
    Cl = 24
    WP = 24
    Fel = 14

class Giant_Bat(Warhammer):
    M = 1
    WS = 33
    BS = 0
    S = 2
    T = 2
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 10
    Int = 14
    Cl = 24
    WP = 24
    Fel = 0

class Giant_Beetle(Warhammer):
    M = 5
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 11
    I = 10
    A = 2
    Dex = 0
    Ld = 43
    Int = 2
    Cl = 24
    WP = 6
    Fel = 0

class Giant_Leech(Warhammer):
    M = 3
    WS = 33
    BS = 0
    S = 2
    T = 2
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 14
    Int = 1
    Cl = 14
    WP = 14
    Fel = 0

class Giant_Scorpion(Warhammer):
    M = 5
    WS = 33
    BS = 0
    S = 5
    T = 4
    W = 17
    I = 10
    A = 3
    Dex = 0
    Ld = 43
    Int = 2
    Cl = 24
    WP = 6
    Fel = 0

class Giant_Spider(Warhammer):
    M = 5
    WS = 33
    BS = 0
    S = 5
    T = 4
    W = 17
    I = 10
    A = 2
    Dex = 0
    Ld = 43
    Int = 2
    Cl = 24
    WP = 6
    Fel = 0

class Gnome(Warhammer):
    M = 4
    WS = 41
    BS = 25
    S = 3
    T = 2
    W = 7
    I = 30
    A = 1
    Dex = 29
    Ld = 43
    Int = 29
    Cl = 29
    WP = 43
    Fel = 29

class Goblin(Warhammer):
    M = 4
    WS = 25
    BS = 25
    S = 2
    T = 2
    W = 5
    I = 40
    A = 1
    Dex = 24
    Ld = 18
    Int = 18
    Cl = 18
    WP = 18
    Fel = 18

class Goldworm(Warhammer):
    M = 1
    WS = 0
    BS = 0
    S = 0
    T = 0
    W = 1
    I = 0
    A = 0
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Great_Unclean_One(Warhammer):
    M = 6
    WS = 90
    BS = 93
    S = 7
    T = 7
    W = 39
    I = 100
    A = 10
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 1

class Greater_Daemon(Warhammer):
    M = 6
    WS = 90
    BS = 93
    S = 7
    T = 7
    W = 59
    I = 100
    A = 10
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 89

class Griffon(Warhammer):
    M = 6
    WS = 50
    BS = 0
    S = 5
    T = 5
    W = 35
    I = 80
    A = 4
    Dex = 0
    Ld = 66
    Int = 14
    Cl = 66
    WP = 66
    Fel = 0

class Guardian_Spirit(Warhammer):
    M = 4
    WS = 0
    BS = 0
    S = 0
    T = 3
    W = 17
    I = 40
    A = 0
    Dex = 0
    Ld = 40
    Int = 18
    Cl = 18
    WP = 18
    Fel = 0

class Halfling(Warhammer):
    M = 3
    WS = 25
    BS = 34
    S = 2
    T = 2
    W = 7
    I = 50
    A = 1
    Dex = 43
    Ld = 24
    Int = 29
    Cl = 24
    WP = 43
    Fel = 43

class Harpy(Warhammer):
    M = 4
    WS = 41
    BS = 25
    S = 4
    T = 4
    W = 11
    I = 20
    A = 1
    Dex = 33
    Ld = 35
    Int = 14
    Cl = 43
    WP = 66
    Fel = 5

class Hawk(Warhammer):
    M = 1
    WS = 40
    BS = 0
    S = 1
    T = 1
    W = 3
    I = 50
    A = 1
    Dex = 0
    Ld = 6
    Int = 6
    Cl = 6
    WP = 6
    Fel = 0

class Herd_Animal(Warhammer):
    M = 7
    WS = 33
    BS = 0
    S = 3
    T = 3
    W = 11
    I = 30
    A = 1
    Dex = 0
    Ld = 6
    Int = 6
    Cl = 6
    WP = 6
    Fel = 0

class Hippogriff(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 4
    T = 5
    W = 23
    I = 80
    A = 4
    Dex = 0
    Ld = 43
    Int = 14
    Cl = 43
    WP = 43
    Fel = 0

class Hobgoblin(Warhammer):
    M = 4
    WS = 33
    BS = 14
    S = 3
    T = 4
    W = 7
    I = 30
    A = 1
    Dex = 29
    Ld = 29
    Int = 24
    Cl = 24
    WP = 24
    Fel = 18

class Horrors(Warhammer):
    M = 4
    WS = 35
    BS = 25
    S = 3
    T = 3
    W = 5
    I = 70
    A = 1
    Dex = 90
    Ld = 20
    Int = 20
    Cl = 20
    WP = 20
    Fel = 1

class Horse(Warhammer):
    M = 8
    WS = 33
    BS = 0
    S = 2
    T = 3
    W = 5
    I = 30
    A = 0
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 10
    WP = 10
    Fel = 0

class Human(Warhammer):
    M = 4
    WS = 33
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
    WP = 29
    Fel = 29

class Hydra(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 4
    T = 6
    W = 41
    I = 30
    A = 8
    Dex = 0
    Ld = 24
    Int = 14
    Cl = 24
    WP = 24
    Fel = 0

class Jabberwock(Warhammer):
    M = 6
    WS = 79
    BS = 0
    S = 5
    T = 6
    W = 47
    I = 10
    A = 4
    Dex = 10
    Ld = 89
    Int = 18
    Cl = 89
    WP = 89
    Fel = 0

class Juggernaut(Warhammer):
    M = 7
    WS = 33
    BS = 0
    S = 5
    T = 5
    W = 17
    I = 20
    A = 2
    Dex = 0
    Ld = 89
    Int = 6
    Cl = 89
    WP = 89
    Fel = 0

class Keeper_Of_Secrets(Warhammer):
    M = 6
    WS = 90
    BS = 93
    S = 7
    T = 7
    W = 39
    I = 100
    A = 6
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 18

class Lashworm(Warhammer):
    M = 0
    WS = 33
    BS = 0
    S = 1
    T = 3
    W = 5
    I = 0
    A = 1
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Lesser_Daemon(Warhammer):
    M = 4
    WS = 50
    BS = 42
    S = 4
    T = 3
    W = 5
    I = 60
    A = 2
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 14

class Liche(Warhammer):
    M = 4
    WS = 41
    BS = 25
    S = 4
    T = 4
    W = 23
    I = 60
    A = 4
    Dex = 43
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 0

class Lizardman(Warhammer):
    M = 4
    WS = 33
    BS = 25
    S = 3
    T = 4
    W = 12
    I = 30
    A = 1
    Dex = 18
    Ld = 89
    Int = 18
    Cl = 89
    WP = 89
    Fel = 10

class Lord_Of_Change(Warhammer):
    M = 6
    WS = 90
    BS = 95
    S = 7
    T = 7
    W = 40
    I = 100
    A = 10
    Dex = 90
    Ld = 90
    Int = 90
    Cl = 90
    WP = 90
    Fel = 30

class Manticore(Warhammer):
    M = 5
    WS = 59
    BS = 34
    S = 6
    T = 6
    W = 41
    I = 40
    A = 4
    Dex = 0
    Ld = 43
    Int = 24
    Cl = 43
    WP = 43
    Fel = 0

class Marshlight(Warhammer):
    M = 4
    WS = 0
    BS = 0
    S = 0
    T = 0
    W = 0
    I = 0
    A = 0
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Minotaur(Warhammer):
    M = 6
    WS = 41
    BS = 25
    S = 4
    T = 4
    W = 17
    I = 30
    A = 2
    Dex = 18
    Ld = 66
    Int = 18
    Cl = 29
    WP = 24
    Fel = 10

class Mount_Of_Slaanesh(Warhammer):
    M = 12
    WS = 33
    BS = 0
    S = 4
    T = 5
    W = 10
    I = 60
    A = 0
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Mummy(Warhammer):
    M = 3
    WS = 33
    BS = 0
    S = 4
    T = 5
    W = 23
    I = 30
    A = 2
    Dex = 24
    Ld = 89
    Int = 43
    Cl = 43
    WP = 89
    Fel = 0

class Mutant(Warhammer):
    M = 4
    WS = 33
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
    Fel = 16

class Nurglings(Warhammer):
    M = 4
    WS = 30
    BS = 30
    S = 3
    T = 3
    W = 15
    I = 40
    A = 3
    Dex = 70
    Ld = 30
    Int = 25
    Cl = 30
    WP = 30
    Fel = 45

class Ogre(Warhammer):
    M = 6
    WS = 33
    BS = 17
    S = 4
    T = 5
    W = 17
    I = 30
    A = 2
    Dex = 18
    Ld = 18
    Int = 14
    Cl = 18
    WP = 29
    Fel = 10

class Orc(Warhammer):
    M = 4
    WS = 33
    BS = 25
    S = 3
    T = 4
    W = 7
    I = 20
    A = 1
    Dex = 29
    Ld = 29
    Int = 18
    Cl = 29
    WP = 29
    Fel = 18

class Otter(Warhammer):
    M = 6
    WS = 33
    BS = 0
    S = 1
    T = 2
    W = 1
    I = 40
    A = 1
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 10
    WP = 10
    Fel = 0

class Owl(Warhammer):
    M = 2
    WS = 59
    BS = 0
    S = 1
    T = 1
    W = 2
    I = 50
    A = 2
    Dex = 0
    Ld = 14
    Int = 14
    Cl = 14
    WP = 14
    Fel = 0

class Pegasus(Warhammer):
    M = 8
    WS = 33
    BS = 0
    S = 4
    T = 3
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 10
    Int = 14
    Cl = 10
    WP = 10
    Fel = 0

class Plaguebearer(Warhammer):
    M = 4
    WS = 50
    BS = 42
    S = 4
    T = 3
    W = 5
    I = 60
    A = 2
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 1

class Rabbit(Warhammer):
    M = 7
    WS = 25
    BS = 0
    S = 0
    T = 1
    W = 1
    I = 30
    A = 1
    Dex = 0
    Ld = 2
    Int = 2
    Cl = 2
    WP = 2
    Fel = 0

class Ram(Warhammer):
    M = 7
    WS = 25
    BS = 0
    S = 2
    T = 3
    W = 6
    I = 30
    A = 1
    Dex = 0
    Ld = 14
    Int = 10
    Cl = 10
    WP = 10
    Fel = 0

class Rat(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 0
    T = 1
    W = 1
    I = 30
    A = 1
    Dex = 0
    Ld = 14
    Int = 10
    Cl = 14
    WP = 14
    Fel = 0

class Raven(Warhammer):
    M = 2
    WS = 33
    BS = 0
    S = 1
    T = 1
    W = 2
    I = 30
    A = 2
    Dex = 0
    Ld = 24
    Int = 2
    Cl = 24
    WP = 24
    Fel = 0

class Razorbill(Warhammer):
    M = 2
    WS = 33
    BS = 0
    S = 1
    T = 2
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 14
    Int = 10
    Cl = 14
    WP = 14
    Fel = 0

class Sand_Clam(Warhammer):
    M = 0
    WS = 33
    BS = 0
    S = 0
    T = 3
    W = 11
    I = 0
    A = 1
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Skaven(Warhammer):
    M = 5
    WS = 33
    BS = 25
    S = 3
    T = 3
    W = 7
    I = 40
    A = 1
    Dex = 24
    Ld = 24
    Int = 24
    Cl = 18
    WP = 29
    Fel = 14

class Skeleton(Warhammer):
    M = 4
    WS = 25
    BS = 17
    S = 3
    T = 3
    W = 5
    I = 20
    A = 1
    Dex = 18
    Ld = 18
    Int = 18
    Cl = 18
    WP = 18
    Fel = 0

class Snake(Warhammer):
    M = 3
    WS = 33
    BS = 0
    S = 1
    T = 2
    W = 3
    I = 30
    A = 1
    Dex = 0
    Ld = 24
    Int = 10
    Cl = 24
    WP = 24
    Fel = 0

class Snotling(Warhammer):
    M = 4
    WS = 17
    BS = 17
    S = 1
    T = 1
    W = 3
    I = 30
    A = 1
    Dex = 14
    Ld = 14
    Int = 14
    Cl = 14
    WP = 14
    Fel = 14

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

class Spectre(Warhammer):
    M = 4
    WS = 41
    BS = 0
    S = 0
    T = 4
    W = 23
    I = 40
    A = 4
    Dex = 0
    Ld = 18
    Int = 18
    Cl = 18
    WP = 18
    Fel = 29

class Squirrel(Warhammer):
    M = 6
    WS = 25
    BS = 0
    S = 0
    T = 1
    W = 1
    I = 40
    A = 1
    Dex = 0
    Ld = 2
    Int = 2
    Cl = 2
    WP = 2
    Fel = 0

class Stoat(Warhammer):
    M = 6
    WS = 41
    BS = 0
    S = 1
    T = 1
    W = 2
    I = 40
    A = 1
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 10
    WP = 10
    Fel = 0

class Sunworm(Warhammer):
    M = 1
    WS = 33
    BS = 0
    S = 4
    T = 4
    W = 11
    I = 60
    A = 0
    Dex = 0
    Ld = 0
    Int = 0
    Cl = 0
    WP = 0
    Fel = 0

class Swarm(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 1
    T = 1
    W = 10
    I = 10
    A = 10
    Dex = 0
    Ld = 89
    Int = 5
    Cl = 89
    WP = 89
    Fel = 0

class Treeman(Warhammer):
    M = 6
    WS = 79
    BS = 25
    S = 6
    T = 7
    W = 36
    I = 20
    A = 4
    Dex = 24
    Ld = 89
    Int = 66
    Cl = 89
    WP = 89
    Fel = 24

class Troglodyte(Warhammer):
    M = 4
    WS = 33
    BS = 25
    S = 4
    T = 4
    W = 10
    I = 10
    A = 2
    Dex = 14
    Ld = 89
    Int = 14
    Cl = 89
    WP = 89
    Fel = 10

class Troll(Warhammer):
    M = 6
    WS = 33
    BS = 9
    S = 5
    T = 4
    W = 18
    I = 10
    A = 3
    Dex = 14
    Ld = 14
    Int = 14
    Cl = 24
    WP = 24
    Fel = 6

class Unicorn(Warhammer):
    M = 8
    WS = 50
    BS = 0
    S = 3
    T = 3
    W = 17
    I = 40
    A = 2
    Dex = 0
    Ld = 89
    Int = 18
    Cl = 89
    WP = 89
    Fel = 0

class Vampire(Warhammer):
    M = 0
    WS = 30
    BS = 30
    S = 3
    T = 3
    W = 15
    I = 30
    A = 3
    Dex = 20
    Ld = 20
    Int = 20
    Cl = 20
    WP = 20
    Fel = 20

class Viydagg(Warhammer):
    M = 6
    WS = 90
    BS = 93
    S = 10
    T = 10
    W = 67
    I = 100
    A = 10
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 0

class War_Dog(Warhammer):
    M = 6
    WS = 41
    BS = 0
    S = 3
    T = 3
    W = 7
    I = 30
    A = 1
    Dex = 0
    Ld = 43
    Int = 14
    Cl = 43
    WP = 43
    Fel = 0

class Warrior_Of_Chaos(Warhammer):
    M = 4
    WS = 59
    BS = 49
    S = 4
    T = 3
    W = 10
    I = 60
    A = 2
    Dex = 89
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 18

class Wight(Warhammer):
    M = 4
    WS = 33
    BS = 0
    S = 0
    T = 4
    W = 17
    I = 30
    A = 1
    Dex = 18
    Ld = 18
    Int = 18
    Cl = 18
    WP = 18
    Fel = 0

class Wild_Cat(Warhammer):
    M = 8
    WS = 41
    BS = 0
    S = 4
    T = 3
    W = 5
    I = 30
    A = 3
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 43
    WP = 43
    Fel = 0

class Wolf(Warhammer):
    M = 9
    WS = 33
    BS = 0
    S = 2
    T = 2
    W = 5
    I = 30
    A = 1
    Dex = 0
    Ld = 10
    Int = 10
    Cl = 14
    WP = 14
    Fel = 0

class Wraith(Warhammer):
    M = 4
    WS = 17
    BS = 0
    S = 3
    T = 4
    W = 11
    I = 30
    A = 2
    Dex = 0
    Ld = 18
    Int = 18
    Cl = 18
    WP = 18
    Fel = 0

class Wyvern(Warhammer):
    M = 4
    WS = 25
    BS = 0
    S = 5
    T = 6
    W = 17
    I = 10
    A = 3
    Dex = 0
    Ld = 14
    Int = 14
    Cl = 14
    WP = 14
    Fel = 0

class Zoat(Warhammer):
    M = 7
    WS = 59
    BS = 25
    S = 5
    T = 5
    W = 18
    I = 50
    A = 2
    Dex = 43
    Ld = 89
    Int = 89
    Cl = 89
    WP = 89
    Fel = 43

class Zombie(Warhammer):
    M = 4
    WS = 25
    BS = 0
    S = 3
    T = 3
    W = 5
    I = 10
    A = 1
    Dex = 10
    Ld = 18
    Int = 14
    Cl = 14
    WP = 14
    Fel = 0

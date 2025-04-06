from wfrp import beasts, careers


def test_addcareers():
    albert = beasts.Human()
    albert.careers |= {"Alchemist Apprentice": careers.Alchemists_Apprentice, "Level 1": careers.Alchemist.Level_1}
    assert albert.careers == {
        "Alchemist Apprentice": careers.Alchemists_Apprentice,
        "Level 1": careers.Alchemist.Level_1,
    }
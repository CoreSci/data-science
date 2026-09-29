"""Lesson 2 - Silly song machine (La machine à chansons rigolotes).

We write the chorus ONCE, inside a function, then sing it as many times as we
want. Big idea: a function is a recipe with a name that we can reuse.
The song words are original. Messages to the child are in French.
"""


def chorus():
    """The chorus: written once, sung many times."""
    print("  Tchou-tchou, boum-boum,")
    print("  la machine chante,")
    print("  tchou-tchou, boum-boum,")
    print("  la chanson est géante !")
    print()


def verse(animal, sound):
    """One verse, with the animal and sound chosen by the child."""
    print("Dans ma machine, il y a " + animal + ",")
    print("qui fait " + sound + " ! " + sound + " ! toute la journée.")
    print()


def main():
    print("Bienvenue dans la machine à chansons !")
    print("Choisis trois animaux et le bruit qu'ils font.")
    print()
    animals = []
    for number in range(1, 4):
        animal = input("Animal numéro " + str(number) + " (ex. : une vache) : ").strip() or "un chat"
        sound = input("Quel bruit fait " + animal + " ? ").strip() or "miaou"
        animals.append((animal, sound))

    print()
    print("🎵 Voici ta chanson ! 🎵")
    print()
    chorus()
    for animal, sound in animals:
        verse(animal, sound)
        chorus()
    print("Fin de la chanson ! Bravo !")


if __name__ == "__main__":
    main()

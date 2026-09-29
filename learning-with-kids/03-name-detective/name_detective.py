"""Lesson 3 - Name detective (Le détective des prénoms).

The computer investigates a name: how many letters, how many vowels, which
letter appears most, and what the name looks like backwards.
Big idea: a loop looks at each letter, one after the other.
Messages to the child are in French.
"""

VOWELS = "aeiouyàâäéèêëîïôöùûü"


def count_letters(word):
    """How many letters (spaces and dashes don't count)."""
    total = 0
    for letter in word:
        if letter.isalpha():
            total = total + 1
    return total


def count_vowels(word):
    """How many vowels, including accented ones (é, è, à...)."""
    total = 0
    for letter in word.lower():
        if letter in VOWELS:
            total = total + 1
    return total


def favourite_letter(word):
    """The letter that appears the most (the first one if there's a tie)."""
    counts = {}
    for letter in word.lower():
        if letter.isalpha():
            counts[letter] = counts.get(letter, 0) + 1
    best = ""
    for letter in counts:
        if best == "" or counts[letter] > counts[best]:
            best = letter
    return best, counts.get(best, 0)


def main():
    print("🔍 Je suis le détective des prénoms !")
    while True:
        name = input("Donne-moi un prénom (ou tape « fini ») : ").strip()
        if name.lower() == "fini":
            print("Enquête terminée. Au revoir, détective !")
            break
        if count_letters(name) == 0:
            print("Hmm, je ne vois pas de lettres. Essaie encore !")
            continue
        letter, times = favourite_letter(name)
        print("  Lettres :", count_letters(name))
        print("  Voyelles :", count_vowels(name))
        print("  Lettre préférée :", letter.upper(), "(" + str(times) + " fois)")
        print("  À l'envers :", name[::-1])
        print()


if __name__ == "__main__":
    main()

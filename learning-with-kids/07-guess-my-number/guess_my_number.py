"""Lesson 7 - Guess my number (Devine mon nombre).

The computer picks a secret number between 1 and 20. You guess; it answers
"trop haut" (too high) or "trop bas" (too low) until you find it.
Big idea: compare, repeat, and a little bit of chance (random).
Messages to the child are in French.
"""
import random

SMALLEST = 1
BIGGEST = 20


def hint(guess, secret):
    """What the computer says after a guess."""
    if guess < secret:
        return "Trop bas ! ⬆️"
    if guess > secret:
        return "Trop haut ! ⬇️"
    return "Bravo, tu as trouvé ! 🎉"


def play(secret, ask=input):
    """One game. Returns how many guesses it took."""
    tries = 0
    while True:
        answer = ask("Ton nombre (" + str(SMALLEST) + " à " + str(BIGGEST) + ") : ").strip()
        if not answer.isdigit():
            print("Écris un nombre avec des chiffres, par exemple : 7")
            continue
        guess = int(answer)
        if guess < SMALLEST or guess > BIGGEST:
            print("Choisis entre", SMALLEST, "et", BIGGEST, "!")
            continue
        tries = tries + 1
        print(hint(guess, secret))
        if guess == secret:
            print("Tu as trouvé en", tries, "essai" + ("s" if tries > 1 else "") + ".")
            return tries


def main():
    print("🤔 J'ai choisi un nombre secret entre", SMALLEST, "et", BIGGEST, ". Devine-le !")
    while True:
        play(random.randint(SMALLEST, BIGGEST))
        again = input("On rejoue ? (oui / non) ").strip().lower()
        if not again.startswith("o"):
            print("Merci d'avoir joué !")
            break


if __name__ == "__main__":
    main()

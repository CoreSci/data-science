"""Lesson 1 - The talking computer (L'ordinateur qui parle).

The computer asks questions and answers back. Big idea: a program can ASK
(input) and ANSWER (print). Messages to the child are in French.
Run it in Thonny (green Run button) and answer in the Shell.
"""


def ask_age():
    """Ask for an age until the answer is a number."""
    while True:
        answer = input("Quel âge as-tu ? ")
        if answer.strip().isdigit():
            return int(answer)
        print("Écris ton âge avec des chiffres, par exemple : 7")


def main():
    print("Bonjour ! Je suis l'ordinateur. Je sais parler !")

    name = input("Comment t'appelles-tu ? ").strip() or "mon ami"
    print("Enchanté,", name, "!")

    color = input("Quelle est ta couleur préférée ? ").strip()
    print("Wow,", color, "! C'est aussi la couleur préférée de mon clavier.")

    age = ask_age()
    print("Dans un an, tu auras", age + 1, "ans.")
    print("Et dans 10 ans, tu auras", age + 10, "ans !")

    print("Au revoir,", name, "! À la prochaine !")


if __name__ == "__main__":
    main()

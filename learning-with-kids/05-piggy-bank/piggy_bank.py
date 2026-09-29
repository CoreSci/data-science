"""Lesson 5 - Piggy bank & wish list (La tirelire et la liste de souhaits).

Two small games that REPEAT and REMEMBER:
  1. the piggy bank adds up coins until you type "fini";
  2. the wish list remembers every wish, then reads them all back.
Big idea: a variable remembers a number, a list remembers many things.
Messages to the child are in French.
"""


def read_amount(answer):
    """'2', '0,25' or '0.25' -> a number of dollars; anything else -> None."""
    try:
        amount = float(answer.strip().replace(",", ".").replace("$", ""))
    except ValueError:
        return None
    return amount if amount >= 0 else None


def piggy_bank():
    total = 0.0
    coins = 0
    print("🐷 Mets des sous dans la tirelire ! (tape « fini » pour compter)")
    while True:
        answer = input("Combien de dollars ? (ex. : 2 ou 0,25) ")
        if answer.strip().lower() == "fini":
            break
        amount = read_amount(answer)
        if amount is None:
            print("Hmm, ce n'est pas un montant. Essaie : 1 ou 0,10")
            continue
        total = total + amount
        coins = coins + 1
        print("Clink ! Il y a maintenant", format_dollars(total), "dans la tirelire.")
    print("Tu as mis", coins, "fois des sous. Total :", format_dollars(total), "🎉")
    return total


def wish_list():
    wishes = []
    print("⭐ Dis-moi tes souhaits ! (tape « fini » quand tu as terminé)")
    while True:
        wish = input("Un souhait : ").strip()
        if wish.lower() == "fini":
            break
        if wish:
            wishes.append(wish)
    print("Voici ta liste de", len(wishes), "souhaits :")
    for number, wish in enumerate(wishes, start=1):
        print(" ", number, "-", wish)
    return wishes


def format_dollars(amount):
    """1.5 -> '1,50 $' (Quebec style)."""
    return f"{amount:.2f}".replace(".", ",") + " $"


def main():
    print("1 = la tirelire   2 = la liste de souhaits")
    choice = input("Quel jeu veux-tu ? ").strip()
    if choice == "2":
        wish_list()
    else:
        piggy_bank()


if __name__ == "__main__":
    main()

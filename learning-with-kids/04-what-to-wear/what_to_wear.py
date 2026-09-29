"""Lesson 4 - What should I wear? (Qu'est-ce que je porte ?)

Type the temperature outside (in °C) and the computer suggests clothes.
Big idea: decisions. IF it is cold... ELSE IF it is cool... ELSE...
Messages to the child are in French (Quebec clothing words).
"""


def advice(temperature):
    """Clothing advice for a temperature in degrees Celsius."""
    if temperature < -10:
        return "Très, très froid ! Habit de neige, tuque, mitaines, foulard et bottes."
    elif temperature < 0:
        return "Il gèle ! Manteau d'hiver, tuque, mitaines et bottes."
    elif temperature < 10:
        return "Frais. Un manteau et un chandail chaud."
    elif temperature < 18:
        return "Doux. Un chandail ou une petite veste."
    elif temperature < 25:
        return "Beau temps ! Un t-shirt suffit."
    else:
        return "Chaud ! T-shirt, short, casquette, crème solaire, et de l'eau !"


def read_temperature(answer):
    """Turn what the child typed into a number, or None. Accepts '-5', '12,5' or '12.5'."""
    try:
        return float(answer.strip().replace(",", "."))
    except ValueError:
        return None


def main():
    print("☀️ ❄️  Qu'est-ce que je porte aujourd'hui ?")
    while True:
        answer = input("Quelle température fait-il dehors (en °C) ? Tape « fini » pour arrêter : ")
        if answer.strip().lower() == "fini":
            print("Bonne journée !")
            break
        temperature = read_temperature(answer)
        if temperature is None:
            print("Écris un nombre, par exemple : 5 ou -12")
            continue
        print(advice(temperature))
        print()


if __name__ == "__main__":
    main()

"""Lesson 6 - Turtle drawing (Dessiner avec la tortue).

A little turtle walks on the screen and draws with a pen. We tell it:
move forward, turn, and REPEAT. Big idea: a loop you can SEE.
Messages to the child are in French. A drawing window opens; close it to finish.
"""
import turtle

RAINBOW = ["red", "orange", "gold", "green", "blue", "purple"]


def square(t, size=100):
    """4 sides, 4 turns of 90 degrees."""
    for side in range(4):
        t.forward(size)
        t.left(90)


def star(t, size=150):
    """5 points: go forward, turn 144 degrees, repeat 5 times."""
    t.color("gold")
    for point in range(5):
        t.forward(size)
        t.right(144)


def rainbow_spiral(t, steps=60):
    """Each step goes a bit farther and turns a bit: a spiral appears!"""
    for step in range(steps):
        t.color(RAINBOW[step % len(RAINBOW)])
        t.forward(step * 3)
        t.left(59)


def flower(t, petals=8):
    """A flower is just a square, repeated while turning!"""
    for petal in range(petals):
        t.color(RAINBOW[petal % len(RAINBOW)])
        square(t, 80)
        t.left(360 / petals)


DRAWINGS = {"1": square, "2": star, "3": rainbow_spiral, "4": flower}


def main():
    print("🐢 Que veux-tu dessiner ?")
    print("1 = un carré   2 = une étoile   3 = une spirale arc-en-ciel   4 = une fleur")
    choice = input("Ton choix : ").strip()
    drawing = DRAWINGS.get(choice, star)

    t = turtle.Turtle()
    t.shape("turtle")
    t.pensize(3)
    t.speed(6)            # 1 = slow, 10 = fast, 0 = fastest
    drawing(t)
    print("Bravo ! Ferme la fenêtre pour terminer.")
    turtle.done()


if __name__ == "__main__":
    main()

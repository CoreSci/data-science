"""Tests for the learning-with-kids programs.

Each program runs as the child would use it: its answers are piped to stdin and
its output is checked. Turtle drawings need a display: run under ``xvfb-run``
on a headless machine; the turtle tests are skipped when no display is available.

Run from this folder: ``python -m pytest -q``
"""
import importlib.util
import math
import os
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent


def run(script, answers):
    """Run a lesson script with the given answers (one per line) and return its output."""
    result = subprocess.run([sys.executable, str(HERE / script)], input="\n".join(answers) + "\n",
                            capture_output=True, text=True, encoding="utf-8", timeout=30,
                            env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    assert result.returncode == 0, result.stderr
    return result.stdout


def load(script):
    spec = importlib.util.spec_from_file_location(Path(script).stem, HERE / script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------- 1. talking computer
def test_talking_computer_retries_age_until_it_is_a_number():
    out = run("01-talking-computer/talking_computer.py", ["Léo", "vert", "sept", "7"])
    assert "Enchanté, Léo !" in out
    assert "vert" in out
    assert "Écris ton âge avec des chiffres" in out
    assert "tu auras 8 ans" in out and "tu auras 17 ans" in out


# ---------------------------------------------------------------- 2. song machine
def test_song_machine_sings_chorus_between_verses():
    out = run("02-silly-song-machine/song_machine.py",
              ["une vache", "meuh", "un chien", "wouf", "", ""])
    assert out.count("Tchou-tchou, boum-boum,") == 4          # chorus sung 4 times
    assert "il y a une vache," in out and "meuh ! meuh !" in out
    assert "il y a un chat," in out                            # empty answer -> default animal


# ---------------------------------------------------------------- 3. name detective
def test_name_detective_functions():
    nd = load("03-name-detective/name_detective.py")
    assert nd.count_letters("Marie-Ève") == 8
    assert nd.count_vowels("Marie-Ève") == 5                   # a, i, e, È, e
    assert nd.favourite_letter("Anna") == ("a", 2)
    assert nd.favourite_letter("") == ("", 0)


def test_name_detective_session():
    out = run("03-name-detective/name_detective.py", ["Léo", "123", "fini"])
    assert "Lettres : 3" in out and "À l'envers : oéL" in out
    assert "je ne vois pas de lettres" in out
    assert "Enquête terminée" in out


# ---------------------------------------------------------------- 4. what to wear
@pytest.mark.parametrize("temp, word", [(-20, "Habit de neige"), (-5, "Il gèle"), (5, "Frais"),
                                        (15, "Doux"), (20, "t-shirt suffit"), (30, "crème solaire")])
def test_what_to_wear_advice(temp, word):
    assert word in load("04-what-to-wear/what_to_wear.py").advice(temp)


def test_what_to_wear_session_accepts_comma_decimals_and_rejects_words():
    out = run("04-what-to-wear/what_to_wear.py", ["12,5", "chaud", "-3", "fini"])
    assert "Doux" in out and "Il gèle" in out
    assert "Écris un nombre" in out and "Bonne journée" in out


# ---------------------------------------------------------------- 5. piggy bank
def test_piggy_bank_adds_coins():
    out = run("05-piggy-bank/piggy_bank.py", ["1", "2", "0,25", "0.10", "beaucoup", "fini"])
    assert "Total : 2,35 $" in out and "Tu as mis 3 fois" in out
    assert "ce n'est pas un montant" in out


def test_wish_list_remembers_wishes():
    out = run("05-piggy-bank/piggy_bank.py", ["2", "un vélo", "", "un chiot", "fini"])
    assert "liste de 2 souhaits" in out
    assert "1 - un vélo" in out and "2 - un chiot" in out


# ---------------------------------------------------------------- 6. turtle drawing
def _display_available():
    if sys.platform.startswith("win") or sys.platform == "darwin":
        return True
    return bool(os.environ.get("DISPLAY"))


needs_display = pytest.mark.skipif(not _display_available(), reason="turtle needs a display (use xvfb-run)")


@needs_display
def test_turtle_drawings_close_their_shapes(tmp_path):
    import turtle
    td = load("06-turtle-drawing/turtle_drawing.py")
    screen = turtle.Screen()
    screen.tracer(0)                                           # draw instantly
    t = turtle.Turtle()
    for shape in (td.square, td.star, td.flower):
        t.penup(); t.home(); t.pendown()
        shape(t)
        x, y = t.position()
        assert math.hypot(x, y) < 1e-6, shape.__name__           # closed shapes end where they started
        assert abs(t.heading() % 360) < 1e-6 or abs(t.heading() % 360 - 360) < 1e-6
    t.penup(); t.home(); t.pendown()
    td.rainbow_spiral(t, steps=60)
    assert math.hypot(*t.position()) > 50                      # the spiral moves outward
    screen.update()
    out = tmp_path / "drawing.eps"
    screen.getcanvas().postscript(file=str(out))
    assert out.stat().st_size > 1000                           # something was actually drawn
    screen.clearscreen()


@needs_display
def test_turtle_main_menu(monkeypatch, capsys):
    import turtle
    td = load("06-turtle-drawing/turtle_drawing.py")
    turtle.Screen().tracer(0)
    monkeypatch.setattr("builtins.input", lambda prompt="": "2")
    monkeypatch.setattr(turtle, "done", lambda: None)          # don't wait for the window to close
    td.main()
    assert "Bravo !" in capsys.readouterr().out
    turtle.Screen().clearscreen()


# ---------------------------------------------------------------- 7. guess my number
def test_hint_messages():
    g = load("07-guess-my-number/guess_my_number.py")
    assert g.hint(3, 10).startswith("Trop bas")
    assert g.hint(15, 10).startswith("Trop haut")
    assert g.hint(10, 10).startswith("Bravo")


def test_play_counts_valid_guesses_only(capsys):
    g = load("07-guess-my-number/guess_my_number.py")
    answers = iter(["dix", "50", "10", "15", "12"])
    assert g.play(12, ask=lambda prompt: next(answers)) == 3   # "dix" and 50 are rejected, not counted
    out = capsys.readouterr().out
    assert "Écris un nombre" in out and "Choisis entre 1 et 20" in out
    assert "Tu as trouvé en 3 essais." in out


def test_guess_game_full_session_with_binary_search():
    # A binary-search player always wins within 5 guesses for 1..20, whatever the secret.
    script = """
import builtins, random, runpy, sys
low, high, state = 1, 20, {"guess": None}
def fake_input(prompt=""):
    if prompt.startswith("On rejoue"):
        return "non"
    state["guess"] = (low + high) // 2
    return str(state["guess"])
builtins.input = fake_input
real_print = builtins.print
def watching_print(*args, **kw):
    global low, high
    text = " ".join(str(a) for a in args)
    if text.startswith("Trop bas"):
        low = state["guess"] + 1
    elif text.startswith("Trop haut"):
        high = state["guess"] - 1
    real_print(*args, **kw)
builtins.print = watching_print
runpy.run_path(sys.argv[1], run_name="__main__")
"""
    result = subprocess.run([sys.executable, "-c", script, str(HERE / "07-guess-my-number/guess_my_number.py")],
                            capture_output=True, text=True, encoding="utf-8", timeout=30,
                            env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    assert result.returncode == 0, result.stderr
    assert "Bravo, tu as trouvé" in result.stdout and "Merci d'avoir joué" in result.stdout
    tries = int(result.stdout.split("Tu as trouvé en ")[1].split(" ")[0])
    assert tries <= 5

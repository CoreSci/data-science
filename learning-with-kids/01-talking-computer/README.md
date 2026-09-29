# Leçon 1 — L'ordinateur qui parle *(The talking computer)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~10 minutes (la première fois) · **Jeu :** 10 minutes

## Objectif (*goal*)
L'ordinateur **pose des questions** et **répond** : ton prénom, ta couleur préférée, ton âge. L'enfant découvre qu'un programme peut **demander** (*input*) et **répondre** (*output / print*).

## Préparation (~10 minutes)
1. Installer **Thonny** (thonny.org), une seule fois pour toutes les leçons.
2. Ouvrir `talking_computer.py` dans Thonny.
3. Cliquer sur **Exécuter** (le bouton vert ▶, ou **F5**).
4. Répondre aux questions en bas, dans la **Console** (*Shell*), puis appuyer sur **Entrée**.

```
 ┌──────────────── Thonny ────────────────┐
 │  (le programme, en haut)                │
 ├─────────────────────────────────────────┤
 │  Console :                              │
 │  Comment t'appelles-tu ? Léo  ⏎         │
 │  Enchanté, Léo !                        │
 └─────────────────────────────────────────┘
```

## Comment ça marche
- **Pour le parent :** `input("…")` affiche une question et attend la réponse de l'enfant ; `print(…)` affiche un message. `ask_age()` redemande tant que la réponse n'est pas un nombre (`isdigit()`), puis on calcule `age + 1` et `age + 10`.
- **Pour l'enfant :** « L'ordinateur ne devine rien : il ne sait que ce que tu lui écris. Il garde ta réponse dans une boîte avec un nom, comme `name`. »

## Essaie ça ! (*try this*)
1. **Répondre n'importe quoi :** écrire « sept » au lieu de « 7 ». Que dit l'ordinateur ?
2. **Changer ce qu'il dit :** dans le programme, remplacer « C'est aussi la couleur préférée de mon clavier » par une phrase inventée par l'enfant.
3. **Une nouvelle question :** ajouter `animal = input("Quel est ton animal préféré ? ")` et une réponse avec `print`.
4. **Dans 100 ans :** changer `age + 10` en `age + 100`. Quel âge aurais-tu ?

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien.
- Temps d'écran court, toujours avec un adulte.

*Programme original, inspiré de mes exercices du cours « Python for Everybody » (2014).*

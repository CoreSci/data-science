# Leçon 6 — Dessiner avec la tortue *(Turtle drawing)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~5 minutes · **Jeu :** 15–20 minutes

## Objectif (*goal*)
Une petite **tortue** se promène sur l'écran avec un crayon : on lui dit **avance**, **tourne**, et **recommence**. Elle dessine un **carré**, une **étoile**, une **spirale arc-en-ciel** ou une **fleur**. L'enfant découvre une **boucle** (*loop*) qu'on peut **voir**.

## Préparation (~5 minutes)
1. Ouvrir `turtle_drawing.py` dans **Thonny**. Le module `turtle` est déjà inclus avec Python, rien à installer.
2. Cliquer sur **Exécuter** (▶ ou **F5**) et choisir un dessin : **1** carré, **2** étoile, **3** spirale, **4** fleur.
3. Une fenêtre s'ouvre et la tortue dessine. Fermer la fenêtre pour terminer.

```
  Un carré = 4 fois :           Une étoile = 5 fois :
     avance 100                    avance 150
     tourne 90°                    tourne 144°
      ┌─────┐                          ★
      │     │
      └─────┘
```

## Comment ça marche
- **Pour le parent :** `for side in range(4):` répète 4 fois `forward(100)` puis `left(90)`. 4 × 90° = 360° : on revient au départ. L'étoile tourne de 144° cinq fois (5 × 144° = 720°, donc deux tours complets). La spirale avance un peu plus loin à chaque pas (`step * 3`) et change de couleur. La fleur répète le carré en tournant, une fonction dans une boucle !
- **Pour l'enfant :** « La tortue est très obéissante : tu lui dis “avance, tourne”, et si tu lui dis de le faire 4 fois, elle dessine un carré ! »

## Essaie ça ! (*try this*)
1. **Un triangle :** copier `square`, mettre `range(3)` et tourner de `120`. Pourquoi 120 ? (3 × 120 = 360 !)
2. **Tortue plus rapide :** changer `t.speed(6)` en `t.speed(0)`, puis en `t.speed(1)` pour la voir marcher lentement.
3. **Plus de pétales :** dans `flower`, changer `petals=8` en `petals=20`. Magnifique !
4. **Nos couleurs :** changer la liste `RAINBOW` avec les couleurs préférées de l'enfant (en anglais : `"pink"`, `"cyan"`, `"black"`…).

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien.
- Temps d'écran court, toujours avec un adulte. Après, on peut dessiner les mêmes formes sur papier en « faisant la tortue » !

*Programme original, inspiré de mes exercices du cours « Python for Everybody » (2014).*

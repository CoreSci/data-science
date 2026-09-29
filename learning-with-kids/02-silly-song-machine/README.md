# Leçon 2 — La machine à chansons rigolotes *(Silly song machine)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~5 minutes · **Jeu :** 15 minutes

## Objectif (*goal*)
L'enfant choisit trois animaux et leurs bruits ; l'ordinateur **chante une chanson** avec un **refrain** (*chorus*) qui revient entre chaque couplet. L'enfant découvre qu'une **fonction** (*function*) est une **recette** qu'on écrit une fois et qu'on utilise autant de fois qu'on veut.

## Préparation (~5 minutes)
1. Ouvrir `song_machine.py` dans **Thonny** (voir la [leçon 1](../01-talking-computer/)).
2. Cliquer sur **Exécuter** (▶ ou **F5**).
3. Écrire chaque animal **avec son petit mot** (« une vache », « un chien »), puis son bruit (« meuh », « wouf »).

```
 Animal numéro 1 (ex. : une vache) : une vache ⏎
 Quel bruit fait une vache ? meuh ⏎
 …
 🎵 Voici ta chanson ! 🎵
   Tchou-tchou, boum-boum, …
```

## Comment ça marche
- **Pour le parent :** `chorus()` et `verse(animal, sound)` sont des fonctions. `chorus()` est écrite une seule fois, mais appelée 4 fois. `verse()` reçoit l'animal et le bruit en **paramètres** (*parameters*), donc chaque couplet est différent. Les réponses sont gardées dans une liste (`animals`) avant de chanter.
- **Pour l'enfant :** « Le refrain, c'est comme une recette de biscuits : on l'écrit une fois dans le livre, et on peut en faire autant de fois qu'on veut ! »

## Essaie ça ! (*try this*)
1. **Chanter ensemble :** lire la chanson à voix haute, avec les bruits d'animaux !
2. **Nouveau refrain :** l'enfant invente les paroles du refrain ; le parent les écrit dans `chorus()`. Elles changent partout d'un coup !
3. **Cinq animaux :** changer `range(1, 4)` en `range(1, 6)`.
4. **Refrain deux fois :** appeler `chorus()` deux fois à la fin, pour une grande finale.

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien.
- Temps d'écran court, toujours avec un adulte.

*Paroles et programme originaux, inspirés de mes exercices du cours « Python for Everybody » (2014).*

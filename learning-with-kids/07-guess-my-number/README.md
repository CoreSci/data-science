# Leçon 7 — Devine mon nombre *(Guess my number)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~5 minutes · **Jeu :** autant qu'on veut !

## Objectif (*goal*)
L'ordinateur choisit un **nombre secret entre 1 et 20**. L'enfant devine, et l'ordinateur répond **« trop haut »** ou **« trop bas »** jusqu'à ce qu'il trouve. L'enfant découvre un vrai jeu : **comparer** (plus grand, plus petit), **recommencer**, et un peu de **hasard** (*random*).

## Préparation (~5 minutes)
1. Ouvrir `guess_my_number.py` dans **Thonny**.
2. Cliquer sur **Exécuter** (▶ ou **F5**).
3. Écrire un nombre et appuyer sur **Entrée**. À la fin : « oui » pour rejouer, « non » pour arrêter.

```
 Ton nombre (1 à 20) : 10 ⏎
 Trop haut ! ⬇️
 Ton nombre (1 à 20) : 5 ⏎
 Trop bas ! ⬆️
 Ton nombre (1 à 20) : 7 ⏎
 Bravo, tu as trouvé ! 🎉
 Tu as trouvé en 3 essais.
```

## Comment ça marche
- **Pour le parent :** `random.randint(1, 20)` choisit le nombre secret. `play()` répète : lire la réponse, vérifier que c'est un nombre entre 1 et 20 (sinon on ne compte pas l'essai), puis `hint()` compare avec `<` et `>`. On compte les essais jusqu'à la bonne réponse.
- **Pour l'enfant :** « L'ordinateur a caché un nombre dans sa tête. Il ne triche pas : il te dit juste si tu es trop haut ou trop bas. »

## Essaie ça ! (*try this*)
1. **La stratégie secrète :** toujours commencer par **10**, le milieu ! Puis choisir le milieu de ce qui reste. Avec cette méthode, on trouve toujours en **5 essais ou moins**.
2. **Plus difficile :** changer `BIGGEST = 20` en `100`. Combien d'essais faut-il maintenant ?
3. **Les rôles inversés :** c'est l'enfant qui pense à un nombre, et le parent qui devine (sans ordinateur !), avec les mêmes mots « trop haut » et « trop bas ».
4. **Le champion :** noter sur papier le nombre d'essais de chaque partie. Qui a le meilleur score ?

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien.
- Temps d'écran court, toujours avec un adulte.

*Programme original. Le jeu « devine le nombre » est un exercice classique de programmation.*

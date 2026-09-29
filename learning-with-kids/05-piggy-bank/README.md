# Leçon 5 — La tirelire et la liste de souhaits *(Piggy bank & wish list)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~5 minutes · **Jeu :** 15 minutes

## Objectif (*goal*)
Deux petits jeux qui **répètent** et **se souviennent** :
1. **la tirelire** additionne les sous qu'on y met, jusqu'à ce qu'on écrive « fini » ;
2. **la liste de souhaits** retient chaque souhait, puis les relit tous.

L'enfant découvre qu'une **variable** (*variable*) se souvient d'un nombre, et qu'une **liste** (*list*) se souvient de plusieurs choses.

## Préparation (~5 minutes)
1. Ouvrir `piggy_bank.py` dans **Thonny**.
2. Pour la tirelire : sortir quelques vraies pièces (0,05 $, 0,10 $, 0,25 $, 1 $, 2 $). C'est plus amusant !
3. Cliquer sur **Exécuter** (▶ ou **F5**), puis choisir **1** (tirelire) ou **2** (souhaits).

```
 Combien de dollars ? (ex. : 2 ou 0,25) 0,25 ⏎
 Clink ! Il y a maintenant 0,25 $ dans la tirelire.
 Combien de dollars ? (ex. : 2 ou 0,25) 1 ⏎
 Clink ! Il y a maintenant 1,25 $ dans la tirelire.
```

## Comment ça marche
- **Pour le parent :** la boucle `while True:` répète la question jusqu'au mot « fini » (`break`). Dans la tirelire, `total = total + amount` fait grandir le total ; « 0,25 » et « 0.25 » sont tous les deux acceptés. Dans la liste de souhaits, `wishes.append(wish)` ajoute chaque souhait, puis une boucle `for` les relit avec leur numéro.
- **Pour l'enfant :** « La variable `total`, c'est la tirelire : chaque fois que tu mets une pièce, elle devient plus lourde. La liste, c'est un carnet où l'on écrit chaque souhait sur une nouvelle ligne. »

## Essaie ça ! (*try this*)
1. **Compter les vraies pièces :** mettre chaque pièce de la main dans un bol, et la taper dans l'ordinateur. Le total est-il bon ? Vérifier en comptant ensemble.
2. **Objectif vélo :** ajouter une ligne à la fin : si le total est plus grand que 5, afficher « Tu peux acheter une petite surprise ! ».
3. **La liste de l'épicerie :** utiliser la liste de souhaits pour faire la liste des courses de la famille.
4. **Le souhait préféré :** afficher seulement le premier souhait avec `print(wishes[0])`.

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien : quand on le ferme, la tirelire est vide (c'est normal !).
- Pièces de monnaie : attention avec les plus petits (risque d'étouffement).

*Programme original, inspiré de mes exercices du cours « Python for Everybody » (2014).*

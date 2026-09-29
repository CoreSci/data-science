# Leçon 3 — Le détective des prénoms *(Name detective)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~5 minutes · **Jeu :** 15 minutes

## Objectif (*goal*)
L'ordinateur fait une **enquête** sur un prénom : combien de **lettres**, combien de **voyelles**, quelle est sa **lettre préférée** (celle qui revient le plus), et le prénom **à l'envers**. L'enfant découvre la **boucle** (*loop*) : l'ordinateur regarde chaque lettre, une après l'autre.

## Préparation (~5 minutes)
1. Ouvrir `name_detective.py` dans **Thonny**.
2. Cliquer sur **Exécuter** (▶ ou **F5**).
3. Écrire des prénoms : le sien, celui des parents, du chat… Écrire « fini » pour arrêter.

```
 Donne-moi un prénom (ou tape « fini ») : Anna ⏎
   Lettres : 4
   Voyelles : 2
   Lettre préférée : A (2 fois)
   À l'envers : annA
```

## Comment ça marche
- **Pour le parent :** `for letter in word:` passe sur chaque lettre. `count_letters()` compte les lettres (pas les tirets ni les espaces), `count_vowels()` compte les voyelles, y compris les accents (é, è, à…), et `favourite_letter()` utilise un dictionnaire (*dict*) pour compter chaque lettre. `name[::-1]` retourne le mot.
- **Pour l'enfant :** « L'ordinateur est un détective très patient : il regarde chaque lettre avec sa loupe et il compte, compte, compte… »

## Essaie ça ! (*try this*)
1. **Qui a le plus long prénom ?** Comparer les prénoms de toute la famille.
2. **Les palindromes :** « Anna », « Ève », « Otto » se lisent pareil à l'endroit et à l'envers. En trouver d'autres !
3. **Prénom composé :** essayer « Marie-Ève ». Le tiret compte-t-il comme une lettre ?
4. **Nouvelle enquête :** ajouter une ligne qui affiche le prénom en MAJUSCULES : `print(name.upper())`.

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien.
- Temps d'écran court, toujours avec un adulte.

*Programme original, inspiré de mes exercices du cours « Python for Everybody » (2014).*

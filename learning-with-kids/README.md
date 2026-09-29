# Apprendre avec les enfants — Python (Learning with kids)

Sept petits programmes Python à faire **avec un enfant de 6 à 8 ans**. À cet âge, l'enfant ne tape pas encore le code : le parent le lance, l'enfant **joue**, répond aux questions de l'ordinateur, puis on change ensemble **un nombre ou un mot** dans le programme pour voir ce qui se passe.

*Seven small Python programs for a child aged 6–8 with a parent. Guides are in French; code and code comments are in English, like the rest of this portfolio. What the program says to the child is in French.*

## Les leçons

| # | Leçon | L'enfant apprend… |
|---|---|---|
| 1 | [L'ordinateur qui parle](01-talking-computer/) *(The talking computer)* | l'ordinateur pose des questions et répond (*input / output*) |
| 2 | [La machine à chansons rigolotes](02-silly-song-machine/) *(Silly song machine)* | une **fonction** = une recette qu'on réutilise |
| 3 | [Le détective des prénoms](03-name-detective/) *(Name detective)* | compter les lettres, une **boucle** (*loop*) |
| 4 | [Qu'est-ce que je porte ?](04-what-to-wear/) *(What should I wear?)* | prendre des **décisions** : si… sinon… (*if / else*) |
| 5 | [La tirelire et la liste de souhaits](05-piggy-bank/) *(Piggy bank & wish list)* | répéter et **se souvenir** (variables, listes) |
| 6 | [Dessiner avec la tortue](06-turtle-drawing/) *(Turtle drawing)* | les boucles qu'on **voit** : carrés, étoiles, spirales |
| 7 | [Devine mon nombre](07-guess-my-number/) *(Guess my number)* | un vrai jeu : comparer, recommencer, le hasard |

## Installation (une seule fois)

1. Installer **Thonny** (thonny.org). C'est un éditeur simple pour débutants, avec Python déjà inclus.
2. Ouvrir le fichier `.py` de la leçon dans Thonny.
3. Cliquer sur le bouton vert **Exécuter** (*Run*, ou touche **F5**).
4. Les questions apparaissent en bas, dans la **Console** (*Shell*). On tape la réponse et on appuie sur **Entrée**.

Pour arrêter un programme : le bouton rouge **Stop**.

## Conseils pour le parent

- **Une leçon = une idée.** 15 à 20 minutes suffisent. On arrête quand c'est encore amusant.
- **L'enfant décide, le parent tape.** « Quel mot veux-tu que l'ordinateur dise ? » Puis on relance.
- **Les erreurs sont normales.** Si Python affiche un message rouge, on le lit ensemble : c'est l'ordinateur qui dit « je n'ai pas compris ». On corrige et on recommence.
- **Sécurité à l'écran :** ces programmes n'utilisent pas Internet. Le temps d'écran reste court et partagé avec un adulte.

*Programmes originaux, inspirés de mes exercices du cours « Python for Everybody » (2014). Aucun code du cours n'est repris.*

## Tests

`test_lessons.py` exécute chaque programme avec des réponses simulées (et la tortue sur un écran virtuel) : `python -m pytest -q`.

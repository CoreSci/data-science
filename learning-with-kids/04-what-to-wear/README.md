# Leçon 4 — Qu'est-ce que je porte ? *(What should I wear?)*

**Âge :** 6–8 ans, avec un parent · **Préparation :** ~5 minutes · **Jeu :** 10–15 minutes

## Objectif (*goal*)
On écrit la **température** dehors (en °C) et l'ordinateur dit **quoi porter** : tuque et mitaines, chandail ou t-shirt. L'enfant découvre les **décisions** : **si** il fait froid… **sinon si**… **sinon**… (*if / elif / else*).

## Préparation (~5 minutes)
1. Ouvrir `what_to_wear.py` dans **Thonny**.
2. Regarder ensemble la température du jour (thermomètre, fenêtre, météo).
3. Cliquer sur **Exécuter** (▶ ou **F5**), écrire la température, puis « fini » pour arrêter.

```
 Quelle température fait-il dehors (en °C) ? -8 ⏎
 Il gèle ! Manteau d'hiver, tuque, mitaines et bottes.
```

| Température | Conseil |
|---|---|
| moins de −10 °C | habit de neige, tuque, mitaines, foulard, bottes |
| −10 à 0 °C | manteau d'hiver, tuque, mitaines, bottes |
| 0 à 10 °C | manteau et chandail chaud |
| 10 à 18 °C | chandail ou petite veste |
| 18 à 25 °C | t-shirt |
| 25 °C et plus | t-shirt, short, casquette, crème solaire, eau |

## Comment ça marche
- **Pour le parent :** `advice()` teste les conditions **dans l'ordre**, avec `if`, puis `elif`, puis `else`. La première condition vraie gagne, et les autres ne sont pas regardées. `read_temperature()` accepte « 12,5 » avec une virgule, comme au Québec.
- **Pour l'enfant :** « L'ordinateur pose des questions dans l'ordre : Est-ce qu'il fait très, très froid ? Non ? Alors, est-ce qu'il gèle ? Non ? Alors… »

## Essaie ça ! (*try this*)
1. **La météo de la semaine :** chaque matin, lancer le programme avec la vraie température. L'ordinateur avait-il raison ?
2. **Températures folles :** essayer −40 et 45. Que dit-il ?
3. **Ajouter la pluie :** ajouter une question « Est-ce qu'il pleut ? (oui / non) » et, si oui, afficher « N'oublie pas tes bottes de pluie et ton parapluie ! ».
4. **Nos propres règles :** l'enfant décide à partir de quelle température on porte un short. On change le nombre `25`.

## Sécurité
- Le programme n'utilise pas Internet et n'enregistre rien.
- Les conseils sont un jeu : c'est le parent qui décide des vêtements !

*Programme original, inspiré de mes exercices du cours « Python for Everybody » (2014).*

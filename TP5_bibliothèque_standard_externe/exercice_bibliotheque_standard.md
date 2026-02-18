# Exercices – Bibliothèques `random`, `datetime` et `os`

## Exercice 1 : Jeu de devinette (`random`)

Créer un programme qui :

- Génère un nombre aléatoire entre 1 et 100.
- Donne à l’utilisateur 5 tentatives maximum pour deviner le nombre.
- Après chaque tentative, affiche :
  - "Trop grand" si le nombre proposé est supérieur.
  - "Trop petit" si le nombre proposé est inférieur.
- Affiche un message de victoire avec le nombre de tentatives utilisées.
- Affiche le bon nombre si l’utilisateur perd.

---

## Exercice 2 : Générateur de mot de passe (`random`)

Créer un programme qui :

- Demande à l’utilisateur la longueur du mot de passe.
- Génère un mot de passe aléatoire contenant :
  - Des lettres (majuscules et minuscules)
  - Des chiffres
  - Des caractères spéciaux
- Vérifie que le mot de passe contient au moins un chiffre.
- Affiche le mot de passe généré.

---

## Exercice 3 : Calculateur d’âge précis (`datetime`)

Créer un programme qui :

- Demande à l’utilisateur sa date de naissance (jour, mois, année).
- Calcule son âge exact en années.
- Calcule le nombre total de jours vécus.
- Affiche les résultats.

---

## Exercice 4 : Création automatique de dossier daté (`os` + `datetime`)

Créer un programme qui :

- Récupère la date du jour.
- Crée un dossier portant le nom de la date (format : AAAA-MM-JJ).
- Vérifie si le dossier existe déjà :
  - S’il existe, afficher un message d’information.
  - Sinon, créer le dossier et afficher un message de confirmation.

---

## Exercice 5 : Journal d’activité aléatoire (`random` + `datetime` + `os`)

Créer un programme qui :

1. Génère une date aléatoire entre le 1er janvier 2020 et aujourd’hui.
2. Crée un fichier texte nommé avec cette date.
3. Écrit dans le fichier :
   - La date générée
   - Une phrase choisie aléatoirement parmi une liste prédéfinie.
4. Vérifie si le fichier existe déjà avant de l’écrire.

### TP5 : Création d'une Application de Visualisation de Données avec **Pandas** et **Streamlit**

---

#### Objectif du TP
Apprendre à manipuler des données avec **Pandas** et créer une interface interactive pour les visualiser avec **Streamlit**. Vous construirez une application qui permet de charger un fichier CSV, de l'explorer, et de visualiser les données sous forme de statistiques et de graphiques.

---

### Instructions Générales
1. Installez les bibliothèques nécessaires avant de commencer :
   ```bash
   pip install pandas streamlit matplotlib seaborn
   ```
2. Téléchargez un fichier CSV, comme [le dataset Iris](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv), ou utilisez un fichier de votre choix.

---

### Énoncé

#### Étape 1 : Configuration de l'application
1. Créez un fichier Python nommé `app.py`.
2. Importez les bibliothèques nécessaires : `streamlit`, `pandas`, `matplotlib.pyplot`, et `seaborn`.
3. Ajoutez un **titre** et une **description** à l'application Streamlit pour indiquer son objectif.

#### Étape 2 : Chargement des données
1. Ajoutez une option dans la barre latérale (`st.sidebar`) pour permettre à l'utilisateur de charger un fichier CSV à l'aide de la fonction `file_uploader` de Streamlit.
2. Une fois le fichier chargé, lisez-le avec Pandas (`pd.read_csv`) et affichez les 5 premières lignes à l'aide de Streamlit.
3. Vérifiez que l'application fonctionne en chargeant un fichier de test.

**Questions :**
- Quelle fonction permet de lire un fichier CSV avec Pandas ?
- Comment afficher dynamiquement les données chargées dans Streamlit ?

---

#### Étape 3 : Exploration des données

**3.1 - Afficher les statistiques descriptives**
1. Ajoutez une option pour afficher les **statistiques descriptives** du fichier chargé.
2. Affichez-les dans un tableau interactif.

**Question :**
- Quelle méthode de Pandas permet d’obtenir des statistiques descriptives rapidement ? 

---

**3.2 - Identifier les types de colonnes**
1. Ajoutez une option pour afficher les types de données de chaque colonne.
2. Affichez cette information dans une section dédiée.

**Question :**
- Quelle méthode de Pandas permet de connaître le type de données de chaque colonne ? 

---

**3.3 - Vérifier les valeurs manquantes**
1. Ajoutez une option pour identifier les colonnes ayant des valeurs manquantes.
2. Affichez le nombre de valeurs manquantes pour chaque colonne.

**Questions :**
- Quelle méthode permet de détecter les valeurs manquantes dans Pandas ?
- Comment calculer le total des valeurs manquantes pour chaque colonne ?

---

#### Étape 4 : Visualisation des données

**4.1 - Histogramme**
1. Ajoutez une option pour afficher un histogramme d'une colonne numérique sélectionnée par l'utilisateur.
2. Permettez à l'utilisateur de personnaliser le nombre de classes (bins) via un curseur.

**Questions :**
- Quelle fonction de Matplotlib permet de créer un histogramme ?
- Comment récupérer l'entrée de l'utilisateur pour choisir la colonne à visualiser ?

---

**4.2 - Nuage de points**
1. Ajoutez une option pour créer un **nuage de points**. Permettez à l'utilisateur de choisir les colonnes pour les axes X et Y.
2. Ajoutez une légende dynamique pour une meilleure interprétation des points.

**Questions :**
- Quelle fonction de Seaborn permet de créer un nuage de points ?
- Comment rendre les choix de l'utilisateur interactifs avec Streamlit ?

---

**4.3 - Boxplot**
1. Ajoutez une option pour afficher un **boxplot** pour une colonne sélectionnée par l'utilisateur.
2. Affichez le graphique dans une section dédiée.

**Questions :**
- Quelle méthode de Seaborn est utilisée pour créer un boxplot ?
- Pourquoi les boxplots sont-ils utiles pour l’analyse des données ?

---

#### Étape 5 : Tester l'application
1. Exécutez votre application dans le terminal avec la commande suivante :
   ```bash
   streamlit run app.py
   ```
2. Testez chaque fonctionnalité avec un fichier CSV, et vérifiez que les graphiques et les statistiques s’affichent correctement.

---

### Critères d'évaluation
1. L'application Streamlit doit être fonctionnelle et ergonomique.
2. Chaque fonctionnalité demandée doit être implémentée correctement.
3. Le code doit être clair et bien commenté.

---

### Travail supplémentaire (optionnel)
- Ajoutez une option pour sauvegarder les graphiques générés au format PNG.
- Permettez à l'utilisateur de télécharger les données manipulées sous forme de fichier CSV.

---
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title("Application de Visualisation de Données")
st.write("**Explorez vos données facilement grâce à cette application interactive !**")

# Chargement du fichier CSV
st.sidebar.header("Chargement des données")
uploaded_file = st.sidebar.file_uploader("Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lecture du fichier avec Pandas
    df = pd.read_csv(uploaded_file)

    # Afficher les 5 premières lignes
    st.subheader("Aperçu des données")
    st.write(df.head())

    # Options pour explorer les données
    st.sidebar.subheader("Options d'exploration")

    # Statistiques descriptives
    if st.sidebar.checkbox("Afficher les statistiques descriptives"):
        st.subheader("Statistiques descriptives")
        st.write(df.describe())

    # Afficher les types de colonnes
    if st.sidebar.checkbox("Afficher les types de colonnes"):
        st.subheader("Types de colonnes")
        st.write(df.dtypes)

    # Afficher les valeurs manquantes
    if st.sidebar.checkbox("Afficher les valeurs manquantes"):
        st.subheader("Valeurs manquantes")
        st.write(df.isnull().sum())

    # Visualisation
    st.sidebar.subheader("Options de visualisation")

    # Afficher un histogramme
    if st.sidebar.checkbox("Afficher un histogramme"):
        st.subheader("Histogramme")
        column = st.sidebar.selectbox("Choisissez une colonne", df.select_dtypes(include=["float64", "int64"]).columns)
        bins = st.sidebar.slider("Nombre de classes (bins)", 5, 50, 10)
        plt.figure(figsize=(8, 5))
        plt.hist(df[column], bins=bins, color='skyblue', edgecolor='black')
        plt.title(f"Histogramme de {column}")
        plt.xlabel(column)
        plt.ylabel("Fréquence")
        st.pyplot(plt)

    # Graphique en nuage de points
    if st.sidebar.checkbox("Afficher un nuage de points"):
        st.subheader("Nuage de points")
        x_col = st.sidebar.selectbox("Axe X", df.select_dtypes(include=["float64", "int64"]).columns)
        y_col = st.sidebar.selectbox("Axe Y", df.select_dtypes(include=["float64", "int64"]).columns)
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=df.columns[-1])
        plt.title(f"Nuage de points : {x_col} vs {y_col}")
        st.pyplot(plt)

    # Graphique en boîte (boxplot)
    if st.sidebar.checkbox("Afficher un boxplot"):
        st.subheader("Boxplot")
        column = st.sidebar.selectbox("Choisissez une colonne pour le boxplot", df.select_dtypes(include=["float64", "int64"]).columns)
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, y=column)
        plt.title(f"Boxplot de {column}")
        st.pyplot(plt)
else:
    st.write("Veuillez télécharger un fichier CSV pour commencer.")

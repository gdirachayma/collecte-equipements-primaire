import streamlit as st
import pandas as pd

st.title("📊 Application de collecte de données")

# --- Formulaire de collecte ---
with st.form("formulaire"):
    nom = st.text_input("Nom")
    age = st.number_input("Âge", min_value=0, max_value=120)
    feedback = st.text_area("Vos commentaires")

    submitted = st.form_submit_button("Envoyer")

if submitted:
    # --- Sauvegarde locale (exemple simple) ---
    data = pd.DataFrame([[nom, age, feedback]], columns=["Nom", "Âge", "Commentaire"])
    data.to_csv("donnees.csv", mode="a", header=False, index=False)
    st.success("✅ Données envoyées avec succès !")

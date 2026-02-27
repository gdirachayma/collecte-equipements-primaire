import streamlit as st
from roboflow import Roboflow
from PIL import Image
import numpy as np
import cv2

# Initialisation Roboflow
rf = Roboflow(api_key="U4TqKvyaYQ5LfxGVumph")
project = rf.workspace().project("find_desks")  # Remplace par ton projet
model = project.version(1).model  # Version 1 par exemple

st.title("Détecteur et compteur de tables")

# Upload d'image
uploaded_file = st.file_uploader("Choisissez une photo de la salle de classe", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image chargée", use_column_width=True)
    
    # Convertir en array pour Roboflow
    img_array = np.array(image)
  
    
    # Prédiction
    prediction = model.predict(img_array, confidence=40, overlap=30).json()
    
    # Compter les tables
    table_count = len(prediction['predictions'])
    
    st.write(f"Nombre de tables détectées : {table_count}")
    
    # Afficher image annotée
    annotated = model.predict(img_array, confidence=40, overlap=30).plot()
    st.image(annotated, caption="Image annotée", use_column_width=True)

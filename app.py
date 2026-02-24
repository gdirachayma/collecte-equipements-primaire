import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.title("Détection et comptage des tables en classe")

# Charger modèle YOLO
model = YOLO("yolov8n.pt")  # modèle léger pré-entraîné

uploaded_file = st.file_uploader("Télécharge une image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image chargée", use_column_width=True)

    # Convertir image
    img_array = np.array(image)

    # Détection
    
    results = model(img_array, conf=0.5)

    # Compter les objets détectés
    boxes = results[0].boxes
    class_ids = boxes.cls.tolist()

    # Classes COCO :
    # 60 = dining table
    # 62 = tv
    # etc.

    table_count = class_ids.count(60)

    st.write(f"Nombre de tables détectées : {table_count}")

    # Afficher image annotée
    annotated = results[0].plot()
    st.image(annotated, caption="Résultat détection", use_column_width=True)

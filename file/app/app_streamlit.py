import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Orange Quality Classification", 
    page_icon="🍊"
    )

model = joblib.load('model/orange_quality_model.joblib')

st.title("🍊 Orange Quality Classification")
st.markdown("Application to predict the quality of oranges")

diameter = st.slider("Diameter", 4.0, 10.0, 6.5)
berat = st.slider("Weight", 100, 250, 210)
tebal_kulit = st.slider("Skin Thickness", 0.2, 1.0, 0.8)
kadar_gula = st.slider("Sugar Content", 8, 14, 12)
asal_daerah = st.selectbox("Origin", ["Jawa Barat", "Kalimantan", "Jawa Tengah"])
warna = st.selectbox("Color", ["hijau", "oranye", "kuning"])
musim_panen = st.selectbox("Harvest Season", ["kemarau", "hujan"])

if st.button("Predict Quality", type="primary"):
    new_data = pd.DataFrame([[diameter, berat, tebal_kulit, kadar_gula, asal_daerah, warna, musim_panen]],
        columns=[
            "diameter", "berat", "tebal_kulit", "kadar_gula", "asal_daerah", "warna", "musim_panen"
        ])
    
    prediksi = model.predict(new_data)[0]
    presentase = max(model.predict_proba(new_data)[0])
    
    if prediksi == "Bagus":
        st.success(f"Model memprediksi kualitas jeruk sebagai '{prediksi}' dengan presentase {presentase*100:.2f}%")
        st.balloons()
    elif prediksi == "Sedang":
        st.warning(f"Model memprediksi kualitas jeruk sebagai '{prediksi}' dengan presentase {presentase*100:.2f}%")
    elif prediksi == "Jelek":
        st.error(f"Model memprediksi kualitas jeruk sebagai '{prediksi}' dengan presentase {presentase*100:.2f}%")
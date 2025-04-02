import streamlit as st
import requests
import json

st.set_page_config(page_title="Typeform API Viewer", layout="wide")

st.title("🔍 Visualizador de Formularios Typeform")

form_id = "WD4lUnn8"
token = "tfp_9sDQa5Ns2LeGtgxwiPp2hnYWsUcqnHG6Nv5VXbjmCXuR_e5CajswVJsC9"

url = f"https://api.typeform.com/forms/{form_id}"
headers = {"Authorization": f"Bearer {token}"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    form_data = response.json()
    st.success("✅ Formulario cargado correctamente.")
    st.subheader("📋 JSON del formulario")
    st.json(form_data)

    json_str = json.dumps(form_data, indent=2, ensure_ascii=False)
    st.download_button("⬇️ Descargar JSON", data=json_str, file_name="formulario.json", mime_

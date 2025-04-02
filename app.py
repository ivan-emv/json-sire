import streamlit as st
import requests
import json

st.set_page_config(page_title="Typeform API Viewer", layout="wide")

st.title("🔍 Visualizador de Formularios Typeform")
st.write("Consulta la estructura de un formulario desde la API de Typeform.")

# Parámetros del formulario
form_id = "WD4lUnn8"
token = "tfp_EVXzJeuqw6XhrwLZ2EGnAWQNuoAsnPcpP9JUXr861iU8_3soNTw72AFXgdX"

# Construcción de la URL y headers
url = f"https://api.typeform.com/forms/{form_id}"
headers = {"Authorization": f"Bearer {token}"}

# Consulta a la API
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    form_data = response.json()

    st.success("✅ Formulario recuperado correctamente.")
    st.subheader("📋 Estructura del formulario (JSON)")
    st.json(form_data)

    # Descarga del JSON
    json_str = json.dumps(form_data, indent=2, ensure_ascii=False)
    st.download_button(
        label="⬇️ Descargar JSON",
        data=json_str,
        file_name="formulario.json",
        mime="application/json"
    )

except requests.exceptions.HTTPError as e:
    st.error(f"❌ Error HTTP: {e.response.status_code}")
    st.code(e.response.text)

except Exception as e:
    st.error("❌ Ocurrió un error inesperado:")
    st.exception(e)

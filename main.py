import streamlit as st
import pandas as pd
import gdown
import os

# Configuración de la página
st.set_page_config(page_title="PizarraCP - Tablero de Vencimientos", layout="wide")

# Título del Dashboard
st.title("📊 Pizarra de Credito Publico")
st.markdown("---")

# URL de Google Drive para el archivo Excel
URL_DRIVE = 'https://drive.google.com/uc?id=1Yx5VL5_nuGGSK5VRJsOnLPG31OaRsnfh'

# Función para cargar los datos desde un archivo Excel en Google Drive
def cargar_datos():
    try:
        # Descargar el archivo si no está disponible localmente
        if not os.path.exists("cartera.xlsx"):
            gdown.download(URL_DRIVE, "cartera.xlsx", quiet=False)
        return pd.read_excel("cartera.xlsx", sheet_name='Datos')
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Función principal para mostrar las secciones
def main():
    df = cargar_datos()
    st.markdown("## 📋 Sección 1: Metricas Generales")
    st.markdown("## 📊 Sección 2: Gráficos de Vencimientos")
    st.markdown("## 📈 Sección 3: Métricas Generales")
    st.markdown("## 🗂 Sección 4: Datos Completos")
    st.write(df)  # Muestra los datos cargados, útil para pruebas

    st.markdown("---")
    st.markdown("Desarrollado por **Manuel** | PizarraCP © 2024")

if __name__ == "__main__":
    main()

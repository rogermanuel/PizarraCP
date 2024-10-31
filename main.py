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
        
        # Verificar si el archivo fue descargado
        if os.path.exists("cartera.xlsx"):
            st.success("Archivo descargado correctamente")
        else:
            st.error("Error: El archivo no se descargó")
            return None

        # Leer el archivo Excel
        return pd.read_excel("cartera.xlsx", sheet_name='Datos')
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Función principal para mostrar las secciones
def main():
    df = cargar_datos()
    
    # Verifica si se cargaron los datos correctamente
    if df is not None:
        # Mostrar el DataFrame para diagnóstico
        st.write("Contenido del DataFrame:")
        st.write(df)
        
        # Obtener el valor de la celda A1
        if not df.empty:
            valor_a1 = df.iat[0, 0]  # iat[0, 0] accede a la primera fila y primera columna (celda A1)
            st.markdown("## 📋 Sección 1: Métricas Generales")
            st.write(f"Valor en la celda A1: {valor_a1}")  # Muestra el valor de la celda A1
        else:
            st.warning("El DataFrame está vacío. Verifica que la hoja 'Datos' tenga contenido.")
        
        # Sección 2: Gráficos de Vencimientos
        st.markdown("## 📊 Sección 2: Gráficos de Vencimientos")
        
        # Sección 3: Métricas Generales (otra parte si es necesario)
        st.markdown("## 📈 Sección 3: Métricas Grales")
        
        # Sección 4: Datos Completos
        st.markdown("## 🗂 Sección 4: Datos Completos")
        st.write(df)  # Muestra los datos cargados en la tabla completa
    
    st.markdown("---")
    st.markdown("Desarrollado por **Manuel** | PizarraCP © 2024")

if __name__ == "__main__":
    main()

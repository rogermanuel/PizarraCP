import streamlit as st
import pandas as pd
import gdown
import os

# Configuración de la página
st.set_page_config(page_title="PizarraCP - Tablero de Vencimientos", layout="wide")

# Título del Dashboard
st.title("📊 Pizarra de Créditos Públicos")
st.markdown("---")

# Estilo CSS para bordes redondeados, tamaño de los títulos, y estilo de los números
st.markdown(
    """
    <style>
    .rounded-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin-top: -10px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
        text-align: center;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .section-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        text-align: center;
        color: #333;
    }
    .metric-number {
        font-size: 50px; /* Tamaño del número */
        font-weight: bold;
        color: #2c3e50; /* Color del número */
        margin: 0;
    }
    .download-link {
        display: inline-block;
        padding: 10px 15px;
        margin: 5px;
        border-radius: 5px;
        text-decoration: none;
        background-color: #36dacd;
        color: white;
        font-weight: bold;
        text-align: center;
        width: 100%;
    }
    .download-link:hover {
        background-color: #0056b3;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Función para mostrar la Sección 1: Métricas en 6 subsecciones con números
def mostrar_metricas():
    st.header("📋 Sección 1: Métricas Generales")
    # Crear seis columnas para las subsecciones
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    # Subsección 1
    with col1:
        st.markdown('<p class="section-title">Total de Créditos</p>', unsafe_allow_html=True)
        st.markdown('<div class="rounded-box"><p class="metric-number">1500</p></div>', unsafe_allow_html=True)

    # Subsección 2
    with col2:
        st.markdown('<p class="section-title">Número de Créditos</p>', unsafe_allow_html=True)
        st.markdown('<div class="rounded-box"><p class="metric-number">320</p></div>', unsafe_allow_html=True)

    # Subsección 3
    with col3:
        st.markdown('<p class="section-title">Vencimientos Próximos</p>', unsafe_allow_html=True)
        st.markdown('<div class="rounded-box"><p class="metric-number">45</p></div>', unsafe_allow_html=True)

    # Subsección 4
    with col4:
        st.markdown('<p class="section-title">Monto Promedio</p>', unsafe_allow_html=True)
        st.markdown('<div class="rounded-box"><p class="metric-number">7500</p></div>', unsafe_allow_html=True)

    # Subsección 5
    with col5:
        st.markdown('<p class="section-title">Tasa de Ejecución</p>', unsafe_allow_html=True)
        st.markdown('<div class="rounded-box"><p class="metric-number">85%</p></div>', unsafe_allow_html=True)

    # Subsección 6
    with col6:
        st.markdown('<p class="section-title">Desviación Presupuestaria</p>', unsafe_allow_html=True)
        st.markdown('<div class="rounded-box"><p class="metric-number">10%</p></div>', unsafe_allow_html=True)

# Función para mostrar la Sección 4: Documentos de Interés en tres columnas
def mostrar_documentos():
    st.header("📂 Sección 4: Documentos de Interés")
    # Lista de documentos de interés con enlaces de descarga
    documentos = [
        {"nombre": "Informe Anual 2023", "url": "https://example.com/informe_anual_2023.pdf"},
        {"nombre": "Guía de Ejecución Presupuestaria", "url": "https://example.com/guia_ejecucion.pdf"},
        {"nombre": "Manual de Procedimientos", "url": "https://example.com/manual_procedimientos.pdf"},
        {"nombre": "Estudio de Impacto Financiero", "url": "https://example.com/estudio_impacto.pdf"},
        {"nombre": "Reglamento Interno", "url": "https://example.com/reglamento_interno.pdf"},
        {"nombre": "Plan de Desarrollo", "url": "https://example.com/plan_desarrollo.pdf"},
        {"nombre": "Informe de Sostenibilidad", "url": "https://example.com/informe_sostenibilidad.pdf"},
        {"nombre": "Evaluación de Riesgos", "url": "https://example.com/evaluacion_riesgos.pdf"},
        {"nombre": "Reporte de Actividades", "url": "https://example.com/reporte_actividades.pdf"},
    ]

    # Dividir en tres columnas y colocar un enlace en cada celda
    cols = st.columns(3)
    for i, doc in enumerate(documentos):
        with cols[i % 3]:  # Esto asegura que los enlaces se distribuyan en tres columnas
            st.markdown(f'<a href="{doc["url"]}" class="download-link" target="_blank">📄 {doc["nombre"]}</a>', unsafe_allow_html=True)

# Función principal para mostrar todas las secciones
def main():
    # Llama a la función mostrar_metricas para la Sección 1
    mostrar_metricas()

    # Sección 2: Gráficos de Vencimientos
    st.header("📊 Sección 2: Gráficos de Vencimientos")
    
    # Sección 3: Métricas Generales (otra parte si es necesario)
    st.header("📈 Sección 3: Métricas Generales")
    
    # Sección 4: Documentos de Interés
    mostrar_documentos()

    st.markdown("---")
    st.markdown("Desarrollado por **RogerManuel** | PizarraCP © 2024")

if __name__ == "__main__":
    main()

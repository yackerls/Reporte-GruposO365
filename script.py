import streamlit as st
import pandas as pd

st.set_page_config(page_title="O365 Member Checker", layout="wide")
st.title("📊 Comparador de Miembros O365")

# Sección de carga de archivos
col1, col2 = st.columns(2)
with col1:
    base_file = st.file_uploader("Cargar: exportGroupMembers (Base)", type=["csv"])
with col2:
    users_file = st.file_uploader("Cargar: users (Tenant)", type=["csv"])

if base_file and users_file:
    df_base = pd.read_csv(base_file)
    df_users = pd.read_csv(users_file)

    if st.button("Procesar Comparación"):
        # Lógica de comparación
        base_emails = set(df_base['userPrincipalName'].dropna().str.lower().unique())
        if 'mail' in df_base.columns:
            base_emails.update(df_base['mail'].dropna().str.lower().unique())

        missing = df_users[~df_users['User principal name'].str.lower().isin(base_emails)]

        # Resultados
        st.success(f"Proceso completado. Se encontraron {len(missing)} usuarios nuevos.")
        st.dataframe(missing)

        # Botón de descarga
        csv = missing.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar Reporte Faltantes", csv, "faltantes.csv", "text/csv")
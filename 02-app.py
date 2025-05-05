import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Cargar datos
df = pd.read_csv("oraciones_incendios_geolocalizado.csv")

# Configuración inicial
st.set_page_config(page_title="Visor de Incendios Edomex", layout="wide")
st.title("🔥 Visor de Incendios Forestales - Estado de México")
st.markdown("Consulta automática de noticias con palabras clave y ubicación detectada.")

# Filtros
palabra = st.selectbox("📌 Filtrar por palabra clave:", sorted(df["Palabra clave"].dropna().unique()))
fuente = st.selectbox("📰 Filtrar por fuente:", ["Todas"] + sorted(df["Fuente"].dropna().unique()))

df_filtrado = df[df["Palabra clave"] == palabra]
if fuente != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Fuente"] == fuente]

# Mostrar tabla filtrada
st.markdown(f"Se encontraron **{len(df_filtrado)}** coincidencias.")
st.dataframe(df_filtrado[["Fuente", "Fecha", "Título", "Palabra clave", "Oración", "Link"]])

# Gráfica de frecuencia de palabras clave
st.subheader("📊 Frecuencia de palabras clave")
conteo = df["Palabra clave"].value_counts().reset_index()
conteo.columns = ["Palabra clave", "Frecuencia"]

fig = px.bar(conteo, x="Palabra clave", y="Frecuencia",
             title="Cantidad de coincidencias por palabra clave",
             labels={"Frecuencia": "Número de coincidencias"},
             height=500)

st.plotly_chart(fig, use_container_width=True)

# Botón de descarga
st.download_button("📥 Descargar resultados filtrados",
                   df_filtrado.to_csv(index=False),
                   "incendios_filtrados.csv",
                   "text/csv")

# Mapa
st.subheader("🗺️ Mapa de incendios detectados por ubicación")

df_mapa = df_filtrado.dropna(subset=["Latitud", "Longitud"])
if not df_mapa.empty:
    mapa = folium.Map(location=[19.3, -99.7], zoom_start=8)
    for _, row in df_mapa.iterrows():
        folium.Marker(
            location=[row["Latitud"], row["Longitud"]],
            popup=f"{row['Lugar detectado']}<br><b>{row['Palabra clave']}</b><br><i>{row['Oración'][:100]}...</i>",
            tooltip=row["Lugar detectado"],
            icon=folium.Icon(color="red", icon="fire", prefix="fa")
        ).add_to(mapa)
    st_folium(mapa, width=1000, height=500)
else:
    st.info("No hay coordenadas disponibles para mostrar en el mapa.")

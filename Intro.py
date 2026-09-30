import streamlit as st
from PIL import Image
st.title("💻 Portafolio de Aplicaciones - Computación Avanzada")

with st.sidebar:
  st.subheader("🌐 Sobre este sitio:")
  parrafo = (
    "Esta página tiene como propósito almacenar las aplicaciones de Streamlit Cloud desarrolladas durante las sesiones" 
    "de la asignatura de Computación Avanzada presentadas por mi, Julián Ardila Castrillón."
  )
  st.write(parrafo)

st.write("A continuación encontrarás cada aplicación con su respectivo enlace para visitarla:")
col1, col2, col3, col4 = st.columns(3)

with col1:
 
 st.subheader("🚨 Detector de Anomalías: Lógica + Big-O + NumPy")
 image = Image.open('big_o.png')
 st.image(image, width=190) 
 url = "https://appbig0-clase4.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

 st.subheader("🌊 Nivel de ríos y quebradas — CORNARE")
 image = Image.open('mi_estacion_cornare.png')
 st.image(image, width=200)
 url = "https://miestacionclase6.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

 st.subheader("🌱 Explora KNN con datos de suelos de AGROSAVIA")
 image = Image.open('suelos_knn.png')
 st.image(image, width=200)
 url = "https://appsuelosknn-xk4jj7j6ffzzevt8xyeqmv.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

with col2: 
 st.subheader("🖩 Datos: preparación y estructura")
 image = Image.open('clase_datos.png')
 st.image(image, width=200)
 url = "https://clasedatos-fvan8meb2t9d5p4nbukagb.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

 st.subheader("🎯 Descenso de Gradiente Interactivo")
 image = Image.open('gradiente.png')
 st.image(image, width=190) 
 url = "https://clasegradiente-bl4nrzfsjkmzoguusvnf5w.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

 st.subheader("🍎 ¿Qué fruta es más parecida?")
 image = Image.open('frutas.png')
 st.image(image, width=200)
 url = "https://clasefruta-ejercicio.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")


with col3: 
 st.subheader("🌫️ Predictor de calidad del aire — CORNARE")
 image = Image.open('prediccion_aire.png')
 st.image(image, width=190) 
 url = "https://prediccionaire-oct94vn8qlgv3qwykrweqs.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

 st.subheader("📈 Regresión — Conceptos clave")
 image = Image.open('regresion_lineal.png')
 st.image(image, width=200)
 url = "https://claseregresionlineal.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")
 
 st.subheader("🌧️ ¿Lloverá mañana? — Regresión Logística interactiva")
 image = Image.open('regresion_logistica.png')
 st.image(image, width=200)
 url = "https://regresion-logistica.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")


with col4: 
 st.subheader("🌡️ Predictor de Sensación Térmica")
 image = Image.open('sensacion_termica.png')
 st.image(image, width=190) 
 url = "https://sensacion-termica-iot.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")

 st.subheader("🌡️ Series de Tiempo — Sensor IoT interactivo")
 image = Image.open('series_tiempo.png')
 st.image(image, width=200)
 url = "https://seriestiempo-3mkmrkkia6okaasw4zhpvi.streamlit.app/"
 st.write(f"Visítala aquí: [Enlace]({url})")
 

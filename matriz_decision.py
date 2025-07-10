import streamlit as st
st.set_page_config(page_title="Matriz de Decisión - Energía Auxiliar", layout="centered")

sistemas = ['Solar PV', 'Eólico', 'Generador', 'Baterías']
factores = ['Costo', 'Tamaño', 'Accesibilidad', 'Impacto Ambiental', 'Tipo Vivienda', 'Ubicación']

st.title("Evaluador de Sistemas Auxiliares de Energía")
st.markdown("Asignar pesos a los criterios según tus prioridades (la suma debe ser 100%)")

# Ingreso de pesos
pesos = {}
suma_pesos = 0
col1, col2 = st.columns(2)
with col1:
    for factor in factores[:3]:
        pesos[factor] = st.slider(f"Peso: {factor}", 0, 100, 10)
with col2:
    for factor in factores[3:]:
        pesos[factor] = st.slider(f"Peso: {factor}", 0, 100, 10)

suma_pesos = sum(pesos.values())
if suma_pesos != 100:
    st.error("La suma de los pesos debe ser 100%")
    st.stop()

st.markdown("---")
st.subheader("Puntajes de cada sistema por criterio (1: malo, 5: excelente)")

puntajes = {}
for sistema in sistemas:
    st.markdown(f"### {sistema}")
    puntajes[sistema] = {}
    for factor in factores:
        puntajes[sistema][factor] = st.slider(f"{factor} ({sistema})", 1, 5, 3)

st.markdown("---")
st.subheader("Resultados ponderados")

resultados = []
for sistema in sistemas:
    total = sum(puntajes[sistema][f] * pesos[f] for f in factores) / 100
    resultados.append((sistema, round(total, 2)))

resultados.sort(key=lambda x: x[1], reverse=True)

for sistema, total in resultados:
    st.success(f"**{sistema}: {total} puntos**")

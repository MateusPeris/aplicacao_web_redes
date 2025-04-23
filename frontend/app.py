import streamlit as st
import requests
import pandas as pd
import altair as alt

# BACKEND_URL = "http://host.docker.internal:5000"

BACKEND_URL = "http://localhost:5000"

st.title("Monitoramento de Tráfego de Rede")

with st.form("registro_form"):
    ip = st.text_input("Endereço IP")
    nome = st.text_input("Nome")
    taxa = st.number_input("Taxa de Tráfego (Mbps)", min_value=0.0)
    if st.form_submit_button("Registrar"):
        requests.post(f"{BACKEND_URL}/dispositivos", json={"ip": ip, "nome": nome, "taxa": taxa})
        st.success("Dispositivo registrado!")

st.subheader("Dispositivos Registrados")
resposta = requests.get(f"{BACKEND_URL}/dispositivos")
dados = resposta.json()
df = pd.DataFrame(dados, columns=["ID", "IP", "Nome", "Taxa"])

def status(t):
    return "Alto" if t >= 50 else "Normal"

df["Status"] = df["Taxa"].apply(status)
# st.bar_chart(df.set_index("Nome")["Taxa"])

chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("Nome:N", axis=alt.Axis(labels=True, title=None, labelAngle=0)),
    y=alt.Y("Taxa:Q", axis=alt.Axis(title=None)),
    tooltip=["Nome", "Taxa", "Status"]
).properties(
    width=600,
    height=400,
    title="Taxa de Tráfego por Dispositivo"
)

st.altair_chart(chart, use_container_width=True)

# Definir o status com base na taxa
def calcular_status(taxa):
    if taxa < 10:
        return "Baixa"
    elif taxa < 50:
        return "Normal"
    else:
        return "Alta"

df["Status"] = df["Taxa"].apply(calcular_status)

# Filtro por status
status_filtro = st.selectbox("Filtrar por status", ["Todos", "Baixa", "Normal", "Alta"])
if status_filtro != "Todos":
    df = df[df["Status"] == status_filtro]

st.markdown("### Lista de Dispositivos")

# Cabeçalho
cols = st.columns([2, 3, 2, 2, 2])
cols[0].markdown("**Endereço IP**")
cols[1].markdown("**Nome**")
cols[2].markdown("**Taxa de Tráfego (Mbps)**")
cols[3].markdown("**Status**")
cols[4].markdown("**Ação**")

# Cores para status
cor_status = {
    "Normal": "#339900",   # verde
    "Alta": "#cc3300",     # vermelho
    "Baixa": "#ffcc00"     # amarelo
}

# Linhas com destaque de status
for _, row in df.iterrows():
    cols = st.columns([2, 3, 2, 2, 2])
    cols[0].markdown(row["IP"])
    cols[1].markdown(row["Nome"])
    cols[2].markdown(f'{row["Taxa"]:.2f}')
    
    # Aplicar cor de fundo no status
    cor = cor_status.get(row["Status"], "#ffffff")
    cols[3].markdown(f"<div style='background-color:{cor}; padding:4px; border-radius:5px; text-align:center'>{row['Status']}</div>", unsafe_allow_html=True)
    
    if cols[4].button("Remover", key=f"remover_{row['ID']}"):
        requests.delete(f"{BACKEND_URL}/dispositivos/{row['ID']}")
        st.rerun()


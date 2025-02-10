import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Carregando os dados
file = 'anxiety.csv'  
df = pd.read_csv(file)

st.set_page_config(layout="wide")

# Título
st.markdown("<h1 style='font-size: 32px;'>📊 Ansiedade e seus Fatores</h1>", unsafe_allow_html=True)
st.markdown("Uma análise dos impactos de diferentes fatores na ansiedade. Explore os gráficos abaixo para entender melhor!")

# Sidebar com faixas etárias
st.sidebar.title("Faixas etárias")
faixas_etarias = {
    "18-30": (18, 30),
    "31-40": (31, 40),
    "41-50": (41, 50),
    "51-60": (51, 60),
    "61+": (61, df["Age"].max())
}

faixas_selecionadas = [faixas_etarias[faixa] for faixa in faixas_etarias if st.sidebar.checkbox(faixa, value=True)]

df_filtrado = df.copy()
if faixas_selecionadas:
    df_filtrado = df_filtrado[df_filtrado["Age"].between(*faixas_selecionadas[0])]
    for faixa in faixas_selecionadas[1:]:
        df_filtrado = pd.concat([df_filtrado, df[df["Age"].between(*faixa)]])

# Renomeando colunas para português
rename_dict = {
    "Age": "Idade",
    "Gender": "Gênero",
    "Occupation": "Profissão",
    "Sleep Hours": "Horas de Sono",
    "Physical Activity (hrs/week)": "Atividade Física (hrs/semana)",
    "Caffeine Intake (mg/day)": "Consumo de Cafeína (mg/dia)",
    "Alcohol Consumption (drinks/week)": "Consumo de Álcool (drinks/semana)",
    "Smoking": "Fumante",
    "Family History of Anxiety": "Histórico Familiar de Ansiedade",
    "Stress Level (1-10)": "Nível de Estresse (1-10)",
    "Heart Rate (bpm during attack)": "Frequência Cardíaca (bpm durante ataque)",
    "Breathing Rate (breaths/min)": "Frequência Respiratória (respirações/min)",
    "Sweating Level (1-5)": "Nível de Suor (1-5)",
    "Dizziness": "Tontura",
    "Medication": "Medicação",
    "Therapy Sessions (per month)": "Sessões de Terapia (por mês)",
    "Recent Major Life Event": "Evento de Vida Recente",
    "Diet Quality (1-10)": "Qualidade da Dieta (1-10)",
    "Severity of Anxiety Attack (1-10)": "Severidade do Ataque de Ansiedade (1-10)"
}
df_filtrado.rename(columns=rename_dict, inplace=True)

df_filtrado["Gênero"].replace({"Male": "Masculino", "Female": "Feminino", "Other": "Outro"}, inplace=True)

# Criando colunas para exibição
col1, col2 = st.columns(2)
colu1, colu2 = st.columns(2)

# Gráfico de distribuição de gênero
genero = df_filtrado["Gênero"].value_counts()
fig_genero = go.Figure(data=[go.Pie(labels=genero.index, values=genero.values, textinfo='percent')])
fig_genero.update_layout(title="Distribuição de Gênero", title_x=0.3)

# Profissões que mais causam ansiedade
trabalho = df_filtrado["Profissão"].value_counts()
fig_trabalho = go.Figure(data=[go.Bar(x=trabalho.index, y=trabalho.values)])
fig_trabalho.update_layout(title="Profissões que Mais Causam Ansiedade", xaxis_title="Profissão", yaxis_title="Quantidade", title_x=0.3)

# Correlação entre fatores e ansiedade
fatores = ["Consumo de Cafeína (mg/dia)", "Horas de Sono", "Atividade Física (hrs/semana)", "Qualidade da Dieta (1-10)", "Consumo de Álcool (drinks/semana)", "Severidade do Ataque de Ansiedade (1-10)"]
df_fatores = df_filtrado[fatores].dropna()
fig_corr = go.Figure(data=go.Heatmap(z=df_fatores.corr().values, x=df_fatores.columns, y=df_fatores.columns, colorscale='RdBu'))
fig_corr.update_layout(title="Correlação Entre Fatores e Ansiedade", title_x=0.3)

# Radar Chart para impacto dos fatores

# Normalizando corretamente os fatores com base nos valores reais do dataset
df_norm = (df_fatores - df_fatores.min()) / (df_fatores.max() - df_fatores.min())
fatores_media = df_norm.mean()

# Convertendo para listas para evitar problemas na visualização
labels = fatores_media.index.tolist()
valores = fatores_media.tolist()

# Criando os ângulos para o radar chart
angles = [n / float(len(labels)) * 2 * np.pi for n in range(len(labels))]
angles += angles[:1]  # Fechando o gráfico

# Ajustando os valores para o radar chart
valores += valores[:1]  # Fechando o loop do radar chart

# Criando o gráfico de radar
fig_radar = go.Figure(data=[
    go.Scatterpolar(
        r=valores,
        theta=labels + [labels[0]],  # Fechando o gráfico
        fill='toself'
    )
])
fig_radar.update_layout(title="Impacto dos Fatores na Ansiedade", title_x=0.3)

# Exibindo os gráficos
col1.plotly_chart(fig_genero)
col2.plotly_chart(fig_trabalho)
colu1.plotly_chart(fig_corr)
colu2.plotly_chart(fig_radar)

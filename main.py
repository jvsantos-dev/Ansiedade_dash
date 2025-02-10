import numpy as np
import base64
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Carregando os dados
file = 'anxiety.csv'  
df = pd.read_csv(file)

st.set_page_config(layout="wide")
# Remover fundo de imagem
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;  /* Fundo branco */
}

[data-testid="stSidebar"] {
    background-color: #1e1e1e;  /* Fundo preto para a sidebar */
}

header, .css-1d391kg, .css-1kxg7xu {
    visibility: hidden;
}

body {
    color: black;  /* Texto preto */
    text-align: center;
}

.stTextInput input {
    color: black;
    background-color: transparent;
    border: 1px solid black;
}

.stTextInput input:focus {
    border-color: lightblue;
}
</style>
""", unsafe_allow_html=True)

# Usando Markdown para título e definindo o tamanho da fonte
st.markdown("<h1 style='font-size: 32px;'>📊 Ansiedade e seus Fatores</h1>", unsafe_allow_html=True)
st.markdown("Uma análise dos impactos de diferentes fatores na ansiedade. Explore os gráficos abaixo para entender melhor!")
col1, col2 = st.columns(2)
colu1, colu2 = st.columns(2)
# Mapeando os gêneros
substituicoes = {"Male": "Masculino", "Female": "Feminino", "Other": "Outro"}
df['Gender'] = df['Gender'].map(substituicoes)

# Distribuição de Gênero
genero = df['Gender'].value_counts()
fig_genero = go.Figure(data=[go.Pie(labels=genero.index, values=genero.values, textinfo='percent', 
                                    marker=dict(colors=['#CB80AB', '#3F3AE6', '#64E66D']))])
fig_genero.update_layout(title="Distribuição de Gênero", title_font_size=24, title_x=0.5, 
                            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(size=18))


# Profissões que Mais Causam Ansiedade
trabalho = df['Occupation'].value_counts()
fig_trabalho = go.Figure(data=[go.Bar(x=trabalho.index, y=trabalho.values, 
                                      marker=dict(color=['#E63946', '#F4A261', '#2A9D8F', '#264653', '#8E44AD']))])
fig_trabalho.update_layout(title="Profissões que Mais Causam Ansiedade", title_font_size=24, title_x=0.5,
                            xaxis_title="Profissão", yaxis_title="Quantidade", font=dict(size=18), 
                            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

# Correlação Entre Fatores e Ansiedade
fatores = ['Caffeine Intake', 'Sleep Hours', 'Physical Activity (hrs/week)', 'Diet Quality (1-10)', 
           'Alcohol Consumption (drinks/week)', 'Severity of Anxiety Attack (1-10)']

# Filtrar colunas existentes
df_fatores = df[[col for col in fatores if col in df.columns]]
fig_corr = go.Figure(data=go.Heatmap(z=df_fatores.corr().values, x=df_fatores.columns, y=df_fatores.columns,
                                     colorscale='RdBu', colorbar=dict(title="Correlação", tickvals=[-1, 0, 1])))
fig_corr.update_layout(title="Correlação Entre Fatores e Ansiedade", title_font_size=24, title_x=0.5)

# Impacto dos Fatores na Ansiedade
fatores_existentes = [col for col in fatores if col in df.columns]
fatores_media = df[fatores_existentes].mean()
fatores_norm = (fatores_media - fatores_media.min()) / (fatores_media.max() - fatores_media.min())
labels = fatores_existentes
num_vars = len(labels)
angles = [n / float(num_vars) * 2 * np.pi for n in range(num_vars)]
angles += angles[:1]

fig_radar = go.Figure(data=[go.Scatterpolar(r=fatores_norm.tolist() + fatores_norm.tolist()[:1], 
                                            theta=labels + [labels[0]], fill='toself', line=dict(color='red'))])
fig_radar.update_layout(title="Impacto dos Fatores na Ansiedade", title_font_size=24, title_x=0.5, 
                        polar=dict(radialaxis=dict(showline=False, ticks='', tickvals=[], ticktext=[], visible=False)), 
                        font=dict(size=18), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

# Exibindo os gráficos
colu1.plotly_chart(fig_radar)
colu2.plotly_chart(fig_corr)
col2.plotly_chart(fig_trabalho)
col1.plotly_chart(fig_genero)
st.sidebar.title("Faixas etárias")

df = df.sort_values(df['Age'])
faixas_etarias = {
    "18-30": (18, 30),
    "31-40": (31, 40),
    "41-50": (41, 50),
    "51-60": (51, 60),
    "61+": (61, df["Age"].max())
}
faixas_selecionadas = []


for faixa, (idade_min, idade_max) in faixas_etarias.item():
    if st.sidebar.checkbox(faixa, valor=True):
        faixas_selecionadas.append((idade_min, idade_max))
# Idade Média por Gênero
media_idades_por_genero = df.groupby('Gender')['Age'].mean()
fig_idade = go.Figure(data=[go.Bar(x=media_idades_por_genero.index, y=media_idades_por_genero.values, 
                                   marker=dict(color=['#6495ED', '#FF69B4']))])
fig_idade.update_layout(title="Idade Média por Gênero", title_font_size=24, title_x=0.5, 
                        xaxis_title="Gênero", yaxis_title="Idade", font=dict(size=18), 
                        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
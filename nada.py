# Radar Chart para impacto dos fatores
fatores_media = df_fatores_norm.mean()

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

Análise de Ansiedade e Seus Fatores

Este projeto oferece uma análise dos impactos de diferentes fatores na ansiedade, permitindo explorar dados sobre o consumo de cafeína, horas de sono, atividade física, entre outros. O painel interativo foi desenvolvido usando Streamlit e inclui gráficos interativos para facilitar a visualização das relações entre variáveis, como a distribuição de gênero, profissões que mais causam ansiedade, correlação entre fatores e a severidade do ataque de ansiedade, além de um gráfico de radar para entender o impacto dos fatores na ansiedade.
Tecnologias Utilizadas

    Python
    Streamlit - Para criar a interface interativa.
    Plotly - Para visualizações gráficas interativas.
    Pandas - Para manipulação e análise de dados.
    NumPy - Para operações numéricas.
    Scikit-learn - Para normalização dos dados.

Funcionalidades

    Faixas Etárias: O usuário pode selecionar faixas etárias específicas para filtrar os dados.
    Distribuição de Gênero: Gráfico de pizza que exibe a distribuição de gênero na base de dados.
    Profissões que Causam Ansiedade: Gráfico de barras que mostra as profissões que mais causam ansiedade.
    Correlação Entre Fatores e Ansiedade: Um gráfico de calor (heatmap) que apresenta a correlação entre diferentes fatores (como consumo de cafeína, horas de sono, etc.) e a severidade do ataque de ansiedade.
    Radar Chart: Exibe o impacto médio de cada fator na ansiedade por meio de um gráfico de radar.

Como Rodar

    Instalar dependências: Para rodar este projeto, instale as dependências usando o pip:

pip install pandas numpy plotly scikit-learn streamlit

Executar o aplicativo: No terminal, navegue até o diretório onde o script está localizado e execute:

    streamlit run app.py

    Visualizar o aplicativo: O aplicativo será executado em um servidor local. Abra o navegador e acesse o endereço fornecido no terminal (geralmente http://localhost:8501).

Estrutura dos Dados

O dataset utilizado contém informações sobre os seguintes fatores:

    Idade: Idade do participante.
    Gênero: Gênero do participante (Masculino, Feminino, Outro).
    Profissão: Profissão do participante.
    Horas de Sono: Quantidade de horas de sono por noite.
    Atividade Física (hrs/semana): Horas de atividade física por semana.
    Consumo de Cafeína (mg/dia): Quantidade de cafeína consumida por dia em miligramas.
    Consumo de Álcool (drinks/semana): Quantidade de bebidas alcoólicas consumidas por semana.
    Fumante: Indicação se a pessoa fuma ou não.
    Histórico Familiar de Ansiedade: Se há histórico familiar de ansiedade.
    Nível de Estresse (1-10): Nível de estresse do participante em uma escala de 1 a 10.
    Frequência Cardíaca (bpm durante ataque): Frequência cardíaca durante um ataque de ansiedade.
    Frequência Respiratória (respirações/min): Frequência respiratória durante um ataque de ansiedade.
    Nível de Suor (1-5): Nível de suor durante um ataque de ansiedade.
    Tontura: Indicação se o participante experimenta tontura.
    Medicação: Indicação se o participante faz uso de medicação.
    Sessões de Terapia (por mês): Número de sessões de terapia realizadas por mês.
    Evento de Vida Recente: Se o participante teve um evento de vida recente significativo.
    Qualidade da Dieta (1-10): Qualidade percebida da dieta em uma escala de 1 a 10.
    Severidade do Ataque de Ansiedade (1-10): Severidade de um ataque de ansiedade em uma escala de 1 a 10.

Contribuições

Se você quiser contribuir com este projeto, fique à vontade para abrir uma issue ou enviar um pull request.
Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.

# 🎧 Spotify Insight AI

Uma aplicação interativa de análise de dados musicais construída com Python e Streamlit, simulando um produto de **analytics estilo SaaS** para exploração de dados do Spotify.

---

## 🚀 Demonstração

O projeto permite explorar dados musicais com filtros interativos, visualizações e recomendações automáticas de músicas com base em popularidade e gênero.

---

## 📊 Funcionalidades

- 🎛 Filtros interativos por gênero e popularidade
- 📈 KPIs em tempo real (total de músicas, média de popularidade, taxa de hits)
- 🎤 Top artistas por volume de músicas
- 🎧 Distribuição de popularidade das músicas
- 🎶 Visão de mercado por gênero musical
- 🤖 Sistema de recomendação simples baseado em popularidade
- 📋 Visualização completa do dataset filtrado

---

## 🧠 Insights Gerados

A aplicação permite responder perguntas como:

- Quais gêneros são mais populares?
- Quais artistas dominam o catálogo?
- Como a popularidade das músicas se distribui?
- Quais músicas têm maior chance de serem hits?

---

## 🛠️ Tecnologias Utilizadas

- Python 🐍
- Pandas 📊
- Matplotlib 📈
- Seaborn 🎨
- Streamlit 🌐

---

## 📂 Estrutura do Projeto


spotify-etl/
│
├── dashboard_spotify.py # Dashboard principal (Streamlit)
├── spotify_tratado.csv # Base de dados tratada
├── etl_spotify.py # Pipeline ETL (opcional)
└── README.md # Documentação do projeto

---

## ▶️ Como executar o projeto

### 1. Instalar dependências

```bash
pip install pandas matplotlib seaborn streamlit
2. Rodar o dashboard
streamlit run dashboard_spotify.py


👨‍💻 Autor Ágata Oliveira
Projeto desenvolvido com foco em portfólio de Data Science e análise de dados.

🤝 Créditos: Este projeto foi desenvolvido com apoio de IA (ChatGPT - OpenAI) para estruturação, análise e design do dashboard.
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIGURAÇÃO
# =========================

st.set_page_config(
    page_title="Spotify Insight AI",
    page_icon="🎧",
    layout="wide"
)

sns.set_theme(style="darkgrid")

# =========================
# DADOS
# =========================

df = pd.read_csv("spotify_tratado.csv")
df["hit"] = df["popularity"] >= 60

# =========================
# SIDEBAR (FILTRO INTELIGENTE)
# =========================

st.sidebar.title("🎛 Control Panel")

generos_disponiveis = sorted(df["genre"].unique())

generos_selecionados = st.sidebar.multiselect(
    "Select genres (optional)",
    generos_disponiveis,
    default=[]
)

min_pop = st.sidebar.slider("Min Popularity", 0, 100, 0)

# lógica: se não selecionar nada, usa todos os gêneros
if len(generos_selecionados) == 0:
    df_filtrado = df
else:
    df_filtrado = df[df["genre"].isin(generos_selecionados)]

df_filtrado = df_filtrado[df_filtrado["popularity"] >= min_pop]

# =========================
# HEADER
# =========================

st.title("🎧 Spotify Insight AI")
st.caption("Music intelligence platform for data-driven insights")

st.divider()

# =========================
# KPIs
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Tracks", len(df_filtrado))
col2.metric("Avg Popularity", round(df_filtrado["popularity"].mean(), 2))
col3.metric("Hits", int(df_filtrado["hit"].sum()))
col4.metric("Success Rate", f"{round(df_filtrado['hit'].mean()*100, 1)}%")

st.divider()

# =========================
# INSIGHT AUTOMÁTICO
# =========================

hit_rate = df_filtrado["hit"].mean()

if hit_rate > 0.6:
    insight = "🔥 High-performing dataset: strong hit concentration."
elif hit_rate > 0.3:
    insight = "📊 Moderate performance across selected data."
else:
    insight = "📉 Low hit concentration in this selection."

st.subheader("🧠 AI Insight")
st.info(insight)

st.divider()

# =========================
# 📊 GRÁFICOS PRINCIPAIS (3 VISUALIZAÇÕES)
# =========================

st.subheader("📊 Key Analytics")

col1, col2 = st.columns(2)

# 🎤 TOP ARTISTS
with col1:
    st.markdown("### 🎤 Top Artists")

    top_artists = df_filtrado["artist_name"].value_counts().head(10).sort_values()

    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=top_artists.values, y=top_artists.index, ax=ax)

    ax.set_xlabel("Tracks")

    st.pyplot(fig)

# 📊 POPULARITY DISTRIBUTION
with col2:
    st.markdown("### 📊 Popularity Distribution")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(df_filtrado["popularity"], bins=20, kde=True, ax=ax)

    ax.set_xlabel("Popularity")

    st.pyplot(fig)

# 🎧 TOP GENRES (RESTO DA TELA)
st.markdown("### 🎧 Market Overview (Genres)")

top_genres = df_filtrado["genre"].value_counts().head(10).sort_values()

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index, ax=ax)

ax.set_xlabel("Tracks")
ax.set_ylabel("Genre")

st.pyplot(fig)

st.divider()

# =========================
# 🎧 RECOMENDAÇÃO
# =========================

st.subheader("🎧 Recommended Songs for You")

mean_pop = df_filtrado["popularity"].mean()

recommendations = df_filtrado[
    df_filtrado["popularity"] >= mean_pop
].sort_values("popularity", ascending=False).head(10)

st.dataframe(
    recommendations[["artist_name", "track_name", "genre", "popularity"]],
    use_container_width=True
)

st.divider()

# =========================
# 📋 DATASET FINAL
# =========================

st.subheader("📋 Dataset Preview")

st.dataframe(
    df_filtrado.sort_values("popularity", ascending=False),
    use_container_width=True
)

st.divider()

# =========================
# FOOTER
# =========================

st.caption(
    "Spotify Insight AI • Developed by Ágata Oliveira • Powered by Data Science & AI 🎧"
)
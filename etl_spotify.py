import pandas as pd

# =========================
# EXTRAÇÃO
# =========================

df = pd.read_csv("SpotifyFeatures.csv")

print("Base original:")
print(df.head())

# =========================
# TRANSFORMAÇÃO
# =========================

# Remover músicas duplicadas
df = df.drop_duplicates(subset=["track_name", "artist_name"])

# Selecionar colunas importantes
df = df[
    [
        "genre",
        "artist_name",
        "track_name",
        "popularity",
        "danceability",
        "energy",
        "tempo",
        "valence"
    ]
]

# Filtrar músicas com popularidade acima de 50
df = df[df["popularity"] > 50]

# Criar classificação de popularidade
def classificar_popularidade(pop):
    if pop >= 80:
        return "Hit Mundial"
    elif pop >= 65:
        return "Muito Popular"
    else:
        return "Popular"

df["categoria_popularidade"] = df["popularity"].apply(classificar_popularidade)

# =========================
# RESULTADO
# =========================

print("\nBase transformada:")
print(df.head())

print("\nQuantidade de músicas:")
print(len(df))

# =========================
# CARREGAMENTO
# =========================

df.to_csv("spotify_tratado.csv", index=False)

print("\nArquivo 'spotify_tratado.csv' salvo com sucesso!")


import pandas as pd

ratings = pd.read_csv("database/ratings.csv", nrows=5000)
movies  = pd.read_csv("database/movies_metadata.csv", nrows=5000)

movies['id'] = pd.to_numeric(movies['id'], errors='coerce')
movies = movies.dropna(subset=['id']) 
movies['id'] = movies['id'].astype(int)

# Filtra apenas avaliações positivas (rating >= 4.0)
ratings_filtrados = ratings[ratings['rating'] >= 4.0]

df = ratings_filtrados.merge(movies[['id', 'title']], left_on='movieId', right_on='id')

# Agrupa por usuário e cria lista de filmes assistidos/avaliados positivamente
def processar_dados():
    global cesta_usuarios
    cesta_usuarios = df.groupby('userId')['title'].apply(list)

processar_dados()

# Exibe exemplo
pd.set_option('display.max_row', None)
print(cesta_usuarios)

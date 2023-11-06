import pandas as pd


arq_actors = pd.read_csv("actors.csv", sep=",")
actor_max_films = arq_actors.loc[arq_actors["Number of Movies"].idxmax(), "Actor"]
qtd_films = arq_actors["Number of Movies"].max()
print(f"O(a) Ator/Atriz com maior quantidade de filmes é: {actor_max_films} com {qtd_films} filmes.")

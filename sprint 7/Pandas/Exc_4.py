import pandas as pd

arq_actors = pd.read_csv("actors.csv", sep=",")
name_films = arq_actors["#1 Movie"].value_counts()
indice_max_movie = name_films.idxmax()
count_max_movie = name_films.loc[indice_max_movie]
print(f"O filme com maior frequência é o {indice_max_movie} sendo exibido {count_max_movie} vezes.")

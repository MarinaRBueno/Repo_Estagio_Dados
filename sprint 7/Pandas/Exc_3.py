
import pandas as pd


arq_actors = pd.read_csv("actors.csv", sep=",")
mean_actors = arq_actors[["Actor", "Average per Movie"]]
average_per_movie = arq_actors["Average per Movie"]
value_max_average_per_movie = average_per_movie.max()
actor_average_per_movie = arq_actors.loc[arq_actors["Average per Movie"].idxmax(), "Actor"]
print(f"O ator/atriz com maior média por filme é {actor_average_per_movie} com o valor de {value_max_average_per_movie}.")

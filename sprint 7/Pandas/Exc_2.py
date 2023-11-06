import pandas as pd

arq_actors = pd.read_csv("actors.csv", sep=",")
number_of_movies = arq_actors["Number of Movies"]
column_average_number_of_movies = number_of_movies.mean()
print(f"A média da coluna Number of Movies é de: {column_average_number_of_movies}")

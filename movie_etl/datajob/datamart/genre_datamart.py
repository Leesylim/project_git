from infra.jdbc import DataMart, DataWarehouse, find_data, save_data
from pyspark.sql.functions import col, ceil


class Genre:
    @classmethod
    def save(cls):
        genre = find_data(DataWarehouse,'MOVIE_GENRE')
        movie  = find_data(DataMart,'MOVIE')

    genre_join = genre.join(movie, on='MOVIE_CODE')

    genre = genre_join.select(genre_join.MOVIE_CODE
                                ,genre_join.GENRE_NAME
                                ,genre_join.HIT_GRADE)

    save_data(DataMart,genre,'GENRE')
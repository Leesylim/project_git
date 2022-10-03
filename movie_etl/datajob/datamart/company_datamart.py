from infra.jdbc import DataMart, DataWarehouse, find_data, save_data
from pyspark.sql.functions import col, ceil


class Company:
    @classmethod
    def save(cls):
        company = find_data(DataWarehouse,'COMPANY')
        movie  = find_data(DataMart,'MOVIE')

    company_join = company.join(movie, on='MOVIE_CODE')

    company = company_join.select(company_join.MOVIE_CODE
                                ,company_join.COMPANY_NAME
                                ,company_join.COMPANY_TYPE
                                ,company_join,HIT_GRADE)

    save_data(DataMart,company,'COMPANY')
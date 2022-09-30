from pyspark.sql.functions import col
from infra.jdbc import DataWarehouse,save_data
from infra.spark_session import get_spark_session
from datetime import datetime, timedelta



class DailyBoxOfficeTransformer:

    @classmethod
    def std_day(cls, time_day) :
        x = datetime.now() - timedelta(time_day)
        year = x.year
        month = x.month if x.month >= 10 else '0' + str(x.month)
        day = x.day if x.day >= 10 else '0' + str(x.day)
        return str(year) + '-' + str(month) + '-' + str(day)
    
    
    @classmethod  #데이터 HDFS에서 읽어오기
    def transform(cls):
        path = '/movie/daily_box_office/daliy_box_office_' + cls.std_day(1) + '.json'
        print(path)
        office_json = get_spark_session().read.json(path, encoding='UTF-8')
        office_json.show()





        














# class DailyBoxOfficeTransformer:
    
#     # MOVIECD = '20215601'

#     @classmethod
#     def transform(cls):
#         box_office_df = find_data(DataWarehouse, 'DAILY_BOX_OFFICE')
#         movie_code_list = box_office_df.select('MOVIE_CODE').rdd.flatMap(lambda x: x).collect()
#         movie_code_list = np.unique(movie_code_list)

#         path = '/movie_data/detail/movie_detail_' + movie_code_list[0] + '.json'
#         movie_json = get_spark_session().read.json(path, encoding='UTF-8')
#         tmp = movie_json.select('movieInfoResult.movieInfo').first()
#         df_movie = get_spark_session().createDataFrame(tmp)

#         df_movie_select = df_movie.select('movieCd', 'movieNm', 'prdtYear', 'showTm', 'openDt', 'typeNm', 'nations', 'directors', 'audits')
        
#         dump_df = df_movie_select.withColumn('nations', col('nations')[0].nationNm) \
#                                 .withColumn('directors', col('directors')[0].peopleNm) \
#                                 .withColumn('audits', col('audits')[0].watchGradeNm)
#         tmp_df = dump_df

#         for i in range(1, len(movie_code_list)):
#             path = '/movie_data/detail/movie_detail_' + movie_code_list[i] + '.json'
#             movie_json = get_spark_session().read.json(path, encoding='UTF-8')
#             tmp = movie_json.select('movieInfoResult.movieInfo').first()
#             df_movie = get_spark_session().createDataFrame(tmp)

#             df_movie_select = df_movie.select('movieCd', 'movieNm', 'stdDate', 'rank', 'salesAmt', 'salesShare', 'audiCnt', 'scrnCnt', 'showCnt')
            
#             dump_df = df_movie_select.withColumn('nations', col('nations')[0].nationNm) \
#                                     .withColumn('directors', col('directors')[0].peopleNm) \
#                                     .withColumn('audits', col('audits')[0].watchGradeNm)

#             tmp_df = tmp_df.union(dump_df).distinct()

#         daily_box_offce_df = tmp_df.withColumnRenamed('movieCd', 'MOVIE_CODE') \
#                                 .withColumnRenamed('movieNm', 'MOVIE_NAME') \
#                                 .withColumnRenamed('stdDate', 'STD_DATE') \
#                                 .withColumnRenamed('rank', 'RANK') \
#                                 .withColumnRenamed('salesAmt', 'SALES_AMT') \
#                                 .withColumnRenamed('salesShare', 'SALES_SHARE') \
#                                 .withColumnRenamed('audiCnt', 'AUDI_CNT') \
#                                 .withColumnRenamed('scrnCnt', 'SCRN_CNT') \
#                                 .withColumnRenamed('showCnt', 'SHOW_CNT')
#         daily_box_offce_df.show()

#         # d = df_movie.select('genres')
#         # d.show()
#         # d.withColumn('genres', col('genres')[0].genreNm).show()

#         save_data(DataWarehouse, daily_box_offce_df, 'DAILY_BOXOFFICE')

import unittest

from datajob.etl.extract.movie_score import MovieScoreExtractor
from datajob.etl.transform.daily_box_offce_transform import DailyBoxOfficeTransformer

class MTest(unittest.TestCase):
    # def test1(self):
    #     NaverSearchMovieExtractor.extract_data()

    def test1(self):
        MovieScoreExtractor.extract_data()

    def test2(self):
        DailyBoxOfficeTransformer.transform()



if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()

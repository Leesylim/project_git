import unittest
from datajob.datamart.company_datamart import Company
from datajob.datamart.genre_datamart import Genre
from datajob.etl.extract.daily_box_office_api import DailyBoxOfficeExtractor
from datajob.etl.transform.daily_box_offce_transform import DailyBoxOfficeTransformer


class MTest(unittest.TestCase):
    def test1(self):
        DailyBoxOfficeExtractor.extract_data(100)

    def test2(self):
        DailyBoxOfficeTransformer.transform()

    def test3(self):
        Genre.save()

    def test4(self):
        Company.save()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()




















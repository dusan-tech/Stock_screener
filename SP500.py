import os
import pandas_datareader.data as web
import datetime
import pandas as pd


class SP500:
    def __init__(self):
        """

        """

    def sp500(self):
        """

        :return:
        """

        start = datetime.datetime(2010, 1, 1)
        end = datetime.datetime(2020, 1, 27)

        sp500 = web.DataReader(['sp500'], 'fred', start, end)

        print(sp500)

        return sp500


if __name__ == "__main__":
    obj_sp500 = SP500()
    obj_sp500.sp500()
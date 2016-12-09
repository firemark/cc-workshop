import csv
from datetime import datetime
import sqlite3

temp_stats = {'abs_max': None, 'abs_min': None, 'abs_avg': None}

db = sqlite3.connect('temp.db')
db.execute('''
DROP TABLE IF EXISTS `measures`;
''')
db.execute('''CREATE TABLE IF NOT EXISTS measures (
    meas_time INT PRIMARY KEY,
    temp NUMERIC,
    humidity NUMERIC,
    pressure NUMERIC
);''')

db_insert_query = "INSERT INTO measures (meas_time, temp, humidity, pressure) VALUES ('{}','{}','{}','{}');"

CSV_YEAR = 0
CSV_MONTH = 1
CSV_DAY = 2
CSV_HOUR = 3
CSV_MINUTE = 4
CSV_TEMP = 5
CSV_RH = 6
CSV_PRESS = 7


def dp(t, h):
    """
    calculates the dewpoint via the formula from weatherwise.org

    :type t: float
    :param t: temperature
    :param h: humidity
    :return: dew point
    """
    x = 1 - 0.01 * h;

    dew_point = (14.55 + 0.114 * t) * x
    dew_point += ((2.5 + 0.007 * t) * x) ** 3
    dew_point += (15.9 + 0.117 * t) * x ** 14
    dew_point = t - dew_point

    return dew_point


# that might be a weather station device, not a file
with open('history_export_2016-12-05T11-55-25.csv', 'rb') as csvfile:
    weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
    # skip header
    next(weather_station, None)

    # process data
    for data_row in weather_station:

        # first entry for absolute max / min
        if temp_stats['abs_max'] is None:
            temp_stats['abs_max'] = data_row[CSV_TEMP]
            temp_stats['abs_min'] = data_row[CSV_TEMP]
            temp_stats['abs_avg'] = float(data_row[CSV_TEMP])
        # update max / min
        else:
            temp_stats['abs_max'] = temp_stats['abs_max'] if (temp_stats['abs_max'] >= data_row[CSV_TEMP]) else \
                data_row[CSV_TEMP]
            temp_stats['abs_min'] = temp_stats['abs_min'] if (temp_stats['abs_min'] <= data_row[CSV_TEMP]) else \
                data_row[CSV_TEMP]
            temp_stats['abs_avg'] = (float(data_row[CSV_TEMP]) + temp_stats['abs_avg']) / 2

        measured_day = datetime(int(data_row[CSV_YEAR]), int(data_row[CSV_MONTH]),
                                int(data_row[CSV_DAY]), int(data_row[CSV_HOUR]), int(data_row[CSV_MINUTE]))

        query = db_insert_query.format(measured_day, data_row[CSV_TEMP], data_row[CSV_RH], data_row[CSV_PRESS])
        db.execute(query)
        db.commit()

        dew_point = dp(float(data_row[CSV_TEMP]), float(data_row[CSV_RH]))

        print "curr: {}, max: {}, min: {}, avg: {}, rh: {}, dp: {}".format(data_row[CSV_TEMP], temp_stats['abs_max'],
                                                                           temp_stats['abs_min'], temp_stats['abs_avg'],
                                                                           data_row[CSV_RH], dew_point)




        # calculate dew point

    db.close()

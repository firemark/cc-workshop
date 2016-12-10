import csv
import json
from datetime import datetime
import sqlite3

options = {
    'db': True,
    'out_html': False,
    'out_raw': True,
    'in_json': False,
    'in_csv': True,
}

def database_start():
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
    return db

db_insert_query = "INSERT INTO measures (meas_time, temp, humidity, pressure) VALUES ('{}','{}','{}','{}');"

def dew_point(t, h):
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
def data_load(file_name):
    csvfile=open(file_name, 'r')
    if options['in_csv']:
        weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
        # skip header
        next(weather_station, None)
    elif options['in_json']:
        weather_station = json.loads(csvfile.read())['data']
    return weather_station
import csv
import sqlite3
import json
from datetime import datetime
from db_inity import db_init
from calculate_temp import dp
#from sources import csv
from options import *
if options['db']:

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

if options['out_html']:
    print '<table>'


# that might be a weather station device, not a file
with open('history_export_2016-12-05T11-55-25.csv', 'rw') as csvfile:
    if options['in_csv']:
        weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
        # skip header
        next(weather_station, None)
    elif options['in_json']:
        weather_station = json.loads(csvfile.read())['data']

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

        if options['db']:

            query = db_insert_query.format(measured_day, data_row[CSV_TEMP], data_row[CSV_RH], data_row[CSV_PRESS])
            db.execute(query)
            db.commit()

        dew_point = dp(float(data_row[CSV_TEMP]), float(data_row[CSV_RH]))

        if options['out_raw']:
            print "curr: {}, max: {}, min: {}, avg: {}, rh: {}, dp: {}".format(data_row[CSV_TEMP], temp_stats['abs_max'],
                                                                           temp_stats['abs_min'], temp_stats['abs_avg'],
                                                                           data_row[CSV_RH], dew_point)
        if options['out_html']:
            print '<tr>'
            print '<th>curr</th><td>%f</td>' % data_row[TEMP]
            print '<th>max</th><td>%f</td>' % temp_stats['abs_max']
            print '<th>min</th><td>%f</td>' % temp_stats['abs_min']
            print '<th>avg</th><td>%f</td>' % temp_stats['abs_avg']
            print '<th>rh</th><td>%f</td>' % data_row[CSV_RH] 
            print '<th>dp</th><td>%f</td>' % dew_point
            print '</tr>'

if options['out_html']:
    print '</table>'
if options['db']:
    db.close()

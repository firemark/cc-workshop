import csv
import json
from datetime import datetime
import sqlite3
import dbase
import dewpoint
import set_var as sv

temp_stats = {'abs_max': None, 'abs_min': None, 'abs_avg': None}


if sv.options['db']:
    db=dbase.db_init()

db_insert_query = "INSERT INTO measures (meas_time, temp, humidity, pressure) VALUES ('{}','{}','{}','{}');"


if sv.options['out_html']:
    print '<table>'


# that might be a weather station device, not a file
with open('history_export_2016-12-05T11-55-25.csv', 'r') as csvfile:
    if sv.options['in_csv']:
        weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
        # skip header
        next(weather_station, None)
    elif sv.options['in_json']:
        weather_station = json.loads(csvfile.read())['data']

    # process data
    for data_row in weather_station:

        # first entry for absolute max / min
        if temp_stats['abs_max'] is None:
            temp_stats['abs_max'] = data_row[sv.CSV_TEMP]
            temp_stats['abs_min'] = data_row[sv.CSV_TEMP]
            temp_stats['abs_avg'] = float(data_row[sv.CSV_TEMP])
        # update max / min
        else:
            temp_stats['abs_max'] = temp_stats['abs_max'] if (temp_stats['abs_max'] >= data_row[sv.CSV_TEMP]) else \
                data_row[sv.CSV_TEMP]
            temp_stats['abs_min'] = temp_stats['abs_min'] if (temp_stats['abs_min'] <= data_row[sv.CSV_TEMP]) else \
                data_row[sv.CSV_TEMP]
            temp_stats['abs_avg'] = (float(data_row[sv.CSV_TEMP]) + temp_stats['abs_avg']) / 2

        measured_day = datetime(int(data_row[sv.CSV_YEAR]), int(data_row[sv.CSV_MONTH]),
                                int(data_row[sv.CSV_DAY]), int(data_row[sv.CSV_HOUR]), int(data_row[sv.CSV_MINUTE]))

        if sv.options['db']:
            query = db_insert_query.format(measured_day, data_row[sv.CSV_TEMP], data_row[sv.CSV_RH], data_row[sv.CSV_PRESS])
            db.execute(query)
            db.commit()

        dew_point = dewpoint.dp(float(data_row[sv.CSV_TEMP]), float(data_row[sv.CSV_RH]))

        if sv.options['out_raw']:
            print "curr: {}, max: {}, min: {}, avg: {}, rh: {}, dp: {}".format(data_row[sv.CSV_TEMP], temp_stats['abs_max'],
                                                                           temp_stats['abs_min'], temp_stats['abs_avg'],
                                                                           data_row[sv.CSV_RH], dew_point)
        if sv.options['out_html']:
            print '<tr>'
            print '<th>curr</th><td>%f</td>' % data_row[TEMP]
            print '<th>max</th><td>%f</td>' % temp_stats['abs_max']
            print '<th>min</th><td>%f</td>' % temp_stats['abs_min']
            print '<th>avg</th><td>%f</td>' % temp_stats['abs_avg']
            print '<th>rh</th><td>%f</td>' % data_row[sv.CSV_RH] 
            print '<th>dp</th><td>%f</td>' % dew_point
            print '</tr>'

if sv.options['out_html']:
    print '</table>'
if sv.options['db']:
    db.close()

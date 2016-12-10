import csv
import json
from datetime import datetime
import sqlite3
import funkcje

temp_stats = {'abs_max': None, 'abs_min': None, 'abs_avg': None}

options = {
    'db': True,
    'out_html': False,
    'out_raw': True,
    'in_json': False,
    'in_csv': True,
}

if options['db']:
    db=funkcje.database_start()


CSV_YEAR = 0
CSV_MONTH = 1
CSV_DAY = 2
CSV_HOUR = 3
CSV_MINUTE = 4
CSV_TEMP = 5
CSV_RH = 6
CSV_PRESS = 7


if options['out_html']:
    print '<table>'




weather_station=funkcje.data_load('../history_export_2016-12-05T11-55-25.csv')


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
        query = funkcje.db_insert_query.format(measured_day, data_row[CSV_TEMP], data_row[CSV_RH], data_row[CSV_PRESS])
        db.execute(query)
        db.commit()

    dew_point = funkcje.dew_point(float(data_row[CSV_TEMP]), float(data_row[CSV_RH]))

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

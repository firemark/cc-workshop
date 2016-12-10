import csv
import json
from datetime import datetime
import database
import output
from utils import modify_stats, get_day
from enum_csv import CSV_TEMP, CSV_RH, CSV_PRESS

temp_stats = {'abs_max': None, 'abs_min': None, 'abs_avg': None}

options = {
    'db': True,
    'out_html': False,
    'out_raw': True,
    'in_json': False,
    'in_csv': True,
}

if options['db']:
    db = database.init('temp.db')
else:
    db = None

if options['out_html']:
    output.render_start_html()

# that might be a weather station device, not a file
with open('history_export_2016-12-05T11-55-25.csv', 'r') as csvfile:
    if options['in_csv']:
        weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
        # skip header
        next(weather_station, None)
    elif options['in_json']:
        weather_station = json.loads(csvfile.read())['data']

    # process data
    for data_row in weather_station:
        modify_stats(temp_stats, data_row)
        measured_day = get_day(data_row)
        if options['db']:
            # keywords - opisane w pliku database.py
            database.add_record(
                db=db,
                day=measured_day,
                temperature=data_row[CSV_TEMP],
                humidity=data_row[CSV_RH],
                pressure=data_row[CSV_PRESS],
            )

        # zapakowanie danych do wyswietlenia
        output_data = output.get_output_data(data_row, temp_stats)

        if options['out_raw']:
            output.render_raw(output_data)
        if options['out_html']:
            output.render_html(output_data)

if options['out_html']:
    output.render_stop_html()
if options['db']:
    database.close(db)


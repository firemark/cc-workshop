# oto propowana przezemnie wersja kodu - nie wiem czy jest idealna
# przyznam szczerze, ze pomysly refactoringu kodu ukradlem od was,
# wiec po czesci to tez wasz kod :)
import csv
import json
from datetime import datetime
import database
import output
import reader
from utils import modify_stats, get_day
from enum_csv import CSV_TEMP, CSV_RH, CSV_PRESS

temp_stats = {'abs_max': None, 'abs_min': None, 'abs_avg': None}

# zamiast options - takie rzeczy powinny byc zastapione przez uzycie argumentow w konsoli
# dobrym pomyslem jest uzycie modulu argparse (ktory zostal napisany przez naszego rodaka :)) 
# https://docs.python.org/2.7/library/argparse.html
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

# tutaj probowaliscie zamienic open na cos innego - dobry pomysl
# niestety ze wzgledu ze nie chcielismy wprowadzac zaawansowanego
# pythona, nie wprowadzalismy dzialanie 'with' bo to wymaga wytlumaczenia
# oraz obiektowosci, wiec nie bylismy w stanie zastapic open
# Jezeli ktos jest zainteresowany: https://docs.python.org/2.7/library/contextlib.html
# Tutaj tez zamiast stalej nazwy fajnie by bylo uzyc argparse (komentarz powyzej)
with open('history_export_2016-12-05T11-55-25.csv', 'r') as csvfile:
    if options['in_csv']:
        weather_station =  reader.get_from_csv(csvfile)
    elif options['in_json']:
        weather_station = reader.get_from_json(csvfile)

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


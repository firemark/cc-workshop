import csv
import json


def get_from_csv(csvfile):
    weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
    # skip header
    next(weather_station, None)
    return weather_station


def get_from_json(jsonfile):
    return json.loads(jsonfile.read())['data']

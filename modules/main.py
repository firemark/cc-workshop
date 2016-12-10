from calculations import process
import db
import loader

temp_stats = {'abs_max': None, 'abs_min': None, 'abs_avg': None}

options = {
	'db': True,
	'out_html': False,
	'out_raw': True,
	'in_json': False,
	'in_csv': True,
}
if options['db']:
	database = db.db_init()
	db_insert_query = db.db_get_insert_query()
if options['out_html']:
	print '<table>'


# that might be a weather station device, not a file
# with loader.load_file('history_export_2016-12-05T11-55-25.csv') as weather_station:

weather_station, file = loader.load_file('./../history_export_2016-12-05T11-55-25.csv')

process(weather_station, temp_stats, options, database)

file.close()

if options['out_html']:
	print '</table>'
if options['db']:
	database.close()

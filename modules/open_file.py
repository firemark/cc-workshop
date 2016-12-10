def otwieram_plik(sourceFile):
	with open(sourceFile, 'r') as csvfile:
    	if options['in_csv']:
    	    weather_station = csv.reader(csvfile, delimiter=';', quotechar='"')
    	    # skip header
    	    next(weather_station, None)
    	elif options['in_json']:
    	    weather_station = json.loads(csvfile.read())['data']

    return weather_station
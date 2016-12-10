import sqlite3

# pozwolilem sobie zmodyfikowac stringa - {} zamienilem na nazewnictwo
db_insert_query = "INSERT INTO measures (meas_time, temp, humidity, pressure) VALUES ('{day}','{temperature}','{humidity}','{pressure}');"


def init(filename):
    # czesto ludzie dodawali argument filename do inicjalizacji bazy
    # +1 dla was
    db = sqlite3.connect(filename)
    db.execute('''
    DROP TABLE IF EXISTS `measures`;
    ''')
    db.execute('''CREATE TABLE IF NOT EXISTS measures (
        meas_time INT PRIMARY KEY,
        temp NUMERIC,
        humidity NUMERIC,
        pressure NUMERIC
    );''')

    # to byl moj temat rozwazan - czy chce uzyc db jako zmienna globalna
    # w tym module albo zwracam polaczenie jako wynik tej funkcji?
    # to jest pytanie dosc programistyczno-filozoficzne
    # 1) db jako stala globalna po za funkcja:
    #  + nie musimy ja zwracac po inicjalizacji
    #    oraz uzywac jej jako pierwszy argument (jak w jezyku C)
    #  + osoba korzystajaca z tego modulu nie musi sie martwic polaczeniem
    #  - nie mozna takim sposobem posiadac wiele polaczen naraz
    # 2) db jako zwrocona wartosc funkcji
    #  + mozna posiadac wiele polaczen naraz
    #  + wygodniejsze testowanie (mozemy modifikowac polaczenie recznie w razie potrzeby)
    #  - programista musi pilnowac obiekt
    # 3) Obiektowosc :) Bedzie na kolejnym spotkaniu
    # ja postanowilem zwracac.
    return db


def add_record(db, day, temperature, humidity, pressure):
    # funkcje w pythonie posiadaja tak zwane keywords
    # mozemy sie odwolac do nazwanego argumentu funkcji
    query = db_insert_query.format(
        day=day,
        temperature=temperature,
        humidity=humidity,
        pressure=pressure,
    )
    db.execute(query)
    db.commit()


def close(db):
    db.close()


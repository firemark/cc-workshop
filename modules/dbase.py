import sqlite3

db_insert_query = "INSERT INTO measures (meas_time, temp, humidity, pressure) VALUES ('{}','{}','{}','{}');"


def connect():
    """ connect with database """
    return sqlite3.connect('temp.db')


def bootstrap(db):
    # drop if messures exists
    db.execute('''
    DROP TABLE IF EXISTS `measures`;
    ''')
    # create measures
    db.execute('''CREATE TABLE IF NOT EXISTS measures (
        meas_time INT PRIMARY KEY,
        temp NUMERIC,
        humidity NUMERIC,
        pressure NUMERIC
    );''')


def insert(db, day, temp, rh, press):
    query = db_insert_query.format(day, temp, rh, press)
    db.execute(query)
    db.commit()

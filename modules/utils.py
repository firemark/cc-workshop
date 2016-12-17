from enum_csv import CSV_TEMP, CSV_YEAR, CSV_DAY, CSV_MONTH, CSV_HOUR, CSV_MINUTE
from datetime import datetime

def dp(t, h):
    """
    calculates the dewpoint via the formula from weatherwise.org

    :type t: float
    :param t: temperature
    :param h: humidity
    :return: dew point
    """
    x = 1 - 0.01 * h;

    dew_point = (14.55 + 0.114 * t) * x
    dew_point += ((2.5 + 0.007 * t) * x) ** 3
    dew_point += (15.9 + 0.117 * t) * x ** 14
    dew_point = t - dew_point

    return dew_point

# Tutaj wykorzystuje dynamicznosc pythona oraz referencje
# nie zwracam nic, modyfikuje obiekt znajdujacy sie w argumencie
# zaleta/wada - trudny temat :) napewno wygodne
def modify_stats(stats, data_row):
    temp = data_row[CSV_TEMP]  # wyciagniecie wartosci jako zmienna lokalna
    if stats['abs_max'] is None:
        stats['abs_max'] = temp
        stats['abs_min'] = temp
        stats['abs_avg'] = float(temp)
    else:
        # nie mialem modyfikowac kodu ale tutaj plakalem jak przepisywalem
        stats['abs_max'] = max(temp, stats['abs_max'])
        stats['abs_min'] = min(temp, stats['abs_min'])
        stats['abs_avg'] = (float(temp) + stats['abs_avg']) / 2.0


def get_day(data_row):
    return datetime(
        int(data_row[CSV_YEAR]), int(data_row[CSV_MONTH]), int(data_row[CSV_DAY]),
        int(data_row[CSV_HOUR]), int(data_row[CSV_MINUTE]))



def calc_dew_point(t, h):
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
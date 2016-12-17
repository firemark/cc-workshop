from utils import dp
from enum_csv import CSV_TEMP, CSV_RH

# dla wygody zmieniam to w jeden slownik danych. Mega wygodne
def get_output_data(data_row, temp_stats):
    dew_point = dp(float(data_row[CSV_TEMP]), float(data_row[CSV_RH]))
    return {
        'temperature': data_row[CSV_TEMP],
        'max': temp_stats['abs_max'],
        'min': temp_stats['abs_min'],
        'avg': temp_stats['abs_avg'],
        'rh': data_row[CSV_RH],
        'dp': dew_point,
    }


def render_raw(data):
    print "curr: {}, max: {}, min: {}, avg: {}, rh: {}, dp: {}".format(
        data['temperature'],
        data['max'],
        data['min'],
        data['avg'],
        data['rh'],
        data['dp'], 
    )

def render_html(data):
    print '<tr>'
    print '<th>curr</th><td>%f</td>' % data['temperature']
    print '<th>max</th><td>%f</td>' % data['max']
    print '<th>min</th><td>%f</td>' % data['min']
    print '<th>avg</th><td>%f</td>' % data['avg']
    print '<th>rh</th><td>%f</td>' % data['rh'] 
    print '<th>dp</th><td>%f</td>' % dew_point
    print '</tr>'

def render_start_html():
    print '<table>'

def render_stop_html():
    print '</table>'

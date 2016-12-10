
def print_row(temp, abs_max, abs_min, abs_avg, rh, dew_point):
    print "curr: {}, max: {}, min: {}, avg: {}, rh: {}, dp: {}".format(
        temp, abs_max, abs_min, abs_avg, rh, dew_point)


def print_row_html(temp, abs_max, abs_min, abs_avg, rh, dew_point):
    print '<tr>'
    print '<th>curr</th><td>%f</td>' % temp
    print '<th>max</th><td>%f</td>' % abs_max
    print '<th>min</th><td>%f</td>' % abs_min
    print '<th>avg</th><td>%f</td>' % abs_avg
    print '<th>rh</th><td>%f</td>' % rh
    print '<th>dp</th><td>%f</td>' % dew_point
    print '</tr>'

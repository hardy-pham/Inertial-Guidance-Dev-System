# test for .csv functionality

import csv
row = [1,2]
test = 111

with open(str(test)+'templog.csv', 'a') as f:
    w = csv.writer(f)
    w.writerow(row)
    w.writerow(['hello'])


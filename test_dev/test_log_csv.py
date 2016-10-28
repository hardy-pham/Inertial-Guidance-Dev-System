# test for .csv functionality
import csv
import time

row = [1,2]
test = 111

# epoch time
epoch = int(time.time())

# unique .csv file on every run
with open(str(epoch) + '_log.csv', 'a') as f:
    w = csv.writer(f)
    w.writerow(row)
    w.writerow(['hello'])


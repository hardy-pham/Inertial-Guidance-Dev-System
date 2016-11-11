# test for .csv functionality
import csv
import time

row = [1,2]
test = 111

# epoch time
epoch = int(time.time())

# time/date
# form ---> YearMonthDate_HourMinutesSeconds
curDateTime = time.strftime("%Y%m%d_%H%M%S")
print(curDateTime)

# unique .csv file on every run
with open('../logs/' + str(curDateTime) + '_log.csv', 'a') as f:
    w = csv.writer(f)
    # append
    w.writerow(row)
    w.writerow(['x-cord','y-cord','z-cord'])


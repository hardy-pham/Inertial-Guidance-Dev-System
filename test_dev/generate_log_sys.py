import sys
import time

sys_out = sys.stdout
log_file = open("../logs/logger.log","w")
sys.stdout = log_file
count = 0

try:
    while True:
        print(count)
        count += 1
        time.sleep(1)
except KeyboardInterrupt:
    sys.stdout = sys_out
    log_file.close()


import schedule
import time

from main import checkClass


schedule.every().hour.at(":01").do(checkClass)

while True:
    schedule.run_pending()
    time.sleep(1)

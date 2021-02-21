import schedule
import time

from main import checkClass

# The following line schedules the checking for class every hour at 01 minute
schedule.every().hour.at(":01").do(checkClass)

print("Class scheduler running...")
print("You will be notified and link will be opened in your browser when a class starts.")

while True:
    schedule.run_pending()
    time.sleep(1)

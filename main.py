import json
import os
from datetime import datetime
import webbrowser
from playsound import playsound
from pynotifier import Notification


timeToClassDict = {}

def playSound():
    playsound('data/sound.ogg')

def notify(subject, link):
    # if os.name == 'nt':
    #     icon = "data/classroom.ico"
    # else:
    #     icon = "data/classroom.png"
    Notification(
        title='Upcoming Class - ' + subject,
        description='Opening - ' + link,
        icon_path="accessories-text-editor", # On Windows .ico is required, on Linux - .png
        duration=5                              # Duration in seconds
    ).send()

def startClass(subject, link):
    notify(subject, link)
    playSound()
    webbrowser.open(link)
    print("Successfully opened.")

def checkClass():
    d = datetime.now()
    day = d.weekday()
    hour = d.hour
    time = day*24 + hour
    print('---------------------------')
    print(str(d))
    if time in timeToClassDict:
        class_ = timeToClassDict[time]
        subject = class_['subject']
        link = class_['link']
        print(subject + " class right now.")
        startClass(subject, link)
    else:
        print("No class right now.")

with open("class-data.json") as f:
    data = json.load(f)
    for class_ in data:
        subject = class_['subject']
        link = class_['link']
        for time in class_['timings']:
            day = time['day']
            hour = time['hour']
            timeToClassDict[day*24 + hour] = {
                'subject': subject,
                'link': link,
            }

if __name__ == '__main__':
    checkClass()

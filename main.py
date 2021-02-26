import json
import os
from datetime import datetime
import webbrowser
from playsound import playsound
from pynotifier import Notification


timeToClassDict = {}

soundPath = os.path.join(os.path.dirname(__file__), 'data', 'sound.ogg')

def playSound():
    playsound(soundPath)

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

# Getting the absolute path of the file
dataPath = os.path.join(os.path.dirname(__file__), 'class-data.json')

# Loading timetable from class-data.json
with open(dataPath) as f:
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

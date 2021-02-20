import json
from datetime import datetime
import webbrowser
from playsound import playsound
import notify2

notify2.init('Classroom')

def playSound():
    playsound('data/sound.ogg')

def notify(subject, link):
    n = notify2.Notification(
        'Upcomming Class - ' + subject,
        'Opening - ' + link,
        "accessories-text-editor"   # Icon name
    )
    n.show()

def startClass(subject, link):
    notify(subject, link)
    playSound()
    webbrowser.open(link)
    print("opened")


timeToClassDict = {}

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
d = datetime.now()
day = d.weekday()
hour = d.hour
time = day*24 + hour
print('---------------------------')
print(str(d) + '\n')
if time in timeToClassDict:
    class_ = timeToClassDict[time]
    subject = class_['subject']
    link = class_['link']
    startClass(subject, link)

import psutil
import pywinauto
from pywinauto.application import Application
import sys
import pickle
import datetime
import csv

# Variables
CHATNAME = "小狐狸🦊"
SCROLLS = 50

# Classes
class RawMessage:
    def __init__(self, time, author, msg):
        self.time = time
        self.author = author
        self.msg = msg

class Message():
    def __init__(self, date, time, author, msg):
        self.date = date
        self.time = time
        self.author = author
        self.msg = msg

# Functions
def extract():
    '''Extract message contents from ListItem. Don't touch this please, I forgot how it works.'''
    msg_contents = message.children()[0].children()[1].children()
    time = msg_contents[0].children()[2].window_text()
    author = msg_contents[0].children()[0].window_text()
    try:
        msg = msg_contents[1].children()[0].children()[0].children()[0].window_text()
    except IndexError as e:
        msg = "[图片]"
    if not msg:
        msg = "[动画表情]"
    return time, author, msg

def checkSame(a, b):
    '''Checks if two RawMessage objects are the same.'''
    if a.time == b.time and a.author == b.author and a.msg == b.msg:
        return True
    return False

def checkSeen(l, a):
    '''Checks if the message a appears twice in the list l.'''
    for i in l:
        if checkSame(i, a):
            return True
    return False

def removeDuplicates():
    '''Will result in less messages than actual. Fine with me though, I don't know how to process it properly.'''
    seen = set()
    unique = []
    for msg in all_msg:
        if not checkSeen(seen, msg):
            unique.append(msg)
            seen.add(msg)

    # return unique[::-1]
    return unique

def printRawMsg(message):
    '''Prints out a RawMessage object in a readable form.'''
    print(f"{message.time} | {message.author}: {message.msg}")

def printMsg(message):
    '''Prints out a Message object in a readable form.'''
    print(f"{message.date} {message.time} | {message.author}: {message.msg}")

# Scraping
# Hook onto the app
PID = 0
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        if 'WeChat.exe' == pinfo['name']:
            PID = pinfo['pid']

app = Application(backend='uia').connect(process=PID)
chat_win = app[CHATNAME] # Change to the chatname you want to scrape

all_msg = []
for cycle in range(0, SCROLLS):
    chats = chat_win.wrapper_object().descendants()
    cur_cycle = []
    for message in chats:
        classname = message.friendly_class_name()
        if (classname == "ListItem"):
            time, author, msg = extract()
            cur_cycle.append(RawMessage(time, author, msg))
    all_msg.extend(cur_cycle)
    cords = chat_win.rectangle()
    pywinauto.mouse.scroll(wheel_dist=4, coords=(cords.left+10, cords.bottom-10))

all_msg = removeDuplicates()

# TODO: The order of the messages if fucked up for some reason. I guess we just have to ignore message order within the minute...

# Data Processing
# Generate dictionary for weekdays 1 week before current date.
eng_to_chinese = {
    'Monday': '星期一',
    'Tuesday': '星期二',
    'Wednesday': '星期三',
    'Thursday': '星期四',
    'Friday': '星期五',
    'Saturday': '星期六',
    'Sunday': '星期天'
}

current_date = datetime.date.today()

weekdays = {}

weekdays["今天"] = current_date
weekdays["昨天"] = current_date-datetime.timedelta(days=1)

for i in range(2,7):
    delta = datetime.timedelta(days=i)
    date = current_date - delta
    weekname = eng_to_chinese[date.strftime('%A')]
    weekdays[weekname] = date

# Process the time and generate a new list replacing RawMessage objects with Message objects
proc_msg = []

for msg in all_msg:
    time = msg.time
    date = weekdays.get(time) # Change chinese weekname to date object
    if date is not None: # e.g. "昨天"
        proc_msg.append(Message(date, "NA", msg.author, msg.msg))
    elif type(time) == str: # e.g. "12:03 pm"
        hour, minute = time.split(' ')[0].split(':')
        hour = int(hour)
        minute = int(minute)
        if time.split(' ')[1] == "pm" and hour != 12:
            hour += 12
        proc_msg.append(Message(current_date, datetime.time(hour, minute, 0), msg.author, msg.msg))
    else: # Normal date, e.g. "22/03/05"
        proc_msg.append(Message(time, "NA", msg.author, msg.msg))

# Export
filename = f"{datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')}.csv" # "23-05-19 18-27-45.csv"

with open(filename, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)

    # Write headers
    headers = ['Date', 'Time', 'Author', 'Msg']
    writer.writerow(headers)

    for msg in proc_msg:
        writer.writerow([msg.date, msg.time, msg.author, msg.msg])

print(f"Data exported to {filename} successfully.")

import psutil
import pywinauto
from pywinauto.application import Application
import sys
import pickle

# TODO: Dumpster fire code pulled straight from the jupyter notebook. I will cleanup...tomorrow...when I'm not sleep deprived... Good night!

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
chat_win = app['小狐狸🦊']
#print(chat_win.dump_tree())
#print("-----------------")
#print(chats)

def search(message):
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

class RawMessage:
    def __init__(self, time, author, msg):
        self.time = time
        self.author = author
        self.msg = msg

all_msg = []
for cycle in range(0, 50):
    chats = chat_win.wrapper_object().descendants()
    current_round = []
    for message in chats:
        classname = message.friendly_class_name()
        if (classname == "ListItem"):
            time, author, msg = search(message)
            #print("---------")
            #print(time)
            #print(author)
            #print(msg)
            current_round.append(RawMessage(time, author, msg))
    all_msg.extend(current_round)
    cords = chat_win.rectangle()
    pywinauto.mouse.scroll(wheel_dist=4, coords=(cords.left+10, cords.bottom-10))

def checkSame(a, b):
    if a.time == b.time and a.author == b.author and a.msg == b.msg:
        return True
    return False

def checkSeen(l, a):
    for i in l:
        if checkSame(i, a):
            return True
    return False

def printRawMsg(message):
    print(f"{message.time} | {message.author}: {message.msg}")

# Will result in less messages than actual. Fine with me though, I don't know how to process it properly.
seen = set()
uniq = []
for msg in all_msg:
    if not checkSeen(seen, msg):
        uniq.append(msg)
        seen.add(msg)

# all_msg = uniq[::-1]
all_msg = uniq
for msg in all_msg:
    printRawMsg(msg)
    continue

# TODO: The order of the messages if fucked up for some reason. I guess we just have to ignore message order within the minute...

import datetime

class Message():
    def __init__(self, date, time, author, msg):
        self.date = date
        self.time = time
        self.author = author
        self.msg = msg

current_date = datetime.date.today()

weekdays = {}
eng_to_chinese = {
    'Monday': '星期一',
    'Tuesday': '星期二',
    'Wednesday': '星期三',
    'Thursday': '星期四',
    'Friday': '星期五',
    'Saturday': '星期六',
    'Sunday': '星期天'
}
date_format = '%y/%m/%d'

for i in range(2,7):
    delta = datetime.timedelta(days=i)
    date = current_date - delta
    weekname = eng_to_chinese[date.strftime('%A')]
    weekdays[weekname] = date

# date = weekdays.get("weekname")
weekdays["今天"] = current_date
weekdays["昨天"] = current_date-datetime.timedelta(days=1)

proc_msg = []

def printMsg(message):
    print(f"{message.date} {message.time} | {message.author}: {message.msg}")

for msg in all_msg:
    time = msg.time
    date = weekdays.get(time)
    if date is not None:
        proc_msg.append(Message(date, "NA", msg.author, msg.msg))
    elif type(time) == str:
        #print(time)
        hour, minute = time.split(' ')[0].split(':')
        hour = int(hour)
        minute = int(minute)
        if time.split(' ')[1] == "pm" and hour != 12:
            hour += 12
        #print(hour, minute)
        #print("---------")
        proc_msg.append(Message(current_date, datetime.time(hour, minute, 0), msg.author, msg.msg))
    else:
        proc_msg.append(Message(time, "NA", msg.author, msg.msg))

for msg in proc_msg:
    printMsg(msg)

import csv

filename = 'output.csv'

with open(filename, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)

    # Write headers
    headers = ['Date', 'Time', 'Author', 'Msg']
    writer.writerow(headers)

    for msg in proc_msg:
        writer.writerow([msg.date, msg.time, msg.author, msg.msg])

print(f"Data exported to {filename} successfully.")

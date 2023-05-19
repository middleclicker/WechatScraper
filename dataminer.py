import csv
import os
import re
import datetime

folder_path = os.getcwd()
data = []
with open("combined.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        data.append(row)

# All messages ever sent timeline
daily_msg = {}
for message in data:
    date = message[0]
    author = message[2]
    if author not in daily_msg:
        daily_msg[author] = {date : 1}
    elif date not in daily_msg[author]:
        daily_msg[author][date] = 1
    else:
        daily_msg[author][date] += 1

# Total messages per person
overall_msg = {}
for message in data:
    author = message[2]
    if author not in overall_msg:
        overall_msg[author] = 1
    else:
        overall_msg[author] += 1

# Avg msg per day
daily_avg_msg = {}
days_texting = {}
for person in daily_msg:
    person_avg = 0
    days = 0
    for date in daily_msg[person]:
        person_avg += daily_msg[person][date]
        days += 1
    days_texting[person] = days
    person_avg /= days
    daily_avg_msg[person] = person_avg

# Avg words per msg
def count_characters_and_words(sentence):
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    words = sentence.split()
    chinese_count = 0
    english_word_count = 0
    for word in words:
        if chinese_pattern.search(word):
            chinese_count += len(re.findall(chinese_pattern, word))
        else:
            english_word_count += 1
    return chinese_count, english_word_count

avg_words_per_msg = {}
for message in data:
    author = message[2]
    msg = message[3]
    chn, eng = count_characters_and_words(msg)
    total = chn + eng
    if author not in avg_words_per_msg:
        avg_words_per_msg[author] = total
    else:
        avg_words_per_msg[author] += total

for person in avg_words_per_msg:
    avg_words_per_msg[person] /= overall_msg[person]

# Total photos / videos
total_photos = {}
for message in data:
    author = message[2]
    msg = message[3]
    if msg != "[图片]":
        continue
    if author not in total_photos:
        total_photos[author] = 1
    else:
        total_photos[author] += 1

# Average hourly messages
total_hourly_msg = {}
avg_hourly_msg = {}

def generateHours():
    x = {}
    for i in range(0, 24):
        x[i] = 0
    return x

for message in data:
    time = message[1]
    author = message[2]
    if time == "NA":
        continue
    hour = int(time.split(':')[0])
    if author not in total_hourly_msg:
        total_hourly_msg[author] = generateHours()
        total_hourly_msg[author][hour] = 1
    else:
        total_hourly_msg[author][hour] += 1

for person in total_hourly_msg:
    avg_hourly_msg[person] = generateHours()
    for hour in total_hourly_msg[person]:
        avg_hourly_msg[person][hour] = total_hourly_msg[person][hour] / days_texting[person]

# First messages of the day
first_msg = {}
total_first_msg = {}
monthly_first_msg = {}
first_msg_contents = {}

users = list(overall_msg.keys())
for i in range(len(data)-1, -1, -1):
    message = data[i]

    date = message[0]
    month = int(date.split('-')[1])
    author = message[2]
    msg = message[3]
    if date not in first_msg:
        first_msg[date] = author
        if author in total_first_msg:
            total_first_msg[author] += 1
        else:
            total_first_msg[author] = 1

        if author not in monthly_first_msg:
            monthly_first_msg[author] = {month : 1}
        elif month not in monthly_first_msg[author]:
            monthly_first_msg[author][month] = 1
        else:
            monthly_first_msg[author][month] += 1

        if msg not in first_msg_contents:
            first_msg_contents[msg] = 1
        else:
            first_msg_contents[msg] += 1

# Average reply time
avg_reply_time = {}
replied_msg = {}
lastMsgAuthor = data[0][2]
lastMsgTime = datetime.datetime.strptime(data[0][1], "%H:%M:%S").time()
for message in data:
    time = message[1]
    author = message[2]
    if time == "NA":
        continue
    if lastMsgAuthor == author:
        lastMsgTime = datetime.datetime.strptime(time, "%H:%M:%S").time()
        continue
    replyMsgTime = datetime.datetime.strptime(time, "%H:%M:%S").time()

    # Create datetime objects with the same date to calculate the time difference
    lastMsgDatetime = datetime.datetime.combine(datetime.datetime.today(), lastMsgTime)
    replyMsgDatetime = datetime.datetime.combine(datetime.datetime.today(), replyMsgTime)
    time_difference_min = abs(lastMsgDatetime - replyMsgDatetime).total_seconds()/60

    if author not in replied_msg:
        replied_msg[author] = 1
    else:
        replied_msg[author] += 1
    if author not in avg_reply_time:
        avg_reply_time[author] = time_difference_min
    else:
        avg_reply_time[author] += time_difference_min

    lastMsgAuthor = author
    lastMsgTime = datetime.datetime.strptime(time, "%H:%M:%S").time()

for person in avg_reply_time:
    avg_reply_time[person] /= replied_msg[person]

# Sentiment analysis
# I will figure this out someday...


print("----")
if not os.path.isdir("data"):
    os.mkdir("data")

with open("data/daily_msg.csv", 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    headers = []
    for x in list(daily_msg.keys()):
        headers.append(f"by {x}, x")
        headers.append(f"by {x}, y")
    writer.writerow(headers)

    proc_msg = []
    people = list(daily_msg.values())
    for x in list(people[0].keys()):
        date_list = []
        for person in people:
            date_list.append(x)
            date_list.append(person[x])
        proc_msg.append(date_list)

    for row in proc_msg:
        writer.writerow(row)

with open("data/overall_msg.csv", 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    headers = []
    headers.append("Variable")
    for x in list(overall_msg.keys()):
        headers.append(f"Sent by {x}")

    proc_msg = []

    total_messages = []
    total_messages.append("Total Messages")
    for x in list(overall_msg.values()):
        total_messages.append(x)
    proc_msg.append(total_messages)

    msg_per_day = []
    msg_per_day.append("Msg/Day")
    for x in list(daily_avg_msg.values()):
        msg_per_day.append(x)
    proc_msg.append(msg_per_day)

    awpm = []
    awpm.append("Msg/Day")
    for x in list(avg_words_per_msg.values()):
        awpm.append(x)
    proc_msg.append(awpm)

    pv = []
    pv.append("Photos/Videos")
    for x in list(total_photos.values()):
        pv.append(x)
    proc_msg.append(pv)

    rp = []
    rp.append("Avg. Reply Time")
    for x in list(avg_reply_time.values()):
        rp.append(x)
    proc_msg.append(rp)

    writer.writerow(headers)
    for row in proc_msg:
        writer.writerow(row)

with open("data/total_hourly_msg.csv", 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    headers = []
    headers.append(f"Time of Day")
    for x in list(daily_msg.keys()):
        headers.append(f"by {x}, y")
    writer.writerow(headers)

    proc_msg = []
    people = list(total_hourly_msg.values())
    for x in list(people[0].keys()):
        time_list = []
        time_list.append(x)
        for person in people:
            time_list.append(person[x])
        proc_msg.append(time_list)

    for row in proc_msg:
        writer.writerow(row)

with open("data/avg_hourly_msg.csv", 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    headers = []
    headers.append(f"Time of Day")
    for x in list(daily_msg.keys()):
        headers.append(f"by {x}, y")
    writer.writerow(headers)

    proc_msg = []
    people = list(avg_hourly_msg.values())
    for x in list(people[0].keys()):
        time_list = []
        time_list.append(x)
        for person in people:
            time_list.append(person[x])
        proc_msg.append(time_list)

    for row in proc_msg:
        writer.writerow(row)

#print(daily_msg)
#print(overall_msg)
#print(daily_avg_msg)
#print(avg_words_per_msg)
#print(total_photos)
#print(total_hourly_msg)
#print(avg_hourly_msg)
#print(days_texting)
#print(users)
#print(first_msg)
#print(total_first_msg)
#print(monthly_first_msg)
#print(first_msg_contents)
#print(replied_msg)
#print(avg_reply_time)

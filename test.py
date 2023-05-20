import os
import csv

daily_msg = {'Andy': {'2023-05-19': 37, '2023-05-18': 55, '2023-05-17': 51}, '小狐狸🦊': {'2023-05-19': 34, '2023-05-18': 46, '2023-05-17': 54}}
overall_msg = {'Andy': 143, '小狐狸🦊': 134}
daily_avg_msg = {'Andy': 47.666666666666664, '小狐狸🦊': 44.666666666666664}
avg_words_per_msg = {'Andy': 3.5314685314685317, '小狐狸🦊': 4.402985074626866}
total_photos = {'Andy': 4, '小狐狸🦊': 4}
total_hourly_msg = {'Andy': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 31, 9: 0, 10: 0, 11: 0, 12: 2, 13: 0, 14: 4, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}, '小狐狸🦊': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 31, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 3, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}}
avg_hourly_msg = {'Andy': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 10.333333333333334, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.6666666666666666, 13: 0.0, 14: 1.3333333333333333, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0}, '小狐狸🦊': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 10.333333333333334, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 1.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0}}
avg_reply_time = {'小狐狸🦊': 1.2222222222222223, 'Andy': 0.2777777777777778}

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

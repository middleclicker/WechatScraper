Planned stats
  - All messages ever sent timeline
    - Her message count each day
    - My message count each day
  - Overall analytics
    - Total messages for each person
    - Avg Msg per day
    - Avg Words per msg
    - Total photos / Videos
  - Average hourly messages
    - Average number of messages for each hour for each person
  - First messages of the day
    (Probably inaccurate)
    - Total of who sent it
    - Total for each month for each person
    - What are those first messages (dictionary with num. of times said)
  - Average reply time
    - I have very little data for this but I really want to know lol
  - Sentiment analysis
  - Cloud visualisation of all the content


  class Message():
      def __init__(self, date, time, author, msg):
          self.date = date
          self.time = time
          self.author = author
          self.msg = msg


{'Andy': {'2023-05-19': 37, '2023-05-18': 55, '2023-05-17': 51}, '小狐狸🦊': {'2023-05-19': 34, '2023-05-18': 46, '2023-05-17': 54}}
{'Andy': 143, '小狐狸🦊': 134}
{'Andy': 47.666666666666664, '小狐狸🦊': 44.666666666666664}
{'Andy': 3.5314685314685317, '小狐狸🦊': 4.402985074626866}
{'Andy': 4, '小狐狸🦊': 4}
{'Andy': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 31, 9: 0, 10: 0, 11: 0, 12: 2, 13: 0, 14: 4, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}, '小狐狸🦊': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 31, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 3, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}}
{'Andy': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 10.333333333333334, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.6666666666666666, 13: 0.0, 14: 1.3333333333333333, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0}, '小狐狸🦊': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 10.333333333333334, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 1.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0}}
{'Andy': 3, '小狐狸🦊': 3}
['Andy', '小狐狸🦊']
{'2023-05-17': 'Andy', '2023-05-18': '小狐狸🦊', '2023-05-19': 'Andy'}
{'Andy': 2, '小狐狸🦊': 1}
{'Andy': {5: 2}, '小狐狸🦊': {5: 1}}
{'james的': 1, '？': 1, '好呀': 1}
{'小狐狸🦊': 18, 'Andy': 18}
{'小狐狸🦊': 1.2222222222222223, 'Andy': 0.2777777777777778}

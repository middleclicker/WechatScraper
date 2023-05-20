# Wechat Scraper

Wechat Scraper is a tool for collecting and analyzing your Wechat chat history. Windows only.

## Project Status
I'll finish it after the exams lol

## Installation

Wechat Scraper runs with the following dependencies
```
matplotlib==3.5.1
plotly==5.6.0
psutil==5.9.0
psutil==5.8.0
pywinauto==0.6.8
wordcloud==1.9.1.1
```
You can install them manually or from the requirements.txt file
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository
```bash
git clone https://github.com/middleclicker/WechatScraper.git
```
2. Edit variables in `mindful.py`
- CHATNAME is the alias you gave to the contact / group chat. You have to change this for the program to run.
- SCROLLS is the number of times the program will scroll up. You do not have to change this.
```python
# Variables
CHATNAME = "小狐狸🦊"
SCROLLS = 500
```
3. Open WeChat and open the chat history box. Make sure it stays as the topmost app with no other windows covering it. I suggest using DeskPins to do this.
4. Open a command prompt and cd to the WechatScraper directory. Run `mindful.py`
```bash
python3 mindful.py
```
5. Wait for the program to finish. You should see a CSV file generated in the directory.
6. Run `combine.py` to combine your different scrapes and remove duplicates. This will generate a `combined.csv`. If you don't have multiple .csv files (multiple scrapes), don't run the file and rename your CSV file to `combined.csv`.
```bash
python3 combine.py
```
7. Run `dataminer.py` to extract information from the `combined.csv` file. The processed data should appear in `/data` directory. Two browser tabs should open displaying the graphs. If you are not happy with the color schemes, simply rerun the program to randomize the color schemes again. You can download the graphs as a PNG file by clicking on the download button.

## Sample Results
### Tally of first sent messages
![image](https://github.com/middleclicker/WechatScraper/blob/main/data/monthly_first_message.png)
### Daily message count
![image](https://github.com/middleclicker/WechatScraper/blob/main/data/total_daily_messages.png)
### All message contents word cloud
![image](https://github.com/middleclicker/WechatScraper/blob/main/data/all_msg_contents.png)
### First message contents word cloud
![image](https://github.com/middleclicker/WechatScraper/blob/main/data/first_msg_contents.png)

## Contributing

Pull requests are welcome. A version for MacOS would be amazing (I have no idea how to do that).

## License

MIT License

Copyright (c) 2023 middleclicker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

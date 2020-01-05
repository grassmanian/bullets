#!/usr/bin/python3
import requests
from datetime import datetime, timedelta

# if today is not sunday, go to previous week, else use this week, 
# if this week fails, downlaod last weeks
date = datetime.now()
date -= timedelta((date.weekday() + 1) % 7)
    
y = str(date.year)
m = str(date.month)
d = str(date.day)

urls = ("https://www.daytonlatinmass.org/wp-content/uploads/{y}/{m}/{y}-{m}-{d}.pdf".format(y = y, m = m.zfill(2), d = d.zfill(2)), 
        "http://www.emmanuelcatholic.com/wp-content/uploads/{year}/{m}/Bulletin-{m}{d}{y}.pdf".format(year = y, y = y[-2:], m = m.zfill(2), d = d.zfill(2)), 
        "https://daytonxii.org/wp-content/uploads/{y}/{m}/{month}-{d}-{y}-Bulletin.pdf".format(y = y, m = m, d = d, month = date.strftime("%B")),
        "https://www.byzantinecolumbus.com/bulletins/b{y}{m}{d}.pdf".format(y=y, m=m.zfill(2), d=d.zfill(2)) )

for url in urls:
    response = requests.get(url, headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36" })
    # if this prints something other than 200, be wary
    if response.status_code == 200:
        print(url, response.status_code)
    filename = response.url
    last = filename.rfind('/')

    with open(filename[last+1:], 'wb') as f:
        f.write(response.content)

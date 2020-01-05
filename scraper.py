#!/usr/bin/python3
import requests

urls = ("https://www.daytonlatinmass.org/wp-content/uploads/2019/12/2019-12-29.pdf", 
        "http://www.emmanuelcatholic.com/wp-content/uploads/2019/12/Bulletin-122919.pdf",
        "https://daytonxii.org/wp-content/uploads/2020/01/January-5-2020-Bulletin.pdf"
        "https://www.byzantinecolumbus.com/bulletins/b20191229.pdf")

for url in urls:
    response = requests.get(url)
    filename = response.url
    last = filename.rfind('/')

    with open(filename[last+1:], 'wb') as f:
        f.write(response.content)

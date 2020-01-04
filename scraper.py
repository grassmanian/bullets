#!/usr/bin/python3
import requests

response = requests.get("https://www.daytonlatinmass.org/wp-content/uploads/2019/12/2019-12-29.pdf")

with open('/tmp/temp.pdf', 'wb') as f:
    f.write(response.content)

import requests
from requests.api import post
r=requests.get("https://financialmodelingprep.com/api/v3/rss_feed?limit=100&apikey=8d9b24474aed44c8b146e6d58bc67671")
print(r.text)
print(r.status_code)

# url="www.something.com"
# data={"p1":4,"p2":8}
# r2=requests.post(url=url,data=data)

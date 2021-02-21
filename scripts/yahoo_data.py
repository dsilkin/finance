import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pytz
import json
import sys
import re
import requests
from bs4 import BeautifulSoup

def roundTime(dt=None, roundTo=60):
   if dt == None : dt = datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

cd2 = roundTime() - timedelta(hours=52)
cd1 = cd2 - timedelta(minutes=10)
data = yf.download(tickers=sys.argv[1], start=cd1,end=cd2, interval="1m",progress=False)
js = json.loads(str(data.to_json()).replace("'","\""))
summ_buy = 0
summ_sale = 0
#print(js["Volume"])
for i in range(0, len(js["Close"].values())):
    if (list(js["Close"].values())[i]) > (list(js["Open"].values())[i]):
        summ_buy = summ_buy + list(js["Volume"].values())[i]
    else:
        summ_sale = summ_sale + list(js["Volume"].values())[i]

URL = 'https://finance.yahoo.com/quote/'+sys.argv[1]+'?p='+sys.argv[1]+'&.tsrc=fin-srch'
res = requests.get(URL)
res.raise_for_status()
content = res.content
soup = BeautifulSoup(content, 'lxml')
quotes = soup.find_all('ul', {'class': 'My(0) Ov(h) P(0) Wow(bw)'})
count = 0
for quote in quotes:
    count+=len(quote.text)

print("bay " + str(summ_buy))
print("sale " + str(summ_sale))
print("news_counter " + str(count))


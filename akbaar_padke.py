#  ec5c9b81ba934bc8823fdb746714f2f7 my Api key from news api
import requests
import json
def str(f):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(f)

str("news for today")
url = "https://newsapi.org/v2/everything?q=tesla&from=2021-10-08&sortBy=publishedAt&apiKey=ec5c9b81ba934bc8823fdb746714f2f7"
news = requests.get(url).text 
news_dict = json.loads(news)
print(news_dict['status']) 
a =  news_dict['articles'] }] 
for articles in a:
    str(articles['title'])
    str("the next news is ")

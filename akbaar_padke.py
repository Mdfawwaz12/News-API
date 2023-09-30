#  ec5c9b81ba934bc8823fdb746714f2f7 my Api key from news api

'''news api se news ka url leko dekhe katho text mein ranga so json view 
chrome extension install karle katho json mein se python mein use karleja
step 1: voice create karnaso
step 2:news api se url copy paste karnaso
step 3:url ko get karnaso and text mein convert karnaso 
step 4: uske baad json mein convert karnaso
step 5:for loop dalko read hojanga


'''
import requests
import json
def str(f):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(f)

str("news for today")
url = "https://newsapi.org/v2/everything?q=tesla&from=2021-10-08&sortBy=publishedAt&apiKey=ec5c9b81ba934bc8823fdb746714f2f7"
#url aako string json ko ek url deko dictionary mein convert hoko access kar sakte
news = requests.get(url).text #ye text denga nai text likhe nai katho
# print(news) ye aako ek string (news['status']) aisa nai karsakte so json mein convert karko dict se access
news_dict = json.loads(news)
print(news_dict['status']) # json mein convert hoga 
a =  news_dict['articles'] #api mein articles aako list [{}] 
#json mein ek data hai katho {} multiple data hai katho[{}] list ka andar liknaso
for articles in a:
    str(articles['title'])
    str("the next news is ")

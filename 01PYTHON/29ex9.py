import json
import requests


def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News of Today..Lets begin")
    url=("https://newsapi.org/v2/top-headlines?country=in&apiKey=2dd4e985654444b4bbfc4b4c9cebd133")
    news=requests.get(url).text
    news_dict=json.loads(news)
    # print(news_dict["articles"])
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to next news........Listen Carefully")
    speak("Thanks for listening.........")

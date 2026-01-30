def read(chiz):
    from win32com.client import Dispatch
    speak  =Dispatch("SAPI.SpVoice")
    speak.Speak(chiz)

if __name__ == '__main__':

    from newsapi import NewsApiClient
    import json

    api = NewsApiClient(api_key='0865ef0ba18e42a5b3276fb358616755')
    d=api.get_top_headlines(sources='bbc-news')

    with open("news.json","w") as f:
        f.write(json.dumps(d,indent=4))
        
    for i in d["articles"]:
       if i['content']:
           read(i['content'])
    
    
    



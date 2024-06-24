import feedparser
from tabulate import tabulate

import json_and_text 

data = []
summary = []
def fetch_feed(url):
    
    rss_url = "feeds.ign.com/ign/games-all"
    f = feedparser.parse(url)
    if f.status ==200:
        for i in f.entries:
            data.append([i.title])
            summary.append([i.title,i.summary])
            
    formart_to_table()
           


def formart_to_table():
    headers = ["title"]
    print(tabulate(data,headers=headers,showindex="always",tablefmt="github"))
    
    index = int(input("Choose yur index: "))
    print("\n\n")
    for i in summary[index]:
        print(i)
  


if __name__=="__main__":
    pass
    # Converter()
    # fetch_feed()
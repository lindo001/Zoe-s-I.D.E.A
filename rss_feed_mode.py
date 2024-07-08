import os
import feedparser
from tabulate import tabulate
from pick import pick

from json_and_text import Converter
# from json_and_text import Converter

# import json_and_text 

data = []
summary = []
def fetch_feed(url):
    
    f = feedparser.parse(url)
    f = feedparser.parse(url)
    if f.status == 200:
        for entry in f.entries:
            data.append([entry.title])
            summary.append([entry.title, entry.summary, entry.link])
    format_to_table()
           


def format_to_table():
    headers = ["title"]
    print(tabulate(data,headers=headers,showindex="always",tablefmt="github"))
    
    index = int(input("Choose yur index: "))
    print("\n\n")
    for i in summary[index]:
        print(i)
    input()
    os.system("clear")
    
      
def feed_genre():
    stuff = Converter("txt_files/rss_links.json",isJson=True).get_data()
    
    type_of_feed = []
    for key, url in stuff.items():
        type_of_feed.append(key)
        print(key)
        
    type_of_feed.append("exit")
    
    title = "Select an RSS topic"
    while True:
        os.system("clear")
        option, index = pick(type_of_feed, title)
        
        if option == "exit":
            return
        else:
            while True:
                fetch_feed(stuff[option])
    
    print(f"You selected: {option}")

if __name__=="__main__":
    # pass
    # hold = Converter("txt_files/rss_links.json",isJson=True)
    feed_genre()
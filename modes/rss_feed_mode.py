import feedparser
from tabulate import tabulate

data = []
summary = []
def fetch_feed():
    url = "https://www.ign.com/rss/articles/feed?tags=games"
    # url = "https://feeds.capi24.com/v1/Search/articles/News24/TopStories/rss"
    # url = "https://www.freecodecamp.org/news/rss"
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
    fetch_feed()
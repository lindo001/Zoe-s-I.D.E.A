# import pick
from pytube import YouTube, Playlist

path:dict = {"save_to":"","read_from":""}

def get_video(string:str)->None:
    save_to=path["save_to"]
    data= YouTube(string)
    streams=data.streams.get_highest_resolution()
    print(streams.download(save_to))
    
def get_playlist(string:str)->None:
    try:
        data = Playlist(string).video_urls
        for i in data:
            get_video(i)
    except:
        print("URL is not from playlist")

def download_mode_menu(option:str):
    file_to_read =path["read_from"]
    title = 'Please choose quality: '
    options = ['video', 'playlist']
    
    
    if  options[0] in option:
        for i in read_text(file_to_read):
            get_video(i)
            # print("getting video")
    elif options[1] in option:
        for i in read_text(file_to_read):
            get_playlist(i)
            # print("getting playlist")
    else:
        print("Failed to retrive data")

def read_text(file_path)-> list[str]:
        links=[]
        with open(file_path,"r")as f:
            links.append(f.readlines()) 
        return links[0]
    
    
#where to save it 
def load_urls():
   path["read_from"] = input("Read url files from: ")
   path["save_to"] = input("Where to save content to: ")
   while True:
        stdin = input("is it a (video or playlist) ?:").lower()
        if stdin == "video" or stdin == "playlist":
            download_mode_menu(stdin)
            break

   
if __name__=="__main__":
    load_urls()
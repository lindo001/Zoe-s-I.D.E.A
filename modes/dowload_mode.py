import pick
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

def download_mode_menu():
    file_to_read =path["read_from"]
    title = 'Please choose quality: '
    options = ['video', 'playlist']
    option,_ = pick.pick(options, title)
    
    
    if option==options[0]:
        for i in read_text(file_to_read):
            get_video(i)
    elif option==options[1]:
        for i in read_text(file_to_read):
            get_playlist(i)

def read_text(file_path)-> list[str]:
        links=[]
        with open(file_path,"r")as f:
            links.append(f.readlines()) 
        return links[0]
    
if __name__=="__main__":
    download_mode_menu()
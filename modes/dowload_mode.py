import pick
from pytube import YouTube, Playlist

    # Quality / Convert /  Playlist / single video
def get_video(string:str)->None:
    data= YouTube(string).author
    print(data)    
    
def get_playlist(string:str)->None:
    try:
        data = Playlist(string).video_urls
        for i in data:
            get_video(i)
    except:
        print("URL is not from playlist")

def download_mode_menu():
    link=""
    title = 'Please choose quality: '
    options = ['video', 'playlist']
    option,_ = pick.pick(options, title)
    
    if option==options[0]:get_video(link)
    elif option==options[1]:get_playlist(link)


if __name__=="__main__":
    download_mode_menu()
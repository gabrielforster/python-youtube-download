from pytube import YouTube

def download_video(link: str):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    
    try:
        yt.download()
    except:
        print("Something went wrong while downloading the video!")
    
    print("The video download has been finished!")

link = input("Input the link for the video you wanna download:")
download_video(link)

# from pytube import YouTube

# def Download(link):
#     # Create a YouTube object using the provided link
#     youtubeObject = YouTube(link)
    
#     # Get the stream with the highest resolution available
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
    
#     try:
#         # Download the selected stream
#         youtubeObject.download()
#         print("Download is completed successfully")
#     except Exception as e:
#         # Print any error that occurs during the download process
#         print(f"An error has occurred: {e}")

# # Input: User provides the URL of the YouTube video
# link = input("Enter the YouTube video URL: ")

# # Call the download function with the provided link
# Download(link)

import yt_dlp

def Download(link):
    try:
        # Define options for yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            print(f"Video Title: {info_dict.get('title', 'No Title')}")
            print("Download is completed successfully")
    except Exception as e:
        # Print the error if something goes wrong
        print(f"An error has occurred: {e}")

# Input: User provides the YouTube video URL
link = input("Enter the YouTube video URL: ")
Download(link)

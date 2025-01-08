import tkinter as tk
from tkinter import messagebox
import youtube_dl
import os

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download and conversion complete")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create download folder if it does not exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# Set up the main application window
root = tk.Tk()
root.title("YouTube to MP3 Converter")

# Create and place the URL entry field
tk.Label(root, text="YouTube URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()
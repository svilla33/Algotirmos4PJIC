import re
import random
import requests
import webbrowser

url = "https://www.youtube.com/results?search_query=cats"

html = requests.get(url).text

# regex para encontrar IDs de video (11 caracteres)
videos = re.findall(r"watch\?v=([a-zA-Z0-9_-]{11})", html)

if videos:
    video_random = random.choice(videos)
    link = f"https://www.youtube.com/watch?v={video_random}"

    print("Video aleatorio:", link)

    webbrowser.open(link)
else:
    print("No se encontraron videos")
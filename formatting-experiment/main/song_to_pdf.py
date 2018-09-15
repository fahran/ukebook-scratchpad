import pdfkit
import json
import song_converter
from bs4 import BeautifulSoup

header = open("styling/song-viewer-head.html", "r").read()
footer = open("styling/song-viewer-foot.html", "r") .read()
css = "styling/song-style.css"

# raw_song = open("songs/a-little-respect-raw.txt", "r").read()
song_data = json.loads(open("songs/a-little-respect.json", "r").read())
weds_formatted_song = song_converter.to_html("A Little Respect", "Erasure", song_data['tabs'][0]['song-body'])
song_page = header + weds_formatted_song + footer

print(song_page)

html_out = open("out.html", "w")
html_out.write(song_page)
html_out.close()

pdfkit.from_string(song_page, "out.pdf", css=css)
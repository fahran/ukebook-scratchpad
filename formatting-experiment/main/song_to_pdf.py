import pdfkit
import song_converter

header = open("styling/song-viewer-head.html", "r").read()
footer = open("styling/song-viewer-foot.html", "r") .read()
song = open("songs/a-little-respect.html", "r").read()
css = "styling/song-style.css"

raw_song = open("songs/a-little-respect-raw.txt", "r").read()

formatted_song = song_converter.to_html(raw_song)

song_page = header + formatted_song + footer
print(song_page)

html_out = open("out.html", "w")
html_out.write(song_page)
html_out.close()

pdfkit.from_string(song_page, "out.pdf", css=css)
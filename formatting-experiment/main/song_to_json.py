import json

song = open("songs/a-little-respect-raw.txt", "r").read()
json = json.dumps({'song-body': song})
print(json)
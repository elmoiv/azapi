from azapi import AZlyrics

api = AZlyrics()

api.artist = "Taylor Swift"
songs = api.getSongs()

for song in songs:
    api.getLyrics(url=songs[song]["url"])


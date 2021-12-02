from azapi import AZlyrics

api = AZlyrics("duckduckgo")

api.artist = "Taylor Swift"
api.title = "Blank Space"

api.getLyrics(path="C:\\Music\\Lyrics")


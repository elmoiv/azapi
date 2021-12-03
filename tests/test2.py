from azapi import AZlyrics
import pprint

api = AZlyrics()

api.artist = "Ed Sheeran"

songs = api.getSongs()

pprint.pprint(songs, indent=5)

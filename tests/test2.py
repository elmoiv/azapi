from azapi import AZlyrics
import pprint

api = AZlyrics()

songs = api.getSongs('Ed Sheeran')

pprint.pprint(songs, indent=5)
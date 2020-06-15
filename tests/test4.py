from azapi import AZlyrics

api = AZlyrics('google')

# We are Searching for Meghan's song "All about that bass"
api.title = 'about that bass'

Lyrics = api.getLyrics()

print(Lyrics)

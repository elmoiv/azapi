from azapi import AZlyrics

api = AZlyrics()

# We are Searching for Meghan's song "All about that bass"
songs = api.search('about the bass', category = 'songs')

# Song appears to be the first in search results
song_url = songs[0]['url']

Lyrics = api.getLyrics(url = song_url)

print(Lyrics)

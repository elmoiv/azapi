from azapi import AZlyrics

api = AZlyrics('google')

# Kanye is in the format of "West" in AZLyrics database
# Here we search for his name to fetch the correct url
api.artist = 'Kanye west'
songs = api.getSongs()

for song in songs:
    print(song, songs[song]['year'])

from azapi import AZlyrics

api = AZlyrics()

# Kanye is in the format of "West" in AZLyrics database
# Here we search for his name to fetch the correct url
songs = api.getSongs('Kanye', True)

print(songs)

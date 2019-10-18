from azapi import AZlyrics

api = AZlyrics()

# Using search to get correct artist and title
Lyrics = api.getLyrics(artist='meghan', title='bass', search=True)

print(Lyrics)

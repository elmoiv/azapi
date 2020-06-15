from azapi import AZlyrics

api = AZlyrics('duckduckgo')

# Mis-typing "Meghan Trainor" and "All about the bass"
api.artist = 'Mehgan trenor'
api.title = 'about this bass'

# Using search to get correct artist and title
Lyrics = api.getLyrics()

print(Lyrics)

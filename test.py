import azapi

artist = input('Artist: ')
title = input('Title: ')

Song = azapi.AZlyric(artist, title)

lyric = Song.Get(save=True)

print(lyric)

input()
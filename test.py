import azapi

title = input('Title: ')
artist = input('Artist: ')

Song = azapi.AZlyric(title, artist)
lyric = Song.Get(save=True)

print(lyric)
input()

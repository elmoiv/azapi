# AZLyricsAPI
A simple api for AZLyrics.com to get lyrics easily :)


# Features
- Save lyrics in a .txt file.
- You can print lyrics in the Terminal.

# How to Use
```
import azapi

Song = azapi.AZlyric(title, artist)

lyric = Song.Get(save=True)

print(lyric)
```

# TODO
* Extend the api to be able to get Artist songs or album list.
* prevent getting blacklisted while scraping
* ...

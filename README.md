# AZLyricsAPI
A simple api for AZLyrics.com to get lyrics easily :)


# Features
- Save lyrics in a .txt file.
- print lyrics in the Terminal.

# How to Use
```
import azapi

Song = azapi.AZlyrics(artist, title)
Song.Get(save=True)

```
- _artist_ : must be string value.
- _title_ : must be string value.
- _save_ : must be boolean value.


# TODO
- Extend the api to be able to get Artist songs or album list.
- thinking...

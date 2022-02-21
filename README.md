# azapi

[![Build Status](https://api.travis-ci.org/elmoiv/azapi.svg?branch=master)](https://travis-ci.org/elmoiv/azapi)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/azapi/)

A fast and secure API for AZLyrics.com to get lyrics easily :)

## Features

- Get artist's songs list with Album, Year ...etc
- Can get results via Google* and Duckduckgo* for accurate results.
- Save lyrics in a .txt file or any format you like.
- Avoid BAN using proxy\*\* and multiple user agents.

## Installation

`azapi` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
pip install azapi
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/elmoiv/azapi.git
```

## Usage

```python
import azapi

API = azapi.AZlyrics('google', accuracy=0.5)

API.artist = 'Tylor Swft'
API.title = 'Bad Blods'

API.getLyrics(save=True, ext='lrc')

print(API.lyrics)

# Correct Artist and Title are updated from webpage
print(API.title, API.artist)
```

## Tests

Here are a few sample tests:

- [Getting lyrics](https://github.com/elmoiv/azapi/tree/master/tests/test1.py)
- [Getting lyrics (Custom Path)](https://github.com/elmoiv/azapi/tree/master/tests/test7.py)
- [Getting songs list](https://github.com/elmoiv/azapi/tree/master/tests/test2.py)
- [Downloading lyrics from a list](https://github.com/elmoiv/azapi/tree/master/tests/test3.py)
- [Get Lyrics by title only](https://github.com/elmoiv/azapi/tree/master/tests/test4.py)
- [Using search engine with titles](https://github.com/elmoiv/azapi/tree/master/tests/test5.py)
- [Using search engine with mistyped title and artist](https://github.com/elmoiv/azapi/tree/master/tests/test6.py)

## Changelog

### v3.0.8 21-02-2022
- [#17](https://github.com/elmoiv/azapi/pull/17) Use search engine method when normal method fails.

### v3.0.7 03-01-2022
- [#6](https://github.com/elmoiv/azapi/issues/6) [Re-Fixed] Single albums return relative urls.

### v3.0.6 12-02-2021

- [#11](https://github.com/elmoiv/azapi/issues/11) Fixed proxy not used properly.

### v3.0.5 26-09-2020

- [#10](https://github.com/elmoiv/azapi/issues/10) Fixed one-liner lyrics can't be retrieved.
- Direct lyrics URLs can now be passed without artist or title.
- Fixed minor bugs.

### v3.0.4 22-08-2020

- [#9](https://github.com/elmoiv/azapi/issues/9) Update title and artist attributes with exact values from AZLyrics.com.
- Fixed minor bugs.

### v3.0.3 13-08-2020

- [#8](https://github.com/elmoiv/azapi/issues/8) Fixed `getSongs` not returning all songs.

### v3.0.2 25-07-2020

- [#7](https://github.com/elmoiv/azapi/issues/7) Added the ability to use custom path with `getLyrics`.
- Added `self.lyrics` and `self.songs` to store last call.
- Added `self.lyrics_history` that stores all fetched lyrics.

### v3.0.1 07-07-2020

- [#6](https://github.com/elmoiv/azapi/issues/6) Fixed single albums return relative urls.

### v3.0.0 15-06-2020

- Project re-done from scratch.
- Added the ability to use search engines.
- Fixed unicode issue with non-english lyrics.
- Fixed songs list not working for artists with single album.
- Removed search as it's no longer needed.
- Fixed NoneType bugs.

### v2.1.0 18-10-2019

- Added search feature to `getSongs` and `getLyrics`.
- You can use search albums, songs and artists.

### v2.0.1 11-09-2019

- First Release

## Stargazers over time

[![Stargazers over time](https://starchart.cc/elmoiv/azapi.svg)](https://starchart.cc/elmoiv/azapi)

## Contributing

Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/azapi/issues) or send me a pull request.

\*_It is adviced not to send too many requests to avoid IP ban by search engines._

_\*\*Proxy is set by the user, defult is empty._

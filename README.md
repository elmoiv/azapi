# azapi
[![HitCount](http://hits.dwyl.io/elmoiv/azapi.svg)](http://hits.dwyl.io/elmoiv/azapi)
[![Build Status](https://api.travis-ci.org/elmoiv/azapi.svg?branch=master)](https://travis-ci.org/elmoiv/azapi)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/azapi/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/52bd035af901477a8c7d7aaf043d580f)](https://www.codacy.com/manual/elmoiv/azapi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=elmoiv/azapi&amp;utm_campaign=Badge_Grade)

A fast and secure api for AZLyrics.com to get lyrics easily :)


## Features
- Get artist's songs list with Album, Year ...etc
- Can get results via Google* and Duckduckgo* for accurate results.
- Save lyrics in a .txt file or any format you like.
- Avoid BAN using proxy** and multiple user agents.

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
```
## Changelog

### v3.0.2 25-07-2020
  * Added the ability to use custom path with `getLyrics`.
  * Added `self.lyrics` and `self.songs` to store last call.
  * Added `self.lyrics_history` that stores all fetched lyrics.

### v3.0.1 07-07-2020
  * Fixed single albums return relative urls.

### v3.0.0 15-06-2020
  * Project re-done from scratch.
  * Added the ability to use search engines.
  * Fixed unicode issue with non-english lyrics.
  * Fixed songs list not working for artists with single album.
  * Removed search as it's no longer needed.
  * Fixed NoneType bugs.

### v2.1.0 18-10-2019
  * Added search feature to `getSongs` and `getLyrics`.
  * You can use search albums, songs and artists.

### v2.0.1 11-09-2019
* First Release

## Tests
Here are a few sample tests:

  * [Getting lyrics](https://github.com/elmoiv/azapi/tree/master/tests/test1.py)
  * [Getting lyrics (Custom Path)](https://github.com/elmoiv/azapi/tree/master/tests/test7.py)
  * [Getting songs list](https://github.com/elmoiv/azapi/tree/master/tests/test2.py)
  * [Downloading lyrics from a list](https://github.com/elmoiv/azapi/tree/master/tests/test3.py)
  * [Get Lyrics by title only](https://github.com/elmoiv/azapi/tree/master/tests/test4.py)
  * [Using search engine with titles](https://github.com/elmoiv/azapi/tree/master/tests/test5.py)
  * [Using search engine with mistyped title and artist](https://github.com/elmoiv/azapi/tree/master/tests/test6.py)

**It is adviced not to send too many requests to avoid IP ban by search engines.*

***Proxy is set by the user, defult is empty.*

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/azapi/issues) or send me a pull request.

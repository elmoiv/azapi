# azapi
[![Build Status](https://api.travis-ci.org/elmoiv/azapi.svg?branch=master)](https://travis-ci.org/elmoiv/azapi)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/azapi/)

A fast and secure api for AZLyrics.com to get lyrics easily :)


## Features
- Get Artist's Songs list with Album, Year ...etc
- Save lyrics in a .txt file or any format you like.
- Avoid BAN using proxy and multiple user agents.
- Search for albums, songs, artists when you are not sure.

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

Artist = azapi.AZlyrics()

lyric = Artist.getLyrics("Taylor Swift", "Bad Blood", save=False)

print(lyric)
```
## Changelog

### v2.1.0 18-10-2019
* Added search feature to `getSongs` and `getLyrics`
* You can use search albums, songs and artists

### v2.0.1 11-9-2019
* First Release

## Tests
Here are a few sample tests:

* [Getting lyrics](https://github.com/elmoiv/azapi/tree/master/tests/test1.py)
* [Getting songs list](https://github.com/elmoiv/azapi/tree/master/tests/test2.py)
* [Downloading lyrics from a list](https://github.com/elmoiv/azapi/tree/master/tests/test3.py)
* [Search for a song and get Lyrics](https://github.com/elmoiv/azapi/tree/master/tests/test4.py)
* [Using search with `getSongs`](https://github.com/elmoiv/azapi/tree/master/tests/test5.py)
* [Using search with `getLyrics`](https://github.com/elmoiv/azapi/tree/master/tests/test6.py)


## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/azapi/issues) or send me a pull request.

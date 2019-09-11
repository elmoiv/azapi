# azapi
[![Build Status](https://api.travis-ci.org/elmoiv/azapi.svg?branch=master)](https://travis-ci.org/elmoiv/azapi)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/azapi/)

A fast and secure api for AZLyrics.com to get lyrics easily :)


## Features
- Get Artist's Songs list with Album, Year ...etc
- Save lyrics in a .txt file or any format you like.
- Avoiding BAN using proxy and multiple user agents.

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

Artist = azapi.AZlyrics(proxy={})

lyric = Artist.getLyrics(artist="Taylor Swift", title="Bad Blood", ext="lrc", save=Fasle)

print(lyric)
```

## Tests
Here are a few sample tests:

* [Getting Lyrics](https://github.com/elmoiv/azapi/tree/master/tests/test1.py)
* [Getting Songs List](https://github.com/elmoiv/azapi/tree/master/tests/test2.py)
* [Downloading Lyrics from aList](https://github.com/elmoiv/azapi/tree/master/tests/test3.py)

## TODO
* Adding songs sorting feature
* ...

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/azapi/issues) or send me a pull request.

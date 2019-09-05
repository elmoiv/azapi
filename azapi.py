#       azapi.py, an api for AZLyrics
#
#       Copyright 2019 Khaled El-Morshedy <elmoiv>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License 3 as published by
#       the Free Software Foundation.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import requests
from lxml import html

class AZlyric:
    def __init__(self, title, artist):
        self.title = title.replace(' ','').lower()
        self.artist = artist.replace(' ','').lower()

    def get(self, save=True):
        page = requests.get(f'https://www.azlyrics.com/lyrics/{self.artist}/{self.title}.html')
        tree = html.fromstring(page.content)
        lyrics = ''.join(tree.xpath('/html/body/div[3]/div/div[2]/div[5]//text()')[1:])
        if lyrics:
            if save and lyrics:
                with open('{}-{}.txt'.format(self.title.title(), self.artist.title()), 'w') as f:
                    f.write(lyrics.strip())
            return lyrics.strip()
        return None

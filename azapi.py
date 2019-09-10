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
            if save:
                with open('{}-{}.txt'.format(self.title.title(), self.artist.title()), 'w') as f:
                    f.write(lyrics.strip())
            return lyrics.strip()
        return None

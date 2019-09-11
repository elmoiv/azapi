import time
from .RequestMaker import Requester
from .AZtools import *

class AZlyrics(Requester):
    '''
    # [AZ Lyrics API](https://github.com/elmoiv/AZLyricsAPI):

    ### Fast and Secure api for AZLyrics.com

    - `title`:  song title
    - `artist`: singer name
    - `proxies`: if you want to use proxy while connecting to AZLyrics.com
        - proxies should be of type `dict` in the form of:
            
             {

                "http":"xxx.xxx.xxx.xx",
                "https":"xxx.xxx.xxx.xx",
                ... etc

            }
    
    '''
    def __init__(self, title='', artist='', proxies={}):
        self.title = filtr(title)
        self.artist = filtr(artist)
        self.proxies = proxies

    def getLyrics(self, url=None, title=None, artist=None, ext='txt', save=True, sleep=5):
        ''' 
        ### Reterives Lyrics for a given song details:

        - `url`: url of the song's Azlyrics page
            - You don't have to set `artist` or `title` if you have the `url` of the lyrics
        - `title`:  song title
        - `artist`: singer name
        - `ext`: extension of the lyrics saved file, default is `.txt`
        - `save`: set to `False` if you don't wan't to save in a file
        - `sleep`: waiting time before sending a requests
            - It is advised to set it to more than `5` seconds to avoid being banned 
        '''
        if sleep < 1:
            # THIS IS RISKY!
            sleep == 1
        time.sleep(sleep)

        link = None

        ### Handling args
        if url:
            link = url
        else:
            title, artist = filtr(title), filtr(artist)
            if not all([title, artist]):
                if all([self.title, self.artist]):
                    title, artist = self.title, self.artist
                else:
                    raise Exception("Both Artist and Title can't be empty!")
            link = '{}/lyrics/{}/{}.html'.format(self.azURL, artist, title)
        
        page = self.get(link, _proxies=self.proxies)

        artist = filtr(str(htmlFindAll(page)('div', class_='lyricsh')[0])[29:-23], True)
        title = filtr(str(htmlFindAll(page)('b')[1])[4:-5], True)
        lyrics = ParseLyric(page)

        ## Saving Lyrics
        if lyrics:
            if save:
                with open('{} - {}.{}'.format(title.title(), artist.title(), ext), 'w', encoding='utf-8') as f:
                    f.write(lyrics.strip())
            return lyrics.strip()

        return None

    def getSongs(self, artist=None):
        '''
        ### Returns a dictionary of songs with their links:
        #### output:
         {
             
             "song name": {
               "year":"1234",
               "album":"song's album",
               "type": "album type", # EP, Album, ...etc
               "url": "url for the song's lyrics"
               }
        }
        - `artist`: singer name
            - If it's `None`, it will be set to what you initialized
        '''

        artist = filtr(artist)

        if not artist:
            if self.artist:
                artist = self.artist
            else:
                raise Exception("Artist can't be empty!")

        albums_page = self.get('{}/{}/{}.html'.format(self.azURL, artist[0], artist), _proxies=self.proxies)

        return ParseSongs(albums_page)

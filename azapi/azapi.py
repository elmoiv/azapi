import time
from .requester import Requester
from .tools import *

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
    def __init__(self, title=None, artist=None, proxies={}):
        self.title = title
        self.artist = artist
        self.proxies = proxies
        self.main_url = 'http://www.azlyrics.com'
        self.search_url = 'https://search.azlyrics.com'

    def getLyrics(self, title=None, artist=None, search=False, url=None, ext='txt', save=True, sleep=5):
        ''' 
        ### Reterives Lyrics for a given song details:
        #### args
        - `url`: url of the song's Azlyrics page
            - You don't have to set `artist` or `title` if you have the `url` of the lyrics
        - `title`:  song title
        - `artist`: singer name
        - `ext`: extension of the lyrics saved file, default is `.txt`
        - `save`: set to `False` if you don't wan't to save in a file
        - `sleep`: waiting time before sending a requests
            - It is advised to set it to more than `5` seconds to avoid being banned 
        '''

        link = None
        tmp_art, tmp_tit = artist, title

        ### Handling args
        if url:
            link = url
        else:
            if title and artist:
                title, artist = filtr(title), filtr(artist)
            else:
                if all([self.title, self.artist]):
                    title, artist = filtr(self.title), filtr(self.artist)
                else:
                    raise Exception("Both Artist and Title can't be empty!")
            link = '{}/lyrics/{}/{}.html'.format(self.main_url, artist, title)
        
        if sleep < 1:
            # THIS IS RISKY!
            sleep == 1
        time.sleep(sleep)
        
        page = self.get(link)
        search_done = False
        # Artist and Title Check
        try:
            artist = filtr(str(htmlFindAll(page)('div', class_='lyricsh')[0])[29:-23], True)
            title = filtr(str(htmlFindAll(page)('b')[1])[4:-5], True)
        except:
            if not search:
                raise Exception('Artist or Title not found!')
            else:
                if not url:
                    search_done = True
                    res = self.search(tmp_art, 'artists')
                    if res:
                        # Get first artist found
                        artist = res[0]['artist']
                        songs = self.search(tmp_tit, 'songs')
                        if songs:
                            for i in songs:
                                # Get song title if artist is same as found
                                if songs[i]['artist'] == artist:
                                    title = songs[i]['name']
                                    link = songs[i]['url']
                                    break
                        else:
                            raise Exception('Title Not Found!')
                    else:
                        raise Exception('Artist Not Found!')
    
        if search_done:
            artist, title = filtr(artist, True), filtr(title, True)
        
        page = self.get(link)
        
        lyrics = ParseLyric(page)

        ## Saving Lyrics
        if lyrics:
            if save:
                with open('{} - {}.{}'.format(title.title(), artist.title(), ext), 'w', encoding='utf-8') as f:
                    f.write(lyrics.strip())
            return lyrics.strip()

        return None

    def getSongs(self, artist=None, search=False):
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
        #### args
        - `artist`: singer name
            - If it's `None`, it will be set to what you initialized
        '''
        link = None

        tmp = artist

        if artist:
            artist = filtr(artist)
        else:
            if self.artist:
                artist = filtr(self.artist)
            else:
                raise Exception("Artist can't be empty!")

        if search:
            # Get url of artist searched
            arts = self.search(tmp, 'artists')
            if not arts:
                raise Exception('Artist not found!')
            link = arts[0]['url']

        if not link:
            link = '{}/{}/{}.html'.format(self.main_url, artist[0], artist)
        
        albums_page = self.get(link)

        return ParseSongs(albums_page)

    def search(self, query, category='songs', limit=1):
        '''
        ### Returns a dictionary of search results with their links:
        #### output:
         {
             
             `zero based index`: {
               "artist": "artist name",
               "name": "result type name",
               "url": "url for the result"
               }
        }
        #### args
        - `query`: text to pass in search
        - `category`: should be one of `('songs', 'albums', 'artists')`
            - default is `songs`
        - `limit`: number of pages to search through
        '''
        #https://search.azlyrics.com/search.php?q=[QUERY]&w=[TYPE]&p=[PAGE]

        if not query:
            raise Exception("Query can't be empty!")

        if not category in ['songs', 'albums', 'artists']:
            raise Exception("Category should be in ('songs', 'albums', 'artists')")

        page = self.get(
            '{}/search.php?q={}&w={}&p={}'.format(
                                            self.search_url,
                                            query,
                                            category,
                                            limit
                                                )
                                    )
                                
        return ParseSearch(page, limit, category)

from .requester import Requester
from .tools import *

class AZlyrics(Requester):
    """
    Fast and Secure API for AZLyrics.com

    Attributes:
        title (str): song title
        artist (str): singer name
        search_engine (str): search engine used to assist scraping lyrics
            - currently available: 'google', 'duckduckgo'
        accuracy (float): used to determine accuracy via jaro algorithm
        proxies (dict): if you want to use proxy while connecting to AZLyrics.com
    """
    
    def __init__(self, search_engine='', accuracy=0.6, proxies={}):
        self.title = ''
        self.artist = ''
        self.search_engine = search_engine
        
        self.accuracy = accuracy
        if not 0 < accuracy <= 1:
            self.accuracy = 0.6
        
        self.proxies = proxies

        self.lyrics_history = []
        self.lyrics = ''
        self.songs = {}

    def getLyrics(self, url=None, ext='txt', save=False, path='', sleep=3):
        """
        Reterive Lyrics for a given song details
        
        Parameters: 
            url (str): url of the song's Azlyrics page. 
            ext (str): extension of the lyrics saved file, default is ".txt".
            save (bool): allow to or not to save lyrics in a file.
            sleep (float): cooldown before next request.  
        
        Returns:
            lyrics (str): Lyrics of the detected song
        """

        if not self.artist + self.title:
            raise ValueError("Both artist and title can't be empty!")
        
        # Best cooldown is 5 sec
        time.sleep(sleep)

        link = url

        if not url:
            if self.search_engine:
                # If user can't remember the artist,
                # he can search by title only
                
                # Get AZlyrics url via Google Search
                link = GoogleGet(
                            self.search_engine,
                            self.accuracy,
                            self.get,
                            self.artist,
                            self.title,
                            0)
                if not link:
                    return 0
            else:
                # Sometimes search engines block you
                # If happened use the normal get method
                link = NormalGet(
                            self.artist,
                            self.title,
                            0)

        page = self.get(link)
        if page.status_code != 200:
            print('Error 404!')
            return 1

        # Getting Basic metadata from azlyrics
        metadata = [elm.text for elm in htmlFindAll(page)('b')]
        artist = filtr(metadata[0][:-7], True)
        title = filtr(metadata[1][1:-1], True)

        lyrics = ParseLyric(page)
        self.lyrics = lyrics.strip()

        # Saving Lyrics
        if lyrics:
            if save:
                # v3.0.2: Adding custom path
                p = os.path.join(
                                path,
                                '{} - {}.{}'.format(
                                                title.title(),
                                                artist.title(),
                                                ext
                                                )
                                )
                
                with open(p, 'w', encoding='utf-8') as f:
                    f.write(lyrics.strip())
            
            # Store lyrics for later usage
            self.lyrics_history.append(lyrics)
            return self.lyrics

        self.lyrics = 'No lyrics found :('
        return 2

    def getSongs(self, sleep=3):
        """
        Reterive a dictionary of songs with their links

        Parameters:
            sleep (float): cooldown before next request.  
        
        Returns:
            dict: dictionary of songs with their links
        """

        if not self.artist:
            raise Exception("Artist can't be empty!")
        
        # Best cooldown is 5 sec
        time.sleep(sleep)
        
        if self.search_engine:
            link = GoogleGet(
                        self.search_engine,
                        self.accuracy,
                        self.get,
                        self.artist,
                        '',
                        1)
            if not link:
                return {}
        else:
            link = NormalGet(
                        self.artist,
                        '',
                        1)
        
        albums_page = self.get(link)
        if albums_page.status_code != 200:
            print('Error 404!')
            return {}
        
        # Store songs for later usage
        self.songs = ParseSongs(albums_page)
        return self.songs
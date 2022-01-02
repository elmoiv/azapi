import bs4, re, time, os
from urllib.parse import quote
from .jaro import jaro_distance

letters = 'abcdefghijklmnopqrstuvwxyz0123456789'

def htmlFind(page):
    # v3.0
    # Changed page.text -> page.content.decode() to support variant unicodes
    soup = bs4.BeautifulSoup(
                        page.content.decode(),
                        "html.parser"
                        )
    return soup.find

def htmlFindAll(page):
    # v3.0
    # Changed page.text -> page.content.decode() to support variant unicodes
    soup = bs4.BeautifulSoup(
                        page.content.decode(),
                        "html.parser"
                        )
    return soup.findAll

def filtr(inpt, isFile=False):
    if isFile:
        return ''.join(i for i in inpt if i not in r'<>:"/\|?*')
    return ''.join(i.lower() for i in inpt if i.lower() in letters)

def normalGet(artist='', title='', _type=0):
    art, tit = filtr(artist), filtr(title)
    if _type:
        print('https://www.azlyrics.com/{}/{}.html'.format(art[0], art))
        return 'https://www.azlyrics.com/{}/{}.html'.format(art[0], art)
    return 'https://www.azlyrics.com/lyrics/{}/{}.html'.format(art, tit)

def googleGet(srch_eng, acc, get_func, artist='', title='', _type=0, proxies={}):
    # Encode artist and title to avoid url encoding errors
    data = artist + ' ' * (title != '' and artist != '') + title
    encoded_data = quote(data.replace(' ', '+'))

    # Perform a search (for accuracy) [Custom search engine]
    search_engines = {
        'google': 'https://www.google.com/search?q=',
        'duckduckgo': 'https://duckduckgo.com/html/?q='
    }

    slctd_srch_engn = 'google'
    if srch_eng in search_engines:
        slctd_srch_engn = srch_eng

    google_page = get_func('{}{}+site%3Aazlyrics.com'.format(
                                    search_engines[slctd_srch_engn],
                                    encoded_data
                                    ),
                            proxies
                            )
    
    # Choose between lyrics or song according to function used
    regex = [
        r'(azlyrics\.com\/lyrics\/(\w+)\/(\w+).html)',
        r'(azlyrics\.com\/[a-z0-9]+\/(\w+).html)'
    ]
    
    # ex result: [('azlyrics.com/t/taylorswift.html', 'taylorswift')]
    # result[0][0] = 'azlyrics.com/t/taylorswift.html'
    results = re.findall(
                        regex[_type],
                        google_page.text
                        )

    if len(results):
        # calculate jaro similarity for artist and title
        jaro_artist = 1.0
        jaro_title = 1.0
        
        if artist:
            jaro_artist = jaro_distance(
                                        artist.replace(' ', ''),
                                        results[0][1]
                                        )
        if title:
            jaro_title = jaro_distance(
                                        title.replace(' ', ''),
                                        results[0][2]
                                        )
        
        if jaro_artist >= acc and jaro_title >= acc:
            return 'https://www.' + results[0][0]
        else:
            print('Similarity <', acc)
    else:
        print(srch_eng.title(), 'found nothing!')
    
    return 0

# v3.0.5: Re-coded ParseLyrics to be more efficient
def parseLyric(page):
    divs = [i.text for i in htmlFindAll(page)('div', {'class': None})]
    return max(divs, key=len)

def parseSongs(page):
    songs = {}
    Parent = htmlFind(page)('div', {'id':'listAlbum'})
    if Parent:
        Raw_Data = Parent.findChildren()

        curType, curName, curYear = '', '', ''

        for elmnt in Raw_Data:

            # v3.0.3: Removed break after script due to google ads inside listAlbum
            # is using script tag, which results in not all songs retrieved
            #if elmnt.name == 'script':
            #    break
            
            # album info are inside divs
            if elmnt.name == 'div':
                if elmnt.text == 'other songs:':
                    curType, curName, curYear = 'Others', '', ''
                else:
                    # Separating to (album, name, year)
                    rgx = re.findall(r'(.*):\s"(.*)"\s\(([0-9]+)\)', elmnt.text)
                    if rgx:
                        curType, curName, curYear = rgx[0]
            if elmnt.name == 'a':
                songs[elmnt.text] = {
                    'year': curYear,
                    'album': curName,
                    'type': curType,
                    # Azlyrics puts hrefs with/without base url
                    'url': 'http://www.azlyrics.com' + elmnt['href'].strip('.') \
                            if elmnt['href'].startswith('/lyrics/') else elmnt['href']
                }
    # v 3.0
    # Some artists have no albums, so we cover this
    else:
        for div in htmlFindAll(page)('div', {'class':'listalbum-item'}):
            a = div.find('a')
            songs[a.text] = {
                'year': '',
                'album': '',
                'type': '',
                # v3.0.1: fix relative urls -> absolute url
                'url': 'http://www.azlyrics.com' + a['href'][2:] \
                        if a['href'][:2] == '..' else a['href']
                }
    return songs
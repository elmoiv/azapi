import bs4, re

letters = 'abcdefghijklmnopqrstuvwxyz0123456789'

def htmlFind(content):
    soup = bs4.BeautifulSoup(content.text, "html.parser")
    return soup.find

def htmlFindAll(content):
    soup = bs4.BeautifulSoup(content.text, "html.parser")
    return soup.findAll

def filtr(inpt, isFile=False):
    if isFile:
        return ''.join(i for i in inpt if i not in r'<>:"/\|?*')
    return ''.join(i.lower() for i in inpt if i.lower() in letters)

def ParseLyric(page):
    divs = htmlFindAll(page)('div')
    for div in divs:
        # Lyrics div has no class
        # So we fast check if there is a class or not
        try:
            div['class']
            continue
        except:
            pass
        # Almost all lyrics have more than one <br> tag
        found = div.find_all('br')
        if len(found) > 1:
            # Removing unnecessary lines
            return div.text[2:-1]

def ParseSongs(page):
    Parent = htmlFind(page)('div', {'id':'listAlbum'})

    Raw_Data = Parent.findChildren()

    songs = {}

    curType, curName, curYear = '', '', ''

    for elmnt in Raw_Data:
        # <script> is the first thing we face after finishing songs list so we break
        if elmnt.name == 'script':
            break
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
                # Azlyrics puts hrefs with/without base url so we cover this
                'url': 'http://www.azlyrics.com' + elmnt['href'][2:] if elmnt['href'][:2] == '..' else elmnt['href']
            }
    return songs

def ParseSearch(page, limit, cat):
    header = htmlFind(page)('div', {'class':'panel-heading'})
    if not header:
        return 'Nothing Found!'
    
    # Calculate page count
    page_count = int(header.text.split(' ')[3]) // 20

    limit = 1 if limit < 1 else page_count if limit > page_count else limit
    
    results = htmlFindAll(page)('td', {'class':'text-left visitedlyr'})

    data = {n:{} for n in range(len(results))}

    for n, result in enumerate(results):

        # adjust to category
        raw_text = result.text.split('\n')[1]
        if cat == 'songs':
            raw_text = raw_text.split('by')
            data[n]['artist'] = raw_text[-1][1:]
            data[n]['name'] = ' '.join(raw_text[0].split()[1:])
        if cat == 'albums':
            raw_text = raw_text.split('-')
            data[n]['artist'] = ' '.join(raw_text[0].split()[1:])
            data[n]['name'] = raw_text[1][1:]
        if cat == 'artists':
            raw_text = raw_text.split()
            data[n]['artist'] = ' '.join(raw_text[1:])
            data[n]['name'] = ''

        # Add url of the result
        for child in result.findChildren():
            if child.name == 'a':
                data[n]['url'] = child['href']
                break
        
    return data

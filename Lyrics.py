import requests
from bs4 import BeautifulSoup
import os

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus


def get_lyrics(song_name):

    song_name += ' metrolyrics'
    name = quote_plus(song_name)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
           '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    url = 'http://www.google.com/search?q=' + name

    result = requests.get(url, headers=hdr).text
    link_start = result.find('http://www.metrolyrics.com')

    if(link_start == -1):
        return("Lyrics not found on Metrolyrics")
        
    link_end = result.find('html', link_start + 1)
    link = result[link_start:link_end + 4]


    lyrics_html = requests.get(link, headers={
                               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel'
                               'Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, '
                               'like Gecko) Chrome/55.0.2883.95 Safari/537.36'
                               }
                               ).text

    soup = BeautifulSoup(lyrics_html, "lxml")
    raw_lyrics = (soup.findAll('p', attrs={'class': 'verse'}))
    paras = []
    try:
        final_lyrics = unicode.join(u'\n', map(unicode, raw_lyrics))
    except NameError:
        final_lyrics = str.join(u'\n', map(str, raw_lyrics))

    final_lyrics = (final_lyrics.replace('<p class="verse">', '\n'))
    final_lyrics = (final_lyrics.replace('<br/>', ' '))
    final_lyrics = final_lyrics.replace('</p>', ' ')
    return (final_lyrics)

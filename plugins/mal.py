import requests
import re
import textwrap
import urllib
from cloudbot import hook
from cloudbot.util import web, formatting, colors, http
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth

@hook.command('mal')
def malsearch(text, reply, bot):
    
    text = urllib.parse.quote(text)
    
    #grab our mal login
    
    try:
        user = bot.config.get("api_keys", {}).get("mal_user", None)
        password = bot.config.get("api_keys", {}).get("mal_pass", None)
    except:
        reply("No api key found.")
    
    url = 'https://myanimelist.net/api/anime/search.xml?q={}'.format(text)
    
    #try to request anime, reply if failed
    try:
        request = requests.get(url, auth=(user, password))
    except Exception as e:
        reply('Error: {}'.format(e))
    
    soup = BeautifulSoup(request.text)
    
    #a whole bunch of sorting
    title = http.strip_html(soup.find('title'))
    episodes = http.strip_html(soup.find('episodes'))
    if episodes == '0':
        episodes = '?'
    status = http.strip_html(soup.find('status'))
    score = http.strip_html(soup.find('score'))
    airtype = http.strip_html(soup.find('type'))
    start_date = http.strip_html(soup.find('start_date'))
    end_date = http.strip_html(soup.find('end_date'))
    
    #Has the anime ended? Yes.
    if end_date == '0000-00-00' and status is not 'Currently Airing':
        end_date = 'has not ended'
    #no but I know when.
    elif status == 'Currently Airing':
        end_date = 'will end {}'.format(http.strip_html(soup.find('end_date')))
    #no I don't know when.
    else:
        print(status, end_date)
        end_date = 'ended {}'.format(http.strip_html(soup.find('end_date')))
    
    #in case we want to ever output synopsis to irc
    synopsis = http.strip_html(http.strip_html(soup.find('synopsis')))
    length = len(synopsis)
    if length > 432 and length < 888:
        synopsis_1, synopsis_2 = textwrap.wrap(synopsis, 432)
    elif length > 864:
        synopsis_1, synopsis_2, synopsis_3 = textwrap.wrap(synopsis, 432)
    
    id = http.strip_html(soup.find('id'))
    
    url = web.shorten('https://' + urllib.parse.quote('myanimelist.net/anime/{}/{}'.format(id, title)))
    
    reply('{}, {}, {}, {} episodes. {}, started {}, {}. {}'.format(title, airtype, score, episodes, status, start_date, end_date, url))
    
    #more stuff we can add later for synopsis //its really spammy
    """if synopsis_1 is not None and synopsis_2 is not None and synopsis_3 is None:
        reply(synopsis_1)
        reply(synopsis_2)
    elif synopsis_1 is not None and synopsis_2 is not None and synopsis_3 is not None:
        reply(synopsis_1)
        reply(synopsis_2)
        reply(synopsis_3)
    else:
        reply(synopsis)"""

#same stuff except with manga instead
@hook.command('malm')
def malmsearch(text, reply, bot):
    
    text = urllib.parse.quote(text)

    try:
        user = bot.config.get("api_keys", {}).get("mal_user", None)
        password = bot.config.get("api_keys", {}).get("mal_pass", None)
    except:
        reply("No api key found.")

    url = 'https://myanimelist.net/api/manga/search.xml?q={}'.format(text)
    
    try:
        request = requests.get(url, auth=(user, password))
    except Exception as c:
        reply('Error: {}'.format(c))
    
    soup = BeautifulSoup(request.text)
    title = http.strip_html(soup.find('title'))
    chapters = http.strip_html(soup.find('chapters'))
    mtype = http.strip_html(soup.find('type'))
    score = http.strip_html(soup.find('score'))
    status = http.strip_html(soup.find('status'))
    start_date = http.strip_html(soup.find('start_date'))
    end_date = http.strip_html(soup.find('end_date'))

    if end_date == '0000-00-00' and status is not 'Publishing':
        end_date = 'has not ended'
    elif status == 'Publishing':
        end_date = 'will end on {}'.format(end_date)
    else:
        end_date = 'ended {}'.format(end_date)
    
    id = http.strip_html(soup.find('id'))
    url = web.shorten('https://' + urllib.parse.quote('myanimelist.net/manga/{}/{}'.format(id, title)))
    
    reply('{}, {}, {}, {} chapters. {}, started {}, {}. {}'.format(title, mtype, score, chapters, status, start_date, end_date, url))


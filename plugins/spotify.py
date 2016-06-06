import re
from cloudbot.util import http, web
from cloudbot import hook
from urllib.parse import urlencode
"""
def sptfy(text, sptfy=False):
    shortenurl = "http://sptfy.com/index.php"
    data = urlencode({'longUrl': text, 'shortUrlDomain': 1, 'submitted': 1, "shortUrlFolder": 6, "customUrl": "",
                      "shortUrlPassword": "", "shortUrlExpiryDate": "", "shortUrlUses": 0, "shortUrlType": 0})
    try:
        soup = http.get_soup(shortenurl, post_data=data, cookies=True)
    except:
        return text
    try:
        link = soup.find('div', {'class': 'resultLink'}).text.strip()
        return link
    except:
        message = "Unable to shorten URL: %s" % \
                  soup.find('div', {'class': 'messagebox_text'}).find('p').text.split("<br/>")[0]
        return web.shorten(text)
"""
@hook.command('sp')
@hook.command
def spotify(text):
    """spotify <song> -- Search Spotify for <song>"""
    try:
        data = http.get_json("http://api.spotify.com/v1/search?q=foo&type=track", q=text.strip())
    except Exception as e:
        return "Could not get track information: {}".format(e)

    try:
        track = data["tracks"]["items"][0]["external_urls"]["spotify"]
    except IndexError:
        return "Could not find track."
    url = web.shorten(track)
    uri = data["tracks"]["items"][0]["uri"]
    return "\x02{}\x02 by \x02{}\x02 - \x02{}\x02, {}".format(data["tracks"]["items"][0]["name"],
                                                           data["tracks"]["items"][0]["artists"][0]["name"], url, uri)


@hook.command
def spalbum(text):
    """spalbum <album> -- Search Spotify for <album>"""
    try:
        data = http.get_json("http://api.spotify.com/v1/search?q=foo&type=album", q=text.strip())
    except Exception as e:
        return "Could not get album information: {}".format(e)

    try:
        albumurl = data["albums"]["items"][0]["external_urls"]["spotify"]
    except IndexError:
        return "Could not find album."
    url = web.shorten(albumurl)
    uri = data["albums"]["items"][0]["uri"]
    return "\x02{}\x02 - \x02{}\x02 - \x02{}\x02".format(data["albums"]["items"][0]["name"], url, uri)


@hook.command
def spartist(text):
    """spartist <artist> -- Search Spotify for <artist>"""
    try:
        data = http.get_json("http://api.spotify.com/v1/search?q=foo&type=artist", q=text.strip())
    except Exception as e:
        return "Could not get artist information: {}".format(e)

    try:
        artisturl = data["artists"]["items"][0]["external_urls"]["spotify"]
    except IndexError:
        return "Could not find artist."
    url = web.shorten(artisturl)
    uri = data["artists"]["items"][0]["uri"]
    return "\x02{}\x02 - \x02{}\x02 - \x02{}\x02".format(data["artists"]["items"][0]["name"], url, uri)
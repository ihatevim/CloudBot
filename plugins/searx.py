from cloudbot import hook
from cloudbot.util import http, formatting
import requests
#credits to Takeru/Seth
#<Takeru> ihatevim, I wrote up a plugin to replace the google CSE and bing since they each only give you 100 requests a day
@hook.command("searchx", "searx", "sx")
def searx(text):
    """<query> - returns the first searx search result for <query>"""
    search = text
    pre = ('https://searx.me/?q=' + search + '&format=json&category_general=1&pageno=1')
    r = requests.get(pre)
    parsed = (r.json())
    url = (parsed['results'][0]['url'])
    title = (parsed['results'][0]['title'])
    return(url + " - " + title)
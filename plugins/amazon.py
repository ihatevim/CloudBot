import urllib.request
import re
from bs4 import BeautifulSoup

from cloudbot import hook
from cloudbot.util import web, formatting, colors, http


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537a'} 

@hook.command('az')
@hook.command
def amazonsearch(text):
    url = "http://www.amazon.com/s/url=search-alias%3Daps&field-keywords={}".format(text.replace(" ", "%20"))
    try:
        request = urllib.request.Request(url, None, headers)
        page = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(page, 'lxml')
        soup = soup.find('li', attrs={'id': ('result_1')})
        title = soup.find('h2')
        title = title.renderContents()
        url = soup.find('a', attrs={'class': ('a-link-normal s-access-detail-page a-text-normal')})
        url = url.get('href')
        try:
            price = soup.find('div', attrs={'class': ('a-column a-span7')})
            price = http.strip_html(price.find('span'))
        except AttributeError:
            price = soup.find('span', attrs={'class': ('a-size-medium a-color-price')})
            price = http.strip_html(price)
        azid = re.match(r'^.*\/dp\/([\w]+)\/.*',url).group(1)
    except AttributeError as e:
        return e

    return u'(\x02{}\x02) {}, https://amzn.com/{}'.format(price, title.decode('ascii', 'ignore'), azid)

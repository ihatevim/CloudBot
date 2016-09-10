import urllib.request
import re
from bs4 import BeautifulSoup

from cloudbot import hook
from cloudbot.util import web, formatting, colors, http


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537a'} 

<<<<<<< HEAD
@hook.command('az')
@hook.command
def amazonsearch(text):
    url = "http://www.amazon.com/s/url=search-alias%3Daps&field-keywords={}".format(text.replace(" ", "%20"))
=======
AMAZON_RE = re.compile(""".*ama?zo?n\.(com|co\.uk|com\.au|de|fr|ca|cn|es|it|in)/.*/(?:exec/obidos/ASIN/|o/|gp/product/|
(?:(?:[^"\'/]*)/)?dp/|)(B[A-Z0-9]{9})""", re.I)

# Feel free to set this to None or change it to your own ID.
# Or leave it in to support CloudBot, it's up to you!
AFFILIATE_TAG = "cloudbot-20"


@hook.regex(AMAZON_RE)
def amazon_url(match):
    cc = match.group(1)
    asin = match.group(2)
    return amazon(asin, _parsed=cc)


@hook.command("amazon", "az")
def amazon(text, _parsed=False):
    """<query> -- Searches Amazon for query"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Referer': 'http://www.amazon.com/'
    }
    params = {
        'url': 'search-alias',
        'field-keywords': text.strip()
    }
    if _parsed:
        # input is from a link parser, we need a specific URL
        request = requests.get(SEARCH_URL.format(_parsed), params=params, headers=headers)
    else:
        request = requests.get(SEARCH_URL.format(REGION), params=params, headers=headers)

    soup = BeautifulSoup(request.text)

    # check if there are any results on the amazon page
    results = soup.find('div', {'id': 'atfResults'})
    if not results:
        if not _parsed:
            return "No results found."
        else:
            return

    # get the first item from the results on the amazon page
    results = results.find('ul', {'id': 's-results-list-atf'}).find_all('li', {'class': 's-result-item'})
    item = results[0]
    asin = item['data-asin']

    # here we use dirty html scraping to get everything we need
    title = formatting.truncate(item.find('h2', {'class': 's-access-title'}).text, 60)
    tags = []

    # tags!
    if item.find('i', {'class': 'a-icon-prime'}):
        tags.append("$(b)Prime$(b)")

    if item.find('i', {'class': 'sx-bestseller-badge-primary'}):
        tags.append("$(b)Bestseller$(b)")

    # we use regex because we need to recognise text for this part
    # the other parts detect based on html tags, not text
    if re.search(r"(Kostenlose Lieferung|Livraison gratuite|FREE Shipping|Envío GRATIS"
                 r"|Spedizione gratuita)", item.text, re.I):
        tags.append("$(b)Free Shipping$(b)")

    price = item.find('span', {'class': ['s-price', 'a-color-price']}).text

    # use a whole lot of BS4 and regex to get the ratings
>>>>>>> refs/remotes/CloudBotIRC/master
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

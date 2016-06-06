from cloudbot import hook
from cloudbot.util import database, http
import random
from cloudbot.util import textgen
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
# RATINGS

# .BS WOULD DISPLAY RATING AND TOTAL VOTES
#TYPE, NICK, VOTES, VOTERS

### Battlestations
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36','Upgrade-Insecure-Requests': '1','x-runtime': '148ms'}
@hook.command(autohelp=False)
def battlestation(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "battlestation <url | @ person> -- Shows a users Battlestation."
    if text:
        if  "http" in text:
            database.set(db,'users','battlestation',text.strip(),'nick',nick)
            notice("Saved your battlestation.")
            return
        elif 'del' in text:
            database.set(db,'users','battlestation','','nick',nick)
            notice("Deleted your battlestation.")
            return
        else:
            if '@' in text: nick = text.split('@')[1].strip()
            else: nick = text.strip()

    result = database.get(db,'users','battlestation','nick',nick)
    if result:
        return '{}'.format(result)
    else:
        if not '@' in text: notice(battlestation.__doc__)
        return 'No battlestation saved for {}.'.format(nick)

### Desktops
@hook.command(autohelp=False)
def desktop(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "desktop http://url.to/desktop | @ nick -- Shows a users Desktop."
    if text:
        if  "http" in text:
            database.set(db,'users','desktop',text.strip(),'nick',nick)
            notice("Saved your desktop.")
            return
        elif 'del' in text:
            database.set(db,'users','desktop','','nick',nick)
            notice("Deleted your desktop.")
            return
        else:
            if '@' in text: nick = text.split('@')[1].strip()
            else: nick = text.strip()

    result = database.get(db,'users','desktop','nick',nick)
    if result:
        return '{}'.format(result)
    else:
        if not '@' in text: notice(desktop.__doc__)
        return 'No desktop saved for {}.'.format(nick)

"""
### Greeting
@hook.command('intro', autohelp=False)
@hook.command(autohelp=False)
def greeting(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "greet <message | @ person> -- Shows a users Greeting."
    try:
        if not text or '@' in text:
            if '@' in text: nick = text.split('@')[1].strip()
            result = database.get(db,'users','greeting','nick',nick)
            if result:
                return '{}'.format(result)
            else:
                if not '@' in text: notice(greeting.__doc__)
                return 'No greeting saved for {}.'.format(nick)
        elif 'del' in text:
            database.set(db,'users','greeting','','nick',nick)
            notice("Deleted your greeting.")
        else:
            database.set(db,'users','greeting','{} '.format(text.strip().replace("'","")),'nick',nick)
            notice("Saved your greeting.")
        return
    except: return "Uwaaahh~~?"
"""

### Waifu & Husbando
@hook.command(autohelp=False)
def waifu(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "waifu <waifu | @ person> -- Shows a users Waifu or Husbando."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','waifu','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(waifu.__doc__)
            return 'No waifu saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','waifu','','nick',nick)
        notice("Deleted your waifu.")
    else:
        database.set(db,'users','waifu','{} '.format(text.strip()),'nick',nick)
        notice("Saved your waifu.")
    return

@hook.command(autohelp=False)
def husbando(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "husbando <husbando | @ person> -- Shows a users husbando or Husbando."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','husbando','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(husbando.__doc__)
            return 'No husbando saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','husbando','','nick',nick)
        notice("Deleted your husbando.")
    else:
        database.set(db,'users','husbando','{} '.format(text.strip()),'nick',nick)
        notice("Saved your husbando.")
    return

@hook.command(autohelp=False)
def imouto(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "imouto <imouto | @ person> -- Shows a users imouto or Husbando."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','imouto','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(imouto.__doc__)
            return 'No imouto saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','imouto','','nick',nick)
        notice("Deleted your imouto.")
    else:
        database.set(db,'users','imouto','{} '.format(text.strip()),'nick',nick)
        notice("Saved your imouto.")
    return

@hook.command(autohelp=False)
def daughteru(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "daughteru <daughteru | @ person> -- Shows a users daughteru."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','daughteru','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(imouto.__doc__)
            return 'No daughteru saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','daughteru','','nick',nick)
        notice("Deleted your daughteru.")
    else:
        database.set(db,'users','daughteru','{} '.format(text.strip()),'nick',nick)
        notice("Saved your daughteru.")
    return


### Desktops
@hook.command(autohelp=False)
def birthday(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "birthday <01/01/2001> | <@ person> -- Shows a users Birthday."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','birthday','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(birthday.__doc__)
            return 'No birthday saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','birthday','','nick',nick)
        notice("Deleted your birthday.")
    else:
        database.set(db,'users','birthday','{} '.format(text.strip()),'nick',nick)
        notice("Saved your birthday.")
    return
"""
@hook.command(autohelp=False)
def horoscope(text, db=None, notice=None, nick=None):
   # """"""
    save = False
    database.init(db)

    if '@' in text:
        nick = text.split('@')[1].strip()
        sign = database.get(db,'users','horoscope','nick',nick)
        if not sign: return "No horoscope sign stored for {}.".format(nick)
    else:
        sign = database.get(db,'users','horoscope','nick',nick)
        if not text:
            if not sign:
                notice(horoscope.__doc__)
                return
        else:
            if not sign: save = True
            if " save" in text: save = True
            sign = text.split()[0]

    url = "http://www.astrology.com/horoscope/daily/%s.html" % sign
    try:
        request = urllib.request.Request(url, None, headers)
        page = urllib.request.urlopen(request).read()
        result = BeautifulSoup(page, 'lxml')
        horoscopetxt = http.strip_html(str(result.find('div', attrs={'class':('page-horoscope-text')})))
    except: return "Check your spelling, acronyms and short forms are not accepted."


    if sign and save: database.set(db,'users','horoscope',sign,'nick',nick)

    return "{}".format(horoscopetxt)
"""

@hook.command(autohelp=False)
def homescreen(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "homescreen <url | @ person> -- Shows a users homescreen."
    if "http" in text:
        database.set(db,'users','homescreen',text.strip(),'nick',nick)
        notice("Saved your homescreen.")
        return
    elif 'del' in text:
        database.set(db,'users','homescreen','','nick',nick)
        notice("Deleted your homescreen.")
        return
    elif not text:
        homescreen = database.get(db,'users','homescreen','nick',nick)
    else:
        if '@' in text: nick = text.split('@')[1].strip()
        else: nick = text.strip()

    homescreen = database.get(db,'users','homescreen','nick',nick)
    if homescreen:
        return '{}: {}'.format(nick,homescreen)
    else:
        # notice(homescreen.__doc__)
        return 'No homescreen saved for {}.'.format(nick)

@hook.command(autohelp=False)
def snapchat(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "snapchat <snapchatname | @ person> -- Shows a users snapchat name."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','snapchat','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(snapchat.__doc__)
            return 'No snapchat saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','snapchat','','nick',nick)
        notice("Deleted your snapchat.")
    else:
        database.set(db,'users','snapchat','{} '.format(text.strip()),'nick',nick)
        notice("Saved your snapchat.")
    return

@hook.command('soc', autohelp=False)
@hook.command(autohelp=False)
def socialmedia(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "socialmedia <socialmedianames | @ person> -- Shows a users social medias names."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','socialmedias','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(snapchat.__doc__)
            return 'No social medias saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','socialmedias','','nick',nick)
        notice("Deleted your social medias.")
    else:
        database.set(db,'users','socialmedias','{} '.format(text.strip()),'nick',nick)
        notice("Saved your social medias.")
    return

@hook.command(autohelp=False)
def myanime(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "myanime <mal name | @ person> -- Shows a users myanimelist profile."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','mal','nick',nick)
        if result:
            return '{}: http://myanimelist.net/animelist/{}'.format(nick,result)
        else:
            if not '@' in text: notice(mal.__doc__)
            return 'No mal saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','mal','','nick',nick)
        notice("Deleted your mal.")
    else:
        database.set(db,'users','mal','{} '.format(text.strip()),'nick',nick)
        notice("Saved your mal.")
    return

@hook.command(autohelp=False)
def mymanga(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "mymanga <mal name | @ person> -- Shows a users myanimelist profile."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','mal','nick',nick)
        if result:
            return '{}: http://myanimelist.net/mangalist/{}'.format(nick,result)
        else:
            if not '@' in text: notice(mal.__doc__)
            return 'No mal saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','mal','','nick',nick)
        notice("Deleted your mal.")
    else:
        database.set(db,'users','mal','{} '.format(text.strip()),'nick',nick)
        notice("Saved your mal.")
    return

@hook.command(autohelp=False)
def selfie(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "selfie <url | @ person> -- Shows a users selfie."
    if text:
        if  "http" in text:
            database.set(db,'users','selfie',text.strip(),'nick',nick)
            notice("Saved your selfie.")
            return
        elif 'del' in text:
            database.set(db,'users','selfie','','nick',nick)
            notice("Deleted your selfie.")
            return
        else:
            if '@' in text: nick = text.split('@')[1].strip()
            else: nick = text.strip()

    result = database.get(db,'users','selfie','nick',nick)
    if result:
        return '{}'.format(result)
    else:
        if not '@' in text: notice(selfie.__doc__)
        return 'No selfie saved for {}.'.format(nick)

@hook.command("steamname", autohelp=False)
def steam(text, nick=None, conn=None, chan=None,db=None, notice=None):
    "steam <steam | @ person> -- Shows a users steam information."

    if not text or '@' in text:
        if '@' in text: nick = text.split('@')[1].strip()
        result = database.get(db,'users','steam','nick',nick)
        if result:
            return '{}'.format(result)
        else:
            if not '@' in text: notice(steam.__doc__)
            return 'No steam information saved for {}.'.format(nick)
    elif 'del' in text:
        database.set(db,'users','steam','','nick',nick)
        notice("Deleted your steam information.")
    else:
        database.set(db,'users','steam','{} '.format(text.strip()),'nick',nick)
        notice("Saved your steam information.")
    return


    ###Old
    #result = unicode(result, "utf8").replace('flight ','')

    # try: sign = db.execute("select horoscope from users where nick=lower(?)", (nick,)).fetchone()[0]
    # except: save = True

    #db.execute("UPSERT INTO users(nick, horoscope) VALUES (?,?)",(nick.lower(), sign,))
    #db.commit()

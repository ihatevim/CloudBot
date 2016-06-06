from cloudbot import hook
from cloudbot.util import http, database
import random
import urllib.request, urllib.parse, urllib.error
#thanks to edwardslabs
# HONK HONK
actions = {
    "honk":["honked at", "honking"],
    "pet":["pet", "petting"],
    "diddle":["diddled", "diddling"],
    "spank":["spanked", "spanking"],
    "rape": ["raped", "raping"]
}

def citation(db,chan,nick,reason):
    fine = random.randint(1, 500)
    try: totalfines = int(database.get(db,'users','fines','nick',nick)) + fine
    except: totalfines = 0 + fine
    database.set(db,'users','fines',totalfines,'nick',nick)
    return "PRIVMSG {} :\x01ACTION fines {} \x02${}\x02 {}. You owe: \x0304${}\x02\x01".format(chan, nick, fine, reason, totalfines)


@hook.command("rape", "spankk", "diddle", "pet", "honk", autohelp=False)
def honk(text, nick=None, conn=None, chan=None, db=None, triggered_command=None):
    "honk <nick> -- Honks at someone."
    target = text.strip()
    command = triggered_command
    if len(text) == 0:
        if random.randint(1, 3) == 2: 
            out = citation(db,chan,nick,"for {}".format(actions[command][1]))
        else:
            out = "PRIVMSG {} :\x01ACTION {}s {}\x01".format(chan, command, nick)
    else:
        randnum = random.randint(1, 4)
        if randnum == 1: 
            out = citation(db,chan,nick,"for {}".format(actions[command][1]))
        elif randnum == 2: 
            out = citation(db,chan,target,"for being too lewd and getting {}".format(actions[command][0]))
        else:
            out = "PRIVMSG {} :\x01ACTION {}s {}\x01".format(chan, command, target)
    conn.send(out)


@hook.command(autohelp=False)
def owed(text, nick=None, conn=None, chan=None,db=None):
    """owe -- shows your total fines"""
    if '@' in text: nick = text.split('@')[1].strip()
    fines = database.get(db,'users','fines','nick',nick)
    if not fines: fines = 0
    if fines <= 0:
        return '\x02{} owes: \x0309${}\x02'.format(nick,fines)
    else:
        return '\x02{} owes: \x0304${}\x02'.format(nick,fines)

@hook.command(autohelp=False)
def pay(text, nick=None, conn=None, chan=None,db=None):
    """pay -- pay your fines"""
    return '\x02Donate to infinitys paypal to pay the fees! \x02'


# VENDINGMACHINE
colors = ([
    ('red',         '\x0304'),
    ('orange',      '\x0307'),
    ('yellow',      '\x0308'),
    ('green',       '\x0309'),
    ('cyan',        '\x0303'),
    ('light blue',  '\x0310'),
    ('royal blue',  '\x0312'),
    ('blue',        '\x0302'),
    ('magenta',     '\x0306'),
    ('pink',        '\x0313'),
    ('maroon',      '\x0305'),
    ('super shiny', '\x03')
])

items = ([
    ('pantsu','used pair of'),
    ('dragon dildo', 'slightly used'),
    ('tfwnogf tears direct from ledzeps feels', 'vial of'),
    ('fursuit','cum stained'),
    ('girlfriend', 'self-inflatable'),
    ('otter suit', 'lube covered slippery'),
    ('dogecoin to call someone that cares', 'worthless'),
    ('condom that doesnt fit and will never be used', 'magnum XXL'),
    ('loli', 'miniature'),
    ("LeDZeP to follow you around and >tfwnogf",'emotionally unstable'),
    ('rimu job that feels like trying to start a fire with sandpaper','rough and tough')
])

@hook.command(autohelp=False)
def vendingmachine(text, nick=None, action=None):
    if text: nick = text
    colornum = random.randint(0, len(colors) - 1)
    itemnum = random.randint(0, len(items) - 1)
    action("dispenses one {} {}{} {}\x03 for {}".format(items[itemnum][1], colors[colornum][1],colors[colornum][0],items[itemnum][0], nick))
    return


# MISC
@hook.command("daki", "hug", autohelp=False)
def hug(text, nick=None):
    "hug <nick> -- hugs someone"
    if not text: text = nick
    return '\x02\x034♥♡❤♡♥\x03 {} \x034♥♡❤♡♥\x03\x02'.format(text)


@hook.command(autohelp=False)
def kiss(text, nick=None):
    "hug <nick> -- hugs someone"
    if not text: text = nick
    return '(づ｡◕‿‿◕｡)づ\x02\x034。。・゜゜・。。・゜❤ {} ❤\x03\x02 '.format(text)

    

@hook.regex(r'^\[(.*)\]$')
@hook.command(autohelp=False)
def intensify(text):
    "intensify <word> -- [EXCITEMENT INTENSIFIES]"
    try: word = text.upper()
    except: word = text.group(1).upper()
    return '\x02[{} INTENSIFIES]\x02'.format(word)


@hook.command(autohelp=False)
def increase(text):
    "increase"
    return '\x02[QUALITY OF CHANNEL SIGNIFICANTLY INCREASED]\x02'


@hook.command(autohelp=False)
def decrease(text):
    "decrease"
    return '\x02[QUALITY OF CHANNEL SIGNIFICANTLY DECREASED]\x02'


@hook.command(autohelp=False)
def pantsumap(text, chan=None, notice=None):
    if chan == "#pantsumen": notice(("Pantsumen Map: http://tinyurl.com/clx2qeg\r\n").encode('utf-8', 'ignore'))
    return

@hook.command("tits", "vagina", "anus", "penis", autohelp=False)
def penis(text, nick=None, triggered_command=None):
    "penis <nicks> -- Analyzes Penis's"
    command = triggered_command
    if not text: text = nick
    if 'penis' in command: url = 'http://en.inkei.net/{}'.format('!'.join(text.split(' ')))
    else: url = 'http://en.inkei.net/{}/{}'.format(command,'!'.join(text.split(' ')))
    return url


@hook.command("anhero", "sudoku", autohelp=False)
def sudoku(text, conn=None, chan=None, nick=None, say=None):
    "up -- Makes the bot kill you in [channel]. "\
    "If [channel] is blank the bot will op you in "\
    "the channel the command was used in."
    say("Sayonara bonzai-chan...")
    conn.send("KICK {} {}".format(chan, nick)) 
    return

@hook.command("storyofrincewindscat", autohelp=False)
def storyofpomfface(text, action=None):
   action(':O C==3')
   action(':OC==3')
   action(':C==3')
   action(':C=3')
   action(':C3')
   action(':3')
   return


@hook.regex(r'^(same)$')
def same(text):
    "same -- dont feel left out"
    if random.randint(1, 5) == 3: return 'butts'
    else: return 'same'


@hook.regex(r'^(HUEHUEHUE)$')
@hook.regex(r'^(huehuehue)$')
def huehuehue(text):
    "huehuehue -- huebaru?"
    return text.group(0)


@hook.regex(r'^(TETETE)$')
@hook.regex(r'^(tetete)$')
def tetete(text, nick=None):
    return 'tetete {}{}{}'.format(nick, nick, nick)


# @hook.regex(r'^(^)$')
# def agree(text):
#     return "^"


woahs = ([
    ('woah'),
    ('woah indeed'),
    ('woah woah woah!'),
    ('keep your woahs to yourself')
])
@hook.regex(r'.*([W|w]+[H|h]+[O|o]+[A|a]+).*')
@hook.regex(r'.*([W|w]+[O|o]+[A|a]+[H|h]+).*')
def woah(text, nick=None):
    if random.randint(0, 4) == 0:
        return woahs[random.randint(0, len(woahs) - 1)].replace('woah',text.group(1))


@hook.regex(r'.*([L|l]+[I|i]+[N|n]+[U|u]+[X|x]).*')
def interject(nick=None):
    if random.randint(0, 12) == 0:
        return "I'd Just Like To Interject For A Moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX." 
        # \
        # "Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of triggered_commands, the version of GNU which is widely used today is often called “Linux”, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project. There really is a Linux, and these people are using it, but it is just a part of the system they use. \n" \
        # "Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called “Linux” distributions are really distributions of GNU/Linux. "


@hook.command
def hack(text):
    return 'hacking...'

@hook.command
def pdawg(text):
    return '<PDawg> i suck cocks...'

# 'is trying to steal your girl','or else Im going to fuck her in the ass tonight lil bitch!'

exercises = [
    "pushups",
    "handstand pushups",
    "squats",
    "curls",
    "dips",
    "crunches",
    "minutes of planking",
    "burpees",
    "jumping jacks",
    "minutes of vigorous fapping"
    ]

fitnesslevels = [
    "swole",
    "fit",
    "cut",
    "ripped",
    "infinity'd",
    "jacked"
    ]

motivators = [
    "bitch",
    "you hungry skeleton",
    "you puny mortal",
    "you weak pathetic fool",
    "you wat wannabe"
    ]

@hook.command(autohelp=False)
def workout(text,reply=None,triggered_command=None,):
    if not text: text = 'you'
    else: text = text.replace('@','').strip()
    reply('wants {} to get {} as fuck, do {} {} now {}!'.format(text,random.choice(fitnesslevels),random.randint(1, 50),random.choice(exercises),random.choice(motivators)))

@hook.command("squats", "pushups", autohelp=False)
def pushups(text,reply=None,triggered_command=None):
    activity = triggered_command
    if not text: text = 'you'
    else: text = text.replace('@','').strip()
    reply('wants {} to get swole as fuck, do {} {} now bitch!'.format(text,random.randint(1, 50),activity))





@hook.command
def room(text, conn=None):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    users = text.split()
    channel = "#rm-"
       
    for i in range(1,6):
        channel = channel + random.choice(letters)

    conn.send("JOIN " + channel)
    
    for user in users:
        conn.send("INVITE " + user + " " + channel)


@hook.command(autohelp=False)
def madoka(text):
    return 'Madoka_Miku has looked at infinitys abs {} times today.'.format(random.randint(1, 500))

"""@hook.command(autohelp=False)
def drink(text,me=None):
    me('Drinks {}, and it was delicious. mmmmmmmmmmmmmmmm'.format(text))
"""
# var replies = ['faggot','i ought to fuk u up m8','1v1 me','do u evn lift','ur mom','consider urself trolld','ur mom iz gay','stfu fagget','omg nub','u hax i repert u','my dad works for this site so I would be nice if I were you','ill rek u','get rekt scrub','u r gay'];


# .sue

@hook.command(autohelp=False)
def cayoot(text, nick=None):
    if not text: text = nick
    return '{} is cayoot!'.format(text)

@hook.command(autohelp=False)
def spit(text, nick=None, action=None):
    if not text: text = nick
    action('spits on {} like a dirty whore'.format(text))



# @hook.command('siid')
# @hook.command(autohelp=False)
# def sleepytime(text, chan=None, conn=None, notice=None):
#     "kick [channel] <user> [reason] -- Makes the bot kick <user> in [channel] "\
#     "If [channel] is blank the bot will kick the <user> in "\
#     "the channel the command was used in."
#     user = 'siid'
#     out = "KICK %s %s" % (chan, user)
#     reason = "sleepytime!"
#     out = out + " :" + reason
#     notice("Attempting to kick %s from %s..." % (user, chan))
#     conn.send(out)


# @hook.command(autohelp=False,channeladminonly=True)
# def touhouradio(text, chan=None, notice=None, bot=None):
#     "disabled -- Lists channels's disabled commands."
#     url = "http://booru.touhouradio.com/post/list/%7Bchannel%7C%23pantsumen%7D/1"
#     html = http.get_html(url)
# 
#     link = html.xpath("//div[@id='main']//a/@href")[0]
#     #COMPARE TO DB
#     image = http.unquote(re.search('.+?imgurl=(.+)&imgrefurl.+', link).group(1))
#     return image

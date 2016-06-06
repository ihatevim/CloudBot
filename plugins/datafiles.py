# -*- coding: utf-8 -*-
from cloudbot import hook
from cloudbot.util import textgen
import random
from random import randint
import json

color_codes = {
    "<r>": "\x02\x0305",
    "<g>": "\x02\x0303",
    "<y>": "\x02"
}

with open("data/yiffs.txt") as f:
    yiffs = [line.strip() for line in f.readlines() if not line.startswith("//")]

with open("data/lewd.txt") as f:
    lewds = [line.strip() for line in f.readlines() if not line.startswith("//")]


def get_generator(_json, variables):
    data = json.loads(_json)
    return textgen.TextGenerator(data["templates"], data["parts"], variables=variables)


def send_phrase(text,attack,nick,conn,reply,notice,chan):
    target = text.strip()
    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot slap itself, slap them
    if target.lower() == conn.nick.lower() or target.lower() == "itself": target = nick

    values = {"user": target,"nick": conn.nick, "channel": chan, "yiffer": nick}
    #if text.split(" ")[-1].isdigit: phrase = attack[int(text.split(" ")[-1].strip())-1]
    #else:
    phrase = random.choice(attack)
    # act out the message
    reply(phrase.format(**values))
    return


@hook.command(autohelp=False)
def yiff(text, action=None, nick=None, conn=None, notice=None, chan=None):
    """yiff <user> -- yiffs <user>."""
    send_phrase(text,yiffs,nick,conn,action,notice, chan)
    return


@hook.command(autohelp=False)
def lewd(text, action=None, nick=None, conn=None, notice=None, chan=None):
    """lewd <user> -- lewd <user>."""
    if len(text) == 0:
        return 'ヽ(◔ ◡ ◔)ノ.･ﾟ*｡･+☆LEWD☆'
    else:
        send_phrase(text,lewds,nick,conn,action,notice, chan)
    return

def get_filename(action,notice):
    if 'loli' in action: action = 'lolis'
    elif 'kek' in action: action = 'keks'
    elif 'moist' in action: action = 'moists'
    elif 'lewd' in action: action = 'lewds'
    elif 'qt' in action: action = 'qts'
    elif 'urmom' in action: action = 'urmom'
    elif 'honry' in action: action = 'old'
    elif 'old' in action: action = 'old'
    elif 'troll' in action: action = 'troll'
    elif 'gain' in action: action = 'gainz'
    elif 'nsfw' in action: action = 'nsfw'
    else:
        notice('Invalid action')
        return
    return action

@hook.command
def add(text,notice=None, channeladminonly=True):
    """add <type> <data> -- appends <data> to <type>.txt"""
    #text = text.split('add')[1]
    action = text.split(' ')[0]
    text = text.replace(action,'').strip()
    action=get_filename(action,notice)

    with open('data/{}.txt'.format(action), 'a') as file:
        file.write(u'{}\n'.format(text).encode('utf-8'))

    notice('{} added.'.format(action))
    file.close()
    return

def process_text(text,name,notice):
    # if not text or text is int:
    if 'add' in text:
        add(text,name,notice)
    else:
        with open("data/{}.txt".format(name)) as file:
            lines = [line.strip() for line in file.readlines() if not line.startswith("//")]
        linecount = len(lines) - 1

        if text and text.isdigit(): num = int(text) - 1
        else: num = randint(0,linecount)

        if num > linecount or num < 0:
            return "Theres nothing there baka"

        reply='\x02[{}/{}]\x02 {}'.format(num+1,linecount+1,lines[num])

        file.close()
        lines = []
        return reply


    # else:
    #     action = text.split(' ')[0]
    #     text = text.replace(action,'').strip()
    #     if "add" in text and text:
    #         with open('plugins/data/{}.txt'.format(name), 'a') as file:
    #             file.write(u'{}\n'.format(text).encode('utf-8'))
    #         file.close()


# def process_text(text,name,notice):
#     num = -1
#     if text:
#         action = text.split(' ')[0]
#         text = text.replace(action,'').strip()

#         if action.isdigit(): num = int(action) - 1
#         elif text.isdigit(): num = int(text) - 1

#         elif 'add' in action:
#             if 'http:' in text:
#                 with open('plugins/data/{}.txt'.format(name), 'a') as file:
#                     file.write(u'{}\n'.format(text).encode('utf-8'))
#                 notice('{} added.'.format(action))
#                 file.close()
#                 return
#             else:
#                 notice('No image to add.')
#                 return
#         elif 'del' in action:
#             num = int(text) - 1
#             notice('Deleted {}: {}.'.format(action,text))
#             with open("plugins/data/{}.txt".format(name)) as file:
#                 lines = [line.strip() for line in file.readlines() if not line.startswith("//")]
#                 lines = lines.replace(lines[num],'')
#             print "deleting"


#     with open("plugins/data/{}.txt".format(name)) as file:
#         lines = [line.strip() for line in file.readlines() if not line.startswith("//")]
#     linecount = len(lines) - 1
#     if num < 0: num = randint(0,linecount)
#     reply='\x02[{}/{}]\x02 {}'.format(num+1,linecount+1,lines[num]).decode('utf-8')


#     file.close()
#     lines =[]
#     return reply

@hook.command('wailord', "troll", autohelp=False)
def troll(text, action=None,notice=None):
    """troll -- Trolls on demand"""
    action(process_text(text,"trolls",notice))
    return

@hook.command("kek", "topkek", autohelp=False)
def topkek(text,reply=None,notice=None):
    """topkek -- keks on demand."""
    reply(process_text(text,"keks",notice))
    return

@hook.command(autohelp=False)
def loli(text,reply=None,notice=None):
    """loli -- Returns a loli."""
    reply("\x02\x034NSFW\x03\x02 {}".format(process_text(text,"lolis",notice)))
    return

@hook.command(autohelp=False)
def moistcake(text,reply=None,notice=None):
    "moistcake -- Moists on demand."
    reply(process_text(text,"moists",notice))
    return

@hook.command(autohelp=False)
def qt(text,reply=None,notice=None):
    """qt --  return qts."""
    reply(process_text(text,"qts",notice))
    return

@hook.command(autohelp=False)
def urmom(text,reply=None,notice=None):
    """urmom --  return urmom."""
    reply(process_text(text,"urmom",notice))
    return

@hook.command("old", "honry", autohelp=False)
def honry(text,reply=None,notice=None):
    """honry --  return honry."""
    reply(process_text(text,"old",notice))
    return

@hook.command(autohelp=False)
def bender(text,reply=None):
    """bender -- Bender quotes."""
    benders = ["Bite my shiny, metal ass!", "Bite my glorious, golden ass!", "Bite my shiny, colossal ass!", "Bite my splintery, wooden ass!", "Lick my frozen, metal ass!", "Like most of life's problems, this one can be solved with bending.", "Cheese it!", "Well, I'm boned.", "Hey, sexy mama...wanna kill all humans?", "Oh! Your! God!", "He's pending for a bending!", "This is the worst kind of discrimination - the kind against reply!", "In case of emergency, my ass can be used as a flotation device.", "In order to get busy at maximum efficiency, I need a girl with a big, 400-ton booty.", "I'm sick of shaking my booty for these fat jerks!", "Bite my red-hot glowing ass!", "All I know is, this gold says it was the best mission ever.", "Hey, guess what you're all accessories to.", "Well, I don't have anything else planned for today. Let's get drunk!", "Oh, no room for Bender, huh? Fine! I'll go build my own lunar lander! With blackjack and hookers! In fact, forget the lunar lander and the blackjack! Ah, screw the whole thing.", "I found it in the street! Like all the food I cook.", "I can't stand idly by while poor people get free food!", "Congratulations Fry, you've snagged the perfect girlfriend. Amy's rich, she's probably got other characteristics...", "You may need to metaphorically make a deal with the devil. By 'devil' I mean robot devil and by 'metaphorically' I mean get your coat.", "Boy, who knew a cooler could also make a handy wang coffin?", "Call reply old fashioned but I like a dump to be as memorable as it is devastating.", "My life, and by extension everyone else's is meaningless.", "Do I preach to you while you're lying stoned in the gutter? No.", "Everybody's a jerk. You, reply, this jerk.", "I hate the people that love reply and they hate reply.", "I've personalized each of your meals. Amy, you're cute, so I baked you a pony!", "Ahh, computer dating. It's like pimping, but you rarely have to use the phrase, 'upside your head'.", "Court’s kinda fun when it’s not my ass on the line!", "Maybe you can interface with my ass! By biting it!", "Well, I'll go build my own theme park! With blackjack and hookers! In fact, forget the park!", "  Compare your lives to mine and then kill yourself!", "I would give up my 8 other senses, even smision, for a sense of taste!", "Stupid anti-pimping laws!", "Blackmail’s such an ugly word. I prefer extortion. The x makes it sound cool.", "Great is ok, but amazing would be great!", "The pie is ready. You guys like swarms of things, right?", "Fry cracked corn, and I don't care; Leela cracked corn, I still don't care; Bender cracked corn, and he is great! Take that you stupid corn!", "Stay away from our women. You got metal fever, baby, metal fever!", "If it ain't black and white, peck, scratch and bite.", "Life is hilariously cruel.", "Pardon reply, brother. Care to donate to the anti-mugging you fund?", "I love this planet. I've got wealth, fame, and access to the depths of sleaze that those things bring.", "C'mon, it's just like making love. Y'know, left, down, rotate sixty-two degrees, engage rotors...", "Oh my God, I'm so excited I wish I could wet my pants.", "Argh. The laws of science be a harsh mistress.", "In the event of an emergency, my ass can be used as a floatation device.", "Hey, I got a busted ass here! I don't see anyone kissing it.", "I'm a fraud - a poor, lazy, sexy fraud.", "This'll show those filthy bastards who's loveable!"]
    reply(random.choice(benders))
    benders = []
    return

@hook.command('gains', "gainz", autohelp=False)
def gainz(text, reply=None,notice=None):
    """gains -- SICK GAINZ BRO"""
    reply(process_text(text,"gainz",notice))
    return

@hook.command(autohelp=False)
def nsfw(text, reply=None,notice=None):
    """nsfw -- Have a nice fap"""
    reply(process_text(text,"nsfw",notice))
    return




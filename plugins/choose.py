import re
import random

from cloudbot import hook

# @hook.regex(r'^uguubot(.*)')
@hook.command('decide')
def decide(text):
    "decide <choice1>, [choice2], [choice3], [choice4], ... -- " \
    "Randomly picks one of the given choices."

    try: text = text.group(1)
    except: text = text

    replacewords = {'should','could','?', ' i ',' you '}

    for word in replacewords:
        text = text.replace(word,'')

    if ':' in text: text = text.split(':')[1]
    
    c = text.split(', ')
    if len(c) == 1:
        c = text.split(' or ')
        if len(c) == 1:
            c = ['Yes','No']

    return random.choice(c).strip()

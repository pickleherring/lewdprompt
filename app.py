"""The lewdprompt app.
"""

import random

import streamlit


adjectives = [
    'buff',
    'busty',
    'frustrated',
    'horny',
    'hung',
    'ravenous',
    'repressed',
    'shy',
    'spoiled',
]

modifiers = [
    'big-butt',
    'college',
    'emo',
    'goth',
    'horsecock',
    'lactating',
    'lesbian',
    'multiboob',
    'pregnant',
    'shortstack',
    'virgin',
]

nouns = [
    'amazons',
    'bimbos',
    'catgirls',
    'centaurs',
    'cowgirls',
    'demons',
    'fairies',
    'femboys',
    'goblins',
    'heiresses',
    'librarians',
    'mermaids',
    'milves',
    'nuns',
    'orcs',
    'pixies',
    'vampires',
    'witches',
]

random.shuffle(adjectives)
random.shuffle(modifiers)
random.shuffle(nouns)


def get_phrase():

    adjective = adjectives.pop()
    modifier = modifiers.pop()
    noun = nouns.pop()

    return ' '.join([adjective, modifier, noun])


streamlit.title('generate frivolous prompts for hentai stories')

streamlit.markdown('''
This app is about S E C K S. By clicking the button below, you declare that you are an adult and consent to reading lewd words.
''')

if streamlit.button('I am an adult, give me a prompt!'):

    phrase1 = get_phrase()
    phrase2 = get_phrase()

    text = f'{phrase1} vs. {phrase2}!'

    streamlit.subheader(text.capitalize())

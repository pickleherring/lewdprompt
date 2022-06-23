"""The lewdprompt app.
"""

import random

import streamlit


adjectives = [
    'buff',
    'busty',
    'horny',
    'hung',
    'ravenous',
    'shy',
    'spoiled',
]

modifiers = [
    'big-butt',
    'college',
    'horsecock',
    'lactating',
    'lesbian',
    'multiboob',
    'pregnant',
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
    'heiresses',
    'librarians',
    'milves',
    'nuns',
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

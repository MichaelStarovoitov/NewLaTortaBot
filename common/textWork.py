import re
from deep_translator import GoogleTranslator
# from langdetect import detect
# pip install langdetect

def escape_markdown_v2(text):
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!', '"']
    for char in escape_chars:
        text = text.replace(char, f"\\{char}")
    return text

def get_simple_markdown(pattern, text):
    return re.sub(r'\*(.*?)\*', r'**\1**', re.sub(pattern, '', text))

def text_translator(text='', src='auto', dest='uk'):
    # source_lang = detect(text)
    translator = GoogleTranslator(source=src, target=dest)
    return translator.translate(text)
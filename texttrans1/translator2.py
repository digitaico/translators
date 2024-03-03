import googletrans
from googletrans import Translator  # detect and translate text
import speech_recognition as sr  # speech recognition

from gtts import gTTS  # Google text-to-speech
import os


translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])

# Detect incoming language

def detectLanguage(string):
    srcLang = translator.detect(string).lang
    return srcLang


def translateLanguage(string, destLang):
    return translator.translate(string, dest=destLang, src='auto').text
 

text = "Hi mom,  I'm leaving to Toront,  maybe arriving to Quebec at noon!"
text2= "この文章は日本語で書かれました。"
text3 = 'veritas lux mea'
trans = translateLanguage(text3, 'english')
detect = detectLanguage(text2)

print(trans)
print(detect)


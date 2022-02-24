import random, os
import speech_recognition as sr

from os import path
from pydub import AudioSegment

from gtts import gTTS
from google_trans_new import google_translator
from google_speech import Speech

# ПУСТЫШКА, НЕ ИСПОЛЬЗУЕТСЯ
# ТОЛЬКО ДЛЯ ТЕСТОВ
def audio(src, any_name):

    sound = AudioSegment.from_ogg(src)
    sound.export(src, format="wav")

    r = sr.Recognizer()

    harvard = sr.AudioFile(src)
    with harvard as source:
        audio = r.record(source)
        audio_text = r.recognize_google(audio)
        audio_name = 'audio/' + str(any_name) + '.txt'

        print(audio_text, file=open(audio_name, "a"))

        speech = open(audio_name).readlines()
        speech = ''.join(speech)
        # print(speech)

        translator = 'audio/' + str(any_name) + '.mp3'
        wav = 'audio/' + str(any_name) + '.wav'

        google  = google_translator()
        text = google.translate(speech,lang_src='en',lang_tgt='ja')
        # print(text)
        lang = "ja"
        speech = Speech(text, lang)
        speech.save(translator)

        sound = AudioSegment.from_mp3(translator)
        sound.export(src, format="wav")

    os.remove(audio_name)
    os.remove(translator)

# ПЕРЕВОД С РУССКОГО НА ЯПОНСКИЙ ГОЛОСОМ
def ru_ja(src, any_name):

    # ОБРАБОТКА ГОЛОСА ПОЛЬЗОВАТЕЛЯ В ФАЙЛЕ
    sound = AudioSegment.from_ogg(src)
    sound.export(src, format="wav")

    r = sr.Recognizer()

    harvard = sr.AudioFile(src)
    with harvard as source:
        # ЗАПИСЬ ЗАПРОСА ПОЛЬЗОВАТЕЛЯ В ТЕКСТОВЫЙ ФАЙЛ
        audio = r.record(source)
        audio_text = r.recognize_google(audio, language="ru-RU")
        audio_name = 'audio/' + str(any_name) + '.txt'

        print(audio_text, file=open(audio_name, "a"))

        speech = open(audio_name).readlines()
        speech = ''.join(speech)
        # print(speech)

        # ФОРМАТЫ ЗВУКОВОГО ФАЙЛА
        translator = 'audio/' + str(any_name) + '.mp3'
        wav = 'audio/' + str(any_name) + '.wav'

        # ПЕРЕВОД ЧЕРЕЗ ГУГЛ
        google  = google_translator()
        text = google.translate(speech,lang_src='rus',lang_tgt='ja')
        # print(text)
        lang = "en-CA"
        speech = Speech(text, lang)
        speech.save(translator)

        # ЭКСПОРТ В ФОРМАТЕ WAV
        sound = AudioSegment.from_mp3(translator)
        sound.export(src, format="wav")

    os.remove(audio_name)
    os.remove(translator)

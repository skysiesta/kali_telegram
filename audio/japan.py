from gtts import gTTS
from google_trans_new import google_translator
from google_speech import Speech

# ПЕРЕВОД НА ЯПОНСКИЙ - ТЕСТ
def translate():
    translator  = google_translator()

    speech = event.raw['object']['fwd_messages'][0]['text']
    speech = translator.translate(speech)
    tts = gTTS(speech)
    tts.save(str(audio) + '_hello.mp3')

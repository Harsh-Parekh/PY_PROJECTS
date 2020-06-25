"""
Download these 4 module
for code using pip
 1 gTTS
 2 speechrecognition
 3 playsound
 4 webbbrowser

command for installation
pip install module_name
"""

from gtts import gTTS
import speech_recognition as sr
import playsound
import webbrowser
import os

def ask_buy(que):
    file_que = 'question.mp3'
    tts = gTTS(que)
    tts.save(file_que)
    playsound.playsound(file_que)
    os.remove(file_que)
    pass

def trans_ans(recg,micro):

    if not isinstance(recg,sr.Recognizer):
        raise TypeError('recognizer is not of type...!')
    elif not isinstance(micro,sr.Microphone):
        raise TypeError('Microphone is not of type...!')

    print('please answer the quetion now')

    with micro as source:
        audio = recg.listen(source)
    try:
        txt = recg.recognize_google(audio)
        return txt
    except sr.RequestError:
        return 'Unreachable'
    except sr.UnknownValueError:
        return 'unable to listen...!'
    except:
        return 'Some other error...!'

def search_product(txt):
    webbrowser.open('https://www.flipkart.com/search?q='+txt)

if __name__=='__main__':
        hp = sr.Recognizer()
        micro =sr.Microphone()

        ask_buy('Hello i am hp what do u want to buy today?')
        txt = trans_ans(hp,micro)
        search_product(txt)




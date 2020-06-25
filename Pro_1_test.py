from gtts import gTTS
import speech_recognition as sr
import playsound
import webbrowser
import os

"""
First function which take one audio file which u call from main
it just simple file which later delete form system for space management
in line no :-18
these file is just use for playing in system nothing else
"""
def ask_buy(que):
    file_que = 'question.mp3'
    tts = gTTS(que)
    tts.save(file_que)
    playsound.playsound(file_que)
    os.remove(file_que)
    pass

"""
Second function which take 2 args
1 recognition or u can say that AI ;)
2 Microphone as receiver
here just your speech is simply converted to text
and return to variable
offcourse there are some exceptions for catching purpose
"""

def trans_ans(recg,micro):

    if not isinstance(recg,sr.Recognizer):
        raise TypeError('recognizer is not of type...!')
    elif not isinstance(micro,sr.Microphone):
        raise TypeError('Microphone is not of type...!')

    print('please kindly answer the question ')

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
    pass
   
if __name__=='__main__':
        hp = sr.Recognizer()
        micro =sr.Microphone()

        ask_buy('Hello i am hp what do u want to buy today?')
        txt = trans_ans(hp,micro)
        if txt=='unable to listen':
            print('unable to listen')
            exit()
        else:
            webbrowser.open('https://www.flipkart.com/search?q='+txt)



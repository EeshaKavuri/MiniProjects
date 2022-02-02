'''
import speech_recognition as speech
#We can store file name in a variable and use it
audio_file =('Hello_voice.wav')
#use the audio file as the source
read = speech.Recognizer()
with speech.AudioFile(audio_file) as source:
    audio = read.record(source)
    
#reads to audio file
try:
    print('Audio file contains:',r.recognize_google(audio))
except speech.UnknownValueError:
    print('Google speech recognition could not understand the audio file')
except speech.RequestError:
    print("Couldn't get the result from google speech recodnition")
except FileNotFoundError:
    print('File not found!')


'''
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('C:\\Users\\Rajendra Prasad\\AppData\\Local\\Programs\\Python\\Python39\\Hello_voice.wav') as source:
    audio = r.record(source)
    
try:
    print('Audio file contains:',r.recognize_google(audio))
except sr.UnknownValueError:
    print('Google speech recognition could not understand the audio file')
except sr.RequestError:
    print("Couldn't get the result from google speech recodnition")
except FileNotFoundError:
    print('File not found!')


from tkinter import *
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import ctypes
import pywhatkit
import googletrans
import playsound
import gtts

def print_gui(text_disp):
    lab1.config(text = text_disp)
    root.update()

def speak(audio):
    converted_audio = gtts.gTTS(audio)
    converted_audio.save('audio.mp3')
    playsound.playsound("audio.mp3")
    os.remove("audio.mp3")

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("How may I help you")

def takeCommand():
        translator = googletrans.Translator()
    # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print_gui("Listening...")
            r.pause_threshold=0.5
            audio = r.listen(source)

        try:
            print_gui("Recognizing...")
            query0001 = r.recognize_google(audio)
            detect = str(translator.detect(query0001).lang)
            print_gui(detect)
            query001 = r.recognize_google(audio,language=detect)
            print_gui(f"User said: {query001}\n")
            print_gui(query001)
        except Exception as e:
            print_gui(e)
            return "None"

        query = str(translator.translate(query001, dest='en').text)
        return query

browser_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('Chrome', None, webbrowser.Chrome(browser_path))
browser=webbrowser.get('Chrome')

def test():
    if __name__ == "__main__":
                query = takeCommand().lower()
                print_gui(query)
                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query)
                    speak("According to Wikipedia")
                    print_gui(results)
                    speak(results)

                elif 'youtube' in query:
                    speak("opening youtube")
                    query1 = query.replace("youtube ", "")
                    browser.open(f"https://www.youtube.com/results?search_query={query1}")

                elif 'news' in query:
                    speak("opening news")
                    browser.open("https://www.news.google.com/")

                elif 'where is' in query:
                    speak("opening maps")
                    query1 = query.replace("where is ", "")
                    browser.open(f"www.google.com/maps/place/{query1}")

                elif 'search' in query:
                    query1 = query.replace("search ", "")
                    speak("searching"+query1)
                    browser.open(query1)

                elif 'who are you' in query:
                    speak("i am your voice assistant")

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'music' in query:
                    music_dir = 'C:\\Users\\pjpan\\Music'
                    songs = os.listdir(music_dir)
                    print_gui(songs)

                    no = 0
                    os.startfile(os.path.join(music_dir, songs[no]))

                    while True:
                        aa = takeCommand().lower()
                        if 'next' in aa:
                            no += 1
                            os.startfile(os.path.join(music_dir, songs[no]))

                        elif'back' in aa:
                            no -= 1
                            os.startfile(os.path.join(music_dir,songs[no]))

                        elif 'stop' in aa:
                            break

                elif 'song' in query:
                    query1 = query.replace(" song", "")
                    speak("searching" + query1)
                    pywhatkit.mainfunctions.playonyt(query1)

                elif 'zoom' in query:
                    speak("opening zoom")
                    os.startfile('C:\\Users\\pjpan\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')

                elif 'lock window' in query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()

                elif 'goodbye' in query:
                    sys.exit(speak("good bye"))

                elif 'shutdown' in query:
                    speak('shutting down windows')
                    pywhatkit.shutdown()
                elif ' ' in query:
                    browser.open(f"https://www.google.com/search?q={query}")

root = Tk()
root.title("Home Assist")
root.geometry("200x200")
root.minsize(200,100)
lab1 = Label(text="click to start", width=100, bg="yellow")
lab1.pack()
btn1 = Button(text="play", command=test)
btn1.pack()
wishMe()
root.mainloop()
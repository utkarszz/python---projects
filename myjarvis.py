import speech_recognition as sr
import pyttsx3
import datetime
import os
import wikipedia
import pywhatkit
import pyaudio
import wolframalpha
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)  # Set volume to maximum (1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

    def greet():
        hour = datetime.datetime.now().hour
        if 0<= hour < 12:
            speak("Good morning!")
        elif 12<= hour < 18:
            speak("Good afternoon!")
        else:
            speak("Good evening!")
        speak("I am your voice assistant. How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-UK')
        print(f"user said;{command}")
    except exception as e:
        print("Sorry, I did not understand that.")
        return None
    return command.lower()
def greet():
    engine = pyttsx3.init()
    engine.say("Hello! I am your voice assistant.")
    engine.runAndWait()

def run_assistant():


    greet()
    speak("I am your voice assistant. How can I help you today?")
    speak("Please give me a moment to start up.")
    speak("I am ready to assist you.")
    speak("I am listening.") 
    speak("Please tell me what you want to do.")
    
       



    while True:
        command = take_command()

        if 'wikipedia' in command:
            topic = command.replace('wikipedia', '')
            result = wikipedia.summary(topic, sentences=2)
            speak("according to Wikipedia")
            speak(result)


        elif 'play' in command:
            song = command.replace('play', '')
            speak(f'playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")

        elif 'calculate' in command:
            client = wolframalpha.Client('536UXX-8J5HKT75T2')
            query = command.replace("calculate", "")
            res = client.query(query)
            answer = next(res.results).text
            speak(f"The answer is {answer}")


        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that. Please try again.")

run_assistant()      
print("you said", command)


        
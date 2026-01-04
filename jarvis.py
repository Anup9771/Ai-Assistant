import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyA-1YNnCeVbzqZXC9si-m_zaxJAZ3B9rf0")

# Initialize speech engine and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    try:
        reply = response.text.strip()
    except:
        reply = "Sorry, I could not process that."
    return reply

def processCommand(c):
    c = c.lower()
    print("Processing command:", c)

    if "google" in c:
        webbrowser.open("https://google.com")
    elif "facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "youtube" in c or "you tube" in c:
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in music_library.music:
            link = music_library.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't know the song {song}")
    else:
        response = aiProcess(c)
        if response:
            print("Jarvis:", response)
            speak(response)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print("You said:", word)

            if "jarvis" in word.lower():
                speak("Ya, I'm listening")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Didn't catch that.")
        except sr.RequestError:
            print("Speech service is down")
        except Exception as e:
            print("Error:", e)

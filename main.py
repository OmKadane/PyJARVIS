import pyttsx3 
import speech_recognition as sr
import pywhatkit as kit
import datetime
import os
import webbrowser
import pyjokes
import wikipedia
import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import requests 
from dotenv import load_dotenv

load_dotenv()  # LOAD THE .env FILE

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

# Set Chrome path correctly
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Listening flag
listening = False

# GUI setup
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x450")

response_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
response_box.pack(pady=20)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    root.after(0, lambda: response_box.insert(tk.END, "Assistant: " + text + "\n"))
    root.after(0, response_box.yview, tk.END)

def listen():
    global listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            if listening:
                speak("Sorry, I did not understand.")
            return None

    if not listening:
        return None

    try:
        command = recognizer.recognize_google(audio).lower()
        root.after(0, lambda: response_box.insert(tk.END, "You: " + command + "\n"))
        root.after(0, response_box.yview, tk.END)
        return command
    except sr.UnknownValueError:
        if listening:
            speak("You did not say anything. Please try again.")
        return None
    except sr.RequestError:
        if listening:
            speak("Sorry, there was a connection issue.")
        return None

def change_voice(type="soft"):
    voices = engine.getProperty('voices')
    if type == "deep":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

def save_memory(data):
    with open("memory.txt", "a") as file:
        file.write(data + "\n")

def recall_memory():
    if os.path.exists("memory.txt"):
        with open("memory.txt", "r") as file:
            return file.read()
    return "I don't have anything remembered."

def get_weather(city=""):
    api_key = os.getenv("OPENWEATHER_API_KEY") # Get key from environment
    if not api_key:
        return "Error: OpenWeather API key not found. Please set it in the .env file."
        
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] != "404":
            main_data = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main_data["temp"]
            humidity = main_data["humidity"]
            return f"The temperature in {city} is {temp}°C with {weather_desc} and humidity at {humidity}%."
        else:
            return "City not found."
    except Exception:
        return "Couldn't fetch weather information."

def main():
    global listening
    change_voice("soft")
    speak("Hello, I am your voice assistant. How can I help you?")
    speak("Listening...")

    while listening:
        command = listen()
        if not listening or command is None:
            continue

        time.sleep(0.5)

        if "open notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad.exe")

        elif "open calculator" in command:
            speak("Opening Calculator.")
            os.system("calc.exe")

        elif "open command prompt" in command or "open cmd" in command:
            speak("Opening Command Prompt.")
            os.system("start cmd")

        elif "what time is it" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "what is today's date" in command or "tell me the date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {current_date}")

        elif "search" in command:
            query = command.replace("search", "").strip()
            speak(f"Searching for {query}")
            kit.search(query)

        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            kit.playonyt(song)

        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.get("chrome").open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.get("chrome").open("https://www.youtube.com")

        elif "open facebook" in command:
            speak("Opening Facebook.")
            webbrowser.get("chrome").open("https://www.facebook.com")

        elif "open instagram" in command:
            speak("Opening Instagram.")
            webbrowser.get("chrome").open("https://www.instagram.com")

        elif "open twitter" in command or "open x" in command:
            speak("Opening Twitter.")
            webbrowser.get("chrome").open("https://www.twitter.com")

        elif "open whatsapp" in command:
            speak("Opening WhatsApp.")
            webbrowser.get("chrome").open("https://web.whatsapp.com")

        elif "open linkedin" in command:
            speak("Opening LinkedIn.")
            webbrowser.get("chrome").open("https://www.linkedin.com")

        elif "open github" in command:
            speak("Opening GitHub.")
            webbrowser.get("chrome").open("https://www.github.com")

        elif "What's your name" in command or "who are you" in command:
            speak("I am your voice assistant")

        elif "tell a joke" in command:
            speak(pyjokes.get_joke())

        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "").strip()
            speak(f"Searching {topic} on Wikipedia.")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything.")

        elif "shutdown" in command:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")

        elif "restart" in command:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")

        elif "exit" in command or "bye" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            break

        elif "remember this" in command:
            memory = command.replace("remember this", "").strip()
            if memory:
                save_memory(memory)
                speak("I have remembered that.")
            else:
                speak("Please tell me what to remember.")

        elif "what did you remember" in command or "do you remember anything" in command:
            memories = recall_memory()
            speak("Here is what I remembered.")
            speak(memories)

        elif "weather" in command:
            city = ""
            if "in" in command:
                city = command.split("in")[-1].strip()
            
            if not city:
                 speak("Please specify a city for the weather report, for example, 'weather in Mumbai'.")
            else:
                weather_report = get_weather(city) 
                speak(weather_report)

        else:
            speak("Sorry, I didn't understand that command.")

        speak("Listening...")

# GUI Buttons
def start_listening():
    global listening
    if not listening:
        listening = True
        threading.Thread(target=main).start()

def stop_listening():
    global listening
    listening = False
    speak("Voice assistant has stopped listening.")

listen_button = tk.Button(root, text="Start Listening", command=start_listening, width=20, height=2)
listen_button.pack()

stop_button = tk.Button(root, text="Stop Listening", command=stop_listening, width=20, height=2)
stop_button.pack(pady=10)

root.mainloop()

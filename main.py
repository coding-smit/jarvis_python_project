import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env file load karega
api_key = os.getenv("OPENAI_API_KEY")  # yahan se key le raha hai
# client = OpenAI(api_key=api_key)

r = sr.Recognizer()
# Set a pause threshold (seconds of non-speaking audio before a phrase is considered complete)
r.pause_threshold = 0.8
if __name__ =="__main__":
     engine = pyttsx3.init()

     def speak(text):
     # """Function to speak the given text."""
          engine.say(text)
          engine.runAndWait()
     
     def processCommand(command):
          print(f"User said: {command}")
                         
                         #this is commaands of jarvise
          if "open google" in command:
               speak("Opening Google.")
               webbrowser.open("https://www.google.com")
                         
          elif "open youtube" in command:
               speak("Opening YouTube.")
               webbrowser.open("https://www.youtube.com")

          elif "what time" in command:
               now = datetime.datetime.now().strftime("%I:%M %p") # e.g., "05:30 PM"
               speak(f"The current time is {now}")

          elif "stop" in command or "exit" in command or "quit" in command:
               speak("Goodbye.")
               sys.exit()
          else:

               client = OpenAI(
               api_key=api_key,
               base_url="https://openrouter.ai/api/v1",
               )

               completion = client.chat.completions.create(
               extra_headers={
               "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
               "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
               },
               model="openai/gpt-4o",
               messages=[
               {
                    "role":"system", "content": "You are Jarvis, my AI assistant. Be polite, concise, and always answer like a friendly butler in English .",
                    "content": command
               }
               ]
               )

               speak(completion.choices[0].message.content)
               print(completion.choices[0].message.content)

          
     while True: 
          # speak("hello sir ,can  i help you")

          with sr.Microphone() as source:
               print("\nListening...")
               # Adjust for ambient noise (optional, but good)
               # r.adjust_for_ambient_noise(source, duration=1) 
               try:
                    # Listen for audio. Increased limits for usability.
                    audio = r.listen(source, timeout=5.0, phrase_time_limit=5.0)
                    print("Recognizing...")
                    
                    # Use Google Speech Recognition
                    word = r.recognize_google(audio).lower()
                    print(f"User said: {word}")
                    
                    if(word.lower()== "jarvis"):
                         speak("yes sir")
                         
                         with sr.Microphone() as source:
                              print("jarvis Active...")
                              audio = r.listen(source)
                              command = r.recognize_google(audio).lower()
                              processCommand(command)
                             
                    # Use Google Speech Recognition

               except sr.WaitTimeoutError:
                    print("Listening timed out. Please try again.")
               except sr.UnknownValueError:
                    print("I didn't catch that. Please try again.")
               except sr.RequestError as e:
                    print(f"Could not request results from Google; {e}")
               except Exception as e:
                    print(f"An unknown error occurred: {e}")

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import pywhatkit as wk
import random
import os
import cv2
import requests
import operator
import time
import json
import logging

log_directory = "C:/Users/Taran Shetty/Desktop/A.L.I.T.A"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(filename=f"{log_directory}/alita_activity.log", level=logging.DEBUG)
logging.info("Testing log creation.")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
MEMORY_FILE = "alita_memory.json"
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        alita_memory = json.load(file)
else:
    alita_memory = {}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("What can I do for you today?")

def save_to_memory(task, status):
    alita_memory[task] = status
    with open(MEMORY_FILE, "w") as file:
        json.dump(alita_memory, file)

def check_memory(task):
    return alita_memory.get(task, "unknown")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1.5 if check_memory("speech_recognition") == "success" else 2
        r.non_speaking_duration = 0.5 if check_memory("speech_recognition") == "success" else 1 
        r.adjust_for_ambient_noise(source, duration=1)
        r.phrase_threshold = 0.3
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Recognized: {query}")  
        save_to_memory("speech_recognition", "success")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        save_to_memory("speech_recognition", "error")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower().strip()
        logging.info(f"Query received: {query}")  
        
        if "how are you" in query or "how r u" in query:
            print("I am fine, thank you.")
            speak("I am fine, thank you.")

        elif "hey alita" in query or "hi alita" in query:
            print("Hello!")
            speak("Hello!")

        elif 'exit' in query or 'quit' in query:
            print("Exiting the program.")
            speak("Exiting the program.")
            break
        
        elif 'who are you' in query or "hu r u" in query:
            print("My name is Alita, your intelligent assistant. Is there anything you'd like help with today?")
            speak("My name is Alita, your intelligent assistant. Is there anything you'd like help with today?")
        
        elif "who created you" in query:
            print("I was created by Taran Shetty")
            speak("I was created by Taran Shetty")

        elif any(phrase in query for phrase in ["meaning of your name", "what's the meaning of your name", "tell me the meaning of", "tell me the meaning of your name"]):
            print("Alita is an acronym for Artificial Language Intelligent Tasking Assistant.")
            speak("Alita is an acronym for Artificial Language Intelligent Tasking Assistant.")

        elif "thanks" in query or "thank you" in query:
            print("Thank you for your kind words. Feel free to ask if you need further assistance.")
            speak("Thank you for your kind words. Feel free to ask if you need further assistance.")
        
        elif "what is " in query:
            try:
                speak("Searching...")
                query = query.replace("what is", "").strip()
                results = wikipedia.summary(query, sentences=3)
                speak("According to the web")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                print("Sorry, I couldn't find any matching page.")
                speak("Sorry, I couldn't find any matching page.")
            except wikipedia.exceptions.DisambiguationError as e:
                print("The query was too ambiguous. Here are some suggestions: " + str(e.options))
                speak("The query was too ambiguous. Please be more specific.")
            except Exception as e:
                print("An error occurred:", e)
                speak("Sorry, I encountered an error while searching.")
        
        elif "who is " in query:
            try:
                speak("Searching...")
                query = query.replace("who is", "").strip()
                results = wikipedia.summary(query, sentences=3)
                speak("According to the web")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                print("Sorry, I couldn't find any matching page.")
                speak("Sorry, I couldn't find any matching page.")
            except wikipedia.exceptions.DisambiguationError as e:
                print("The query was too ambiguous. Here are some suggestions: " + str(e.options))
                speak("The query was too ambiguous. Please be more specific.")
            except Exception as e:
                print("An error occurred:", e)
                speak("Sorry, I encountered an error while searching.")

        elif "open the weather app" in query.lower().strip():
             pyautogui.press('win')
             time.sleep(1)
             pyautogui.typewrite('weather')
             pyautogui.press('enter')

        elif 'just open google' in query:
            webbrowser.open('google.com')
        
        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")

        elif 'just open youtube' in query.lower().strip(): 
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('youtube')
            pyautogui.press('enter')

        
        elif 'open youtube' in query:
             speak("What will you like to watch?")
             query = takeCommand().lower()
             wk.playonyt(f"{query}")
        
        elif "search" in query:
            query = query.replace("search", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif"find my youtube channel" in query:
            img = pyautogui.locateCenterOnScreen("image recognition/Screenshot1.png",confidence =0.8)
            pyautogui.doubleClick(img)
            time.sleep(1)
            pyautogui.hotkey('alt','space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)
            pyautogui.typewrite('youtube')
            pyautogui.press('enter')
            time.sleep(2)
            img1 =pyautogui.locateCenterOnScreen("image recognition/Screenshot2.png",confidence =0.9)
            pyautogui.doubleClick(img1)
            time.sleep(3)
            img2 =pyautogui.locateCenterOnScreen("image recognition/Screenshot3.png",confidence = 0.5)
            pyautogui.click(img2)
            time.sleep(1)
            pyautogui.typewrite("taran shetty",0.1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')
            img3 =pyautogui.locateCenterOnScreen("image recognition/Screenshot4.png",confidence = 0.8)
            pyautogui.click(img3)

        elif 'close browser' in query:
            os.system("C:\\Windows\\System32\\taskkill.exe /f /im msedge.exe")
            speak("Closing browser...")

        elif 'close chrome' in query:
            os.system("C:\\Windows\\System32\\taskkill.exe /f /im chrome.exe")
            speak("Closing chrome...")

        elif 'type' in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}", 0.1)

        elif "open paint" in query:
            npath = r"C:\Users\Taran Shetty\AppData\Local\Microsoft\WindowsApps\mspaint.exe"
            os.startfile(npath)
        
        elif'draw a line' in query:
            pyautogui.moveTo(x=400, y=300, duration = 1)
            pyautogui.leftClick
            pyautogui.dragRel(400,0,1)

        elif'draw a square' in query:
            pyautogui.moveTo(x=1000, y=300, duration =1)
            pyautogui.leftClick()
            distance = 400
            pyautogui.dragRel(distance, 0, duration = 1)
            pyautogui.dragRel( 0,distance, duration = 1)
            pyautogui.dragRel(-distance, 0, duration = 1)
            pyautogui.dragRel(0,-distance, duration = 1)

        elif "draw a rectangular spiral" in query:
            pyautogui.moveTo(x =400, y= 300,duration =1)
            pyautogui.leftClick()
            distance = 300
            while distance> 0:
             pyautogui.dragRel(distance, 0, 0.1 , button='left')
             distance = distance - 10
             pyautogui.dragRel( 0,distance,0.1, button ='left')
             pyautogui.dragRel(-distance, 0,0.1,button ='left')
             distance = distance -10
             pyautogui.dragRel(0,-distance,0.1,button ='left')
   
        elif 'undo' in query:
            pyautogui.hotkey("ctrl","z")

        elif "close paint" in query:
            os.system("C:\\Windows\\System32\\taskkill.exe /f /im mspaint.exe")

        elif "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("C:\\Windows\\System32\\taskkill.exe /f /im notepad.exe")

        elif "open command prompt" in query:
            npath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(npath)

        elif "close command prompt" in query:
            os.system("C:\\Windows\\System32\\taskkill.exe /f /im cmd.exe")

        elif 'open whatsapp' in query:
            pyautogui.press("win")
            time.sleep(1)
            pyautogui.typewrite('whatsapp')
            pyautogui.press('enter')

        elif'press enter' in query:
            pyautogui.press('enter')

        elif 'maximise' in query or 'maximize'in query :
             pyautogui.hotkey('win','up')

        elif 'minimize' in query or 'minimise' in query:
             pyautogui.hotkey('win','down')
        
        elif 'play music' in query or 'maximize' in query:
            music_dir = r"C:\Users\Taran Shetty\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'shutdown' in query:
            speak("Shutting down the system in 5 seconds...")
            os.system("C:\\Windows\\System32\\shutdown.exe /s /t 5")
        
        elif 'restart' in query:
            speak("Restarting the system in 5 seconds...")
            os.system("C:\\Windows\\System32\\shutdown.exe /r /t 5")

        elif "lock screen" in query:
            os.system("C:\\Windows\\System32\\rundll32.exe user32.dll,LockWorkStation")
        
        elif 'open camera' in query :
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "take screenshot" in query:
         speak("tell me a name for the file")
         name = takeCommand().lower().strip()
         time.sleep(3)
         img = pyautogui.screenshot()
         img.save(f"C:\\Users\\Taran Shetty\\OneDrive\\Desktop\\A.L.I.T.A\\{name}.png")
         speak("screenshot saved")
               
        elif 'calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("listening")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    '/': operator.__truediv__,

                }.get(op)
            def eval_binary_expr(op1, oper, op2):
             try:
                 op1, op2 = float(op1), float(op2)
                 return get_operator_fn(oper)(op1, op2)
             except ValueError as e:
                 return f"Error in operands: {e}"
             except Exception as e:
                 return f"Error in operation: {e}"
            components = my_string.split()

            if len(components)==3:
                op1,oper,op2 = components

                result = eval_binary_expr(op1,oper,op2)
                print(f"your result is {str(result)}")
                speak(f"your result is{str(result)}")

            else:
                speak("Sorry,I could not understand the expression.")

        elif "ip address" in query.lower().strip():  
            speak("Checking for your IP address...")
            try:
              ip = requests.get("https://api.ipify.org").text
              print(f"Your IP address is: {ip}")  
              speak(f"Your IP address is {ip}")
            except Exception as e:
               print(f"Error: {e}") 
               speak("Sorry, I couldn't fetch your IP address. Please try again later.")

        elif'open calculator' in query:
             pyautogui.press('win')
             time.sleep(1)
             pyautogui.typewrite('calculator')
             pyautogui.press("enter")

        elif'close app' in query:
             pyautogui.hotkey("alt","f4")

        elif 'volume up' in query:
            for _ in range(6):
              pyautogui.press("volumeup")

        elif "volume down" in query:
            for _ in range(6):
              pyautogui.press("volumedown")

        elif 'mute' in query or "unmute" in query:
              pyautogui.press("volumemute")

        elif 'how is the weather today' in query:
         wapi = "2a7f67f0407141c33dce869320ca494c"  
         location = 'mumbai' 
         url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={wapi}&units=metric"
         try:
             response = requests.get(url)
             data = response.json()  
             wd = data['weather'][0]['description']
             temperature = data['main']['temp']
             print(f"The weather in {location} is currently {wd} with a temperature of {temperature} degrees Celsius.")
             speak(f"The weather in {location} is currently {wd} with a temperature of {temperature} degrees Celsius.")
    
         except Exception as e:
             print("Sorry, unable to fetch data.")
             speak("Sorry, I couldn't fetch the weather data.")

        else:
            print("I am unable to understand kindly repeat")
            speak("I am unable to understand kindly repeat")



        

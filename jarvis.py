import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import random

print(" INITIALIZING JARVIS ")
CREATOR= "JOHN"                                      # YOUR NAME CAN BE ENTERED HERE


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish () :
    hour = datetime.datetime.now().hour
    
    if hour>=0 and hour<=12 :
        speak("GOOD MORNING" + CREATOR)
    
    elif hour>= 12 and hour< 18 :
        speak("GOOD AFTERNOON " + CREATOR)
        
    else :
        speak("GOOD EVENING " + CREATOR)
    
    speak("HI I AM JARVIS , HOW MAY I HELP YOU")    
    
        
# STARTING OF MAIN PROGRAM
said= ""

def inputcommand():
    r= sr.Recognizer()
    with sr.Microphone() as source :
        print("LISTENING....")
        audio = r.listen(source)
        
    try :
        print("recognizing ....")
        said = r.recognize_google(audio, language = "en-in")
        print(f"you said .. : {said}\n",)


    except Exception as e :
        print("CAN YOU PLEASE SAY THAT AGAIN ...")

    return said    
           
wish() 
said = inputcommand()   

#logic to access web

if "open youtube" in said.lower() :
    url = "youtube.com"

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif "open google" in said.lower() :
    url = "google.com"

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'       # FOR OPENING IN GOOGLE CHROME
    webbrowser.get(chrome_path).open(url)

elif "play music" in said.lower() :
    songs_dir = "C:\\Users\\avime\\Desktop\\SONGS"
    songs = os.listdir(songs_dir)  
    print(songs)                                                      # INSERT YOUR OWN PATH DIRECTORY
    os.startfile(os.path.join(songs_dir,songs[0]))

elif "the time"  in said.lower() :  
    strtime= datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{CREATOR} the time is {strtime}")

elif  "timer" in said.lower() or "set a timer" in said.lower():
    speak("Starting a timer of 10 seconds ")
    for i in range(10,0,-1) :
        speak(str(i))

    speak("YOUR TIME IS UP")

elif "open coursera" in said.lower() :
    url = "https://www.coursera.org/"

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)    
    
elif " open movie"  in said.lower() :
    movie_dir ="D:\\MOVIES"                 # enter your own directory path
    movie = os.listdir(movie_dir)
    print(movie)
    os.startfile(os.path.join(movie_dir,movie[0]))

elif "a joke" in said.lower():
    jokes=[" I can't believe I got fired from the calendar factory. All I did was take a day off ", "How did I escape Iraq? Iran.", "I'm reading a book about anti-gravity. It's impossible to put down.","Atheism is a non-prophet organization"," I wasn't originally going to get a brain transplant, but then I changed my mind.","The future, the present and the past walked into a bar. Things got a little tense. "]  
    speak("Allrite, hear this ")
    jke= random.sample(jokes,1)
    print(jke)
    speak(jke)

elif " can you perform calculations" in said.lower()  or "calculations" in said.lower() :
    speak("sure")
    speak(" what would you like me to do")
    per = inputcommand()
    if "add" in per.lower() or "perform addition" in per.lower() :
        speak("ok , what are the numbers ")
        op= inputcommand()
        res = [int(i) for i in op.split() if i.isdigit()]
        print(sum(res))
        ans= sum(res)
        speak(ans)

    elif "subtract" in per.lower() or "perform subtraction" in per.lower() :
        speak("ok , what are the numbers ")
        op= inputcommand()
        res = [int(i) for i in op.split() if i.isdigit()]
        print(res[0]-res[1])
        ans= res[0]-res[1]
        speak(ans)

    elif "multiply " in per.lower()  or " perform multiplication "  in per.lower() :
        speak("ok , what are the numbers ")
        op = inputcommand()
        res= [ int(i)  for i in op.split() if i]
        print(res[0] * res[1])
        ans = res[0]* res[1]
        speak(ans)

    elif "divide" in per.lower()  or " perform division" in per.lower() :
        speak("ok , what are the numbers ")
        op = inputcommand()
        res= [ int(i)  for i in op.split() if i]
        print(res[0] / res[1])
        ans = res[0] / res[1]
        speak(ans)

    elif " power " in per.lower() or " perform power " :
        speak("ok , what are the numbers ")
        op = inputcommand()
        res= [ int(i)  for i in op.split() if i]
        print(res[0] ** res[1])
        ans = res[0] ** res[1]
        speak(ans)


else :
    speak("sorry the command is not yet installed , or not found ")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-spanish")
            command = command.lower()
            if "selena" in command:
                command = command.replace("selena", "")
                print(command)
    except:
        pass
    return command


def run_selena():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("reproduciendo" + song)
        pywhatkit.playonyt(song)
    elif "dime la hora" in command:
        time = datetime.datetime.now().strftime("%I:%M:%p")
        talk("la hora es " + time)

    elif "busca en wikipedia" in command:
        fact = command.replace("busca en wikipedia", "")  # fact = dato
        # el 1 limita los resultados que se muestran
        info = wikipedia.summary(fact, 1)
        print("info")
        talk(info)
    elif "dime una broma" in command:
        talk(pyjokes.get_joke("es"))

    elif "qué opinas de meredy" in command:
        talk("Meredy no me cae bien, pero es buena persona")
    else:
        talk("aun no se como contestar a eso")


while True:
    run_selena()

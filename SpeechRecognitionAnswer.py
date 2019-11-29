import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr

#Initialisation
engine = pyttsx3.init()
r = sr.Recognizer()
#Obtention des valeurs actuel de la voie synthétisée
engine.getProperty('voices')
#Définition des propriétés de la voix
engine.setProperty('voice', 'fr-be')
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
#Obtention et ajustement de la vitesse de la voix   --->   (defaut = 200 mots/minutes)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 100)
#Presets des questions
#Création d'une liste de questions/réponse
greetings = ['bonjour','salut','hey!']
jokes = ['blague1','blague2','blague3']
question = ['comment ca va?','comment tu vas?','ca va bilbo?']
responses = ['je vais bien','ok']
rep9 = ['De rien', 'ravi de pouvoir vous aider']
var1 = ['qui t\'as créé?', 'qui t\'as fabriqué', 'qui est ton créateur']
var2 = ['J\'ai été créé par LB depuis cette ordinateur', 'LB', 'Je ne sais pas']
var3 = ['quel heure est-il?', 'donne moi l\'heure']
var4 = ['qui est-tu?', 'quel est ton nom?']
cmd1 = ['ouvre le navigateur','ouvre google']
cmd2 = ['joue de la musique', 'je veux écouter de la musique', 'ouvre moi le lecteur de musique']
cmd3 = ['raconte moi une blague','fais moi rire']
cmd4 = ['ouvre youtube']
cmd5 = ['quel est la météo?', 'quel temps fait-il']
cmd6 = ['au revoir', 'éteins toi', 'arret']
cmd9 = ['merci']

#Affichage de la date actuelle
now = datetime.datetime.now()
print(now, ' -----> La première partie fonctionne')

with sr.Microphone() as source:
    engine.say('Bonjour, dites quelque chose')
    engine.runAndWait()
    print('Veuillez vous exprimer')
    #Reduction du bruit ambiant
    r.adjust_for_ambient_noise(source)
    #Récupération de l'audio
    #audio = r.listen(source)
    r.energy_threshold = 50
    audio = r.listen(source, timeout=1,phrase_time_limit=5)
    try:
        print('Vous avez dit: -' + r.recognize_google(audio, language = 'fr-be'))
        engine.say('Vous avez dit:-' + r.recognize_google(audio, language = 'fr-be'))
        engine.runAndWait()
    except sr.UnknownValueError:
        print('Je ne vous ai pas compris')
        engine.say('Je ne vous ai pas compris')
        engine.runAndWait()
if r.recognize_google(audio) in greetings:
    random_greeting = random.choice(greetings)
    print(random_greeting)
    engine.say(random_greeting)
    engine.runAndWait()
elif r.recognize_google(audio) in question:
    engine.say('Je vais bien')
    engine.runAndWait()
    print('Je vais bien')
elif r.recognize_google(audio) in var1:
    engine.say('J\'ai été programmé par LB')
    engine.runAndWait()
    reply = random.choice(var2)
    print(reply)
elif r.recognize_google(audio) in cmd9:
    print(random.choice(rep9))
    engine.say(random.choice(rep9))
    engine.runAndWait()
elif r.recognize_google(audio) in cmd2:
    mixer.init()
    mixer.music.load("The_Storm.mp3")
    mixer.music.play()
elif r.recognize_google(audio) in var4:
    engine.say('Je suis un robot')
    engine.runAndWait()
elif r.recognize_google(audio) in cmd4:
    webbrowser.open('https://www.youtube.com/watch?v=G_sBOsh-vyI')
elif r.recognize_google(audio) in cmd6:
    print('A plus tard')
    engine.say('A plus tard')
    engine.runAndWait()
    exit()
elif r.recognize_google(audio) in cmd5:
    owm = pyowm.OWM('f6101ed0537f69647b3a23503d71c4a1')
    observation = owm.weather_at_place('Amiens, FR')
    observation_list = owm.weather_around_coords(49.9, 2.3)
    w = observation.get_weather()
    w.get_wind()
    w.get_humidity()
    w.get_temperature('celsius')
    print(w)
    print(w.get_wind())
    print(w.get_humidity())
    print(w.get_temperature('celsius'))
    engine.say(w.get_wind())
    engine.runAndWait()
    engine.say('Humidité')
    engine.runAndWait()
    engine.say(w.get_humidity())
    engine.runAndWait()
    engine.say('Temperature')
    engine.runAndWait()
    engine.say(w.get_temperature('celsius'))
    engine.runAndWait()
elif r.recognize_google(audio) in var3:
    print("Current date and time : ")
    print(now.strftime("Il est %H:%M"))
    engine.say(now.strftime("Il est %H:%M"))
    engine.runAndWait()
elif r.recognize_google(audio) in cmd1:
    webbrowser.open('www.google.com')
elif r.recognize_google(audio) in cmd3:
    jokrep = random.choice(jokes)
    engine.say(jokrep)
    engine.runAndWait()
else:
    engine.say("Veuillez patienter")
    engine.runAndWait()
    print(wikipedia.summary(r.recognize_google(audio)))
    engine.say(wikipedia.summary(r.recognize_google(audio)))
    engine.runAndWait()
    userInput3 = input("or else search in google")
    webbrowser.open_new('www.google.com/search?q=' + userInput3)
print('Fin tu test')

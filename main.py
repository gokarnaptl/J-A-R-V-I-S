from cmath import exp
from fileinput import filename
from os import link
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import pyttsx3
import pywhatkit
from torch import true_divide
import wikipedia
from time import sleep
import webbrowser as web
import webbrowser
import pyautogui
from pyautogui import click


recognizer = speech_recognition.Recognizer()

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
todo_list = ['Go to sleep', 'play chess']

##################################################################################

def create_note():
	global recognizer
	engine.say("what you want to write onto your note ?")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				note = recognizer.recognize_google(audio)
				note = note.lower()

				engine.say("Choose a filename")
				engine.runAndWait()

				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)

				filename = recognizer.recognize_google(audio)
				filename = filename.lower()

			with open(filename, 'w') as f:
				f.write(note)
				done = True
				engine.say(f" successfully updated the note {filename}")
				engine.runAndWait()
		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			engine.say("I did not understand you! Please try again!")
			engine.runAndWait()

#####################################################################

def add_todo():
	global recognizer
	engine.say("what you want to add?")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				item = recognizer.recognize_google(audio)
				item = item.lower()

				todo_list.append(item)
				done = True

				engine.say("I added {item} to the to do list!")
				engine.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			engine.say("I did not understand you! Please try again!")
			engine.runAndWait()
##############################################################################

def show_todo():
	global recognizer
	engine.say("The items in your to do list are the following")
	for item in todo_list:
		engine.say(item)
	engine.runAndWait()

########################################################################

def greeting():
	global recognizer
	engine.say("Hello my lord what can i do for you")
	engine.runAndWait()

#########################################################################

def youtube():
	global recognizer
	engine.say("what you want to play on youtube?")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				title = recognizer.recognize_google(audio)
				title = title.lower()

				engine.say("Okay, playing{audio}")

				pywhatkit.playonyt(title)

				done = True

				engine.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			engine.say("I did not understand you! Please try again!")
			engine.runAndWait()

##############################################################################

######################################################

def google_meet():
	global recognizer
	engine.say("which class you want to join?")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				query = recognizer.recognize_google(audio)
				query = query.lower()

				engine.say("Okay")

				if 'science' in query:

					from OnlineClass.Links import Science

					Link=Science()

					webbrowser.open(Link)

					sleep(10)

					click(x=1315, y=581)

					sleep(1)

				engine.say("You are in the class now")

				done = True

				engine.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			engine.say("I did not understand you! Please try again!")
			engine.runAndWait()

def chat_box():
	global recognizer
	engine.say("what message should i convey in the meet")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				query = recognizer.recognize_google(audio)
				query = query.lower()

				engine.say("Okay")


				click(x=1686, y=971)

				sleep(1)

				pyautogui.write(query)

				pyautogui.press('enter')

				sleep(6)

				engine.say("Your message has been sent")

				click(x=1803, y=196)

				done = True

				engine.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			engine.say("I did not understand you! Please try again!")
			engine.runAndWait()
			##########################################

def leave_meet():
	global recognizer
	engine.say("Okay")
	click(x=1116, y=981)

	############################################3

##############################################################################
def web():
	global recognizer
	engine.say("what you want to search on the web?")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				query = recognizer.recognize_google(audio)
				query = query.lower()

				engine.say("Okay")

				result = pywhatkit.search(query)

				engine.say("This is what I got on web")

				done = True

				engine.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			engine.say("I did not understand you! Please try again!")
			engine.runAndWait()

######################################################




def see_you():
	global recognizer
	engine.say("See you soon my lord")
	sys.exit(0)
	
############################################################################

mappings = {
	"greeting": greeting,
	"create_note": create_note,
	"add_todo": add_todo,
	"show_todo": show_todo,
	"youtube": youtube,
	"web": web,
	"see_you": see_you,
	"google_meet": google_meet,
	"chat_box": chat_box,
	"leave_meet": leave_meet
	
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model() 

while True:

	try:
		with speech_recognition.Microphone() as mic:
			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			audio= recognizer.listen(mic)

			message = recognizer.recognize_google(audio)
			message = message.lower()

		assistant.request(message)
	except speech_recognition.UnknownValueError:
		recognizer = speech_recognition.Recognizer()
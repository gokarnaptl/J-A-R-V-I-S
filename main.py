from cmath import exp
# from email import message
from fileinput import filename
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import pyttsx3
import pywhatkit
from torch import true_divide
import wikipedia
# email imports
from email.message import EmailMessage
import smtplib
# import email.utils


recognizer = speech_recognition.Recognizer()

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
todo_list = ['Go to sleep', 'play chess']


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


def show_todo():
	global recognizer
	engine.say("The items in your to do list are the following")
	for item in todo_list:
		engine.say(item)
	engine.runAndWait()


def greeting():
	global recognizer
	engine.say("Hello. What can I do for you ?")
	engine.runAndWait()


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


def email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('jarvisstark884@gmail.com', 'jarvisgoku')
    email = EmailMessage()
    email['From'] = 'jarvisstark884@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'purva': 'purva.tekade15@gmail.com',
    'shubhada': 'shubhadatambe2610@gmail.com',
    'goku': 'gokarnapatil3@gmail.com'
}

def send_email():
	global recognizer
	engine.say("To Whom you want to send email?")
	engine.runAndWait()
	done = False

	while not done:
		try:

			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				name = recognizer.recognize_google(audio)
				name = name.lower()
				receiver = email_list[name]
				done = True

				engine.runAndWait()

		except speech_recognition.UnknownValueError:
				recognizer = speech_recognition.Recognizer()
				engine.say("I did not understand you! Please try again!")
				engine.runAndWait()

		try:
			engine.say("What is the subject of your email?")
			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)
				subject = recognizer.recognize_google(audio)
				subject = subject.lower()
				done = True
				engine.runAndWait()
		except speech_recognition.UnknownValueError:
				recognizer = speech_recognition.Recognizer()
				engine.say("I did not understand you! Please try again!")
				engine.runAndWait()
		try:
			engine.say("what text should i send in email?")
			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				
				audio = recognizer.listen(mic)
				message = recognizer.recognize_google(audio)
				message = message.lower()

				engine.say("okay sir !")

				email(receiver, subject, message)

				engine.say("Hello lazy kid, your email is sent !")

				done = True

				engine.runAndWait()

		except speech_recognition.UnknownValueError:
				recognizer = speech_recognition.Recognizer()
				engine.say("I did not understand you! Please try again!")
				engine.runAndWait()

				engine.say("Hey lazy boy, your email is sent")
				engine.runAndWait()


def quit():
	global recognizer
	engine.say("Bye")
	engine.runAndWait()
	sys.exit(0)

mappings = {
	"greeting": greeting,
	"create_note": create_note,
	"add_todo": add_todo,
	"show_todo": show_todo,
	"youtube": youtube,
	"send_email": send_email,
	"web": web,
	"exit": quit
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
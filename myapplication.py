import pyttsx3
import os
import webbrowser
import socket
from pygame import mixer
import smtplib, ssl


pyttsx3.speak("hello user lets chat")
while True:
	print("Hey lets chat" , end='')
	inp=input()
	# run chrome
	if(("run" in inp) or ("open" in inp)) and ("chrome" in inp):
		pyttsx3.speak("yes I run chrome")
		os.system("chrome")
		# run notepad
	elif(("run" in inp) or("execute" in inp)) and (("notepad" in inp) or("editor" in inp)):
		pyttsx3.speak("yes I open notepad for you")
		os.system("notepad")
		# run wmplayer
	elif("run" in inp) and("player" in inp) and ("media" in inp):
		pyttsx3.speak("ok I run media player for you")
		os.system("wmplayer")
		# run paint
	elif(("run" in inp) or("open" in inp)) and("paint" in inp):
		pyttsx3.speak("yes I open paint for you")
		os.system("mspaint")
		# run word
	elif(("run" in inp) or("open" in inp)) and("word" in inp):
		pyttsx3.speak("yes I run word for you")
		os.system("winword")
		# run excel
	elif(("run" in inp) or("open" in inp)) and("excel" in inp):
		pyttsx3.speak("yes I run excel for you")
		os.system("excel")
		# run power point
	elif(("run" in inp) or("open" in inp)) and("power point" in inp):
		pyttsx3.speak("yes I run power point for you")
		os.system("powerpnt")
		# run onenote
	elif(("run" in inp) or("open" in inp)) and("onenote" in inp):
		pyttsx3.speak("yes I run one note for you")
		os.system("onenote")
		# run outlook
	elif(("run" in inp) or("open" in inp)) and("outlook" in inp):
		pyttsx3.speak("yes I run outlook for you")
		os.system("outlook")
		# run current date
	elif(("run" in inp) or("show" in inp) or ("display" in inp)) and("date" in inp):
		pyttsx3.speak("ok here is the current date")
		os.system("date")
		# run current time
	elif(("run" in inp) or("show" in inp) or ("display" in inp)) and("time" in inp):
		pyttsx3.speak("ok here is the current time")
		os.system("time")
		# open amazon website
	elif(("run" in inp) or("open" in inp) or ("go" in inp)) and("amazon" in inp):
		pyttsx3.speak("yes I run amazon website for you")
		webbrowser.open("amazon.in")
		# open yahoo website
	elif(("run" in inp) or("open" in inp) or ("go" in inp)) and("yahoo" in inp):
		pyttsx3.speak("yes I run yahoo website for you")
		webbrowser.open("yahoo.com")
		# open youtube
	elif(("run" in inp) or("open" in inp) or ("go" in inp)) and("youtube" in inp):
		pyttsx3.speak("yes I run youtube for you")
		webbrowser.open("youtube.com")
		# open calculator
	elif(("run" in inp) or("open" in inp)) and("calculator" in inp):
		pyttsx3.speak("ok I run calculator for you")
		os.system("calc")
		# it will give us hostname
	elif(("run" in inp) or("show" in inp)) and("hostname" in inp):
		pyttsx3.speak("ok here is the hostname")
		print(socket.gethostname())
		# it will give ip address
	elif(("run" in inp) or("show" in inp)) and("ip address" in inp):
		pyttsx3.speak("ok here is the ip address")
		print (socket.gethostbyname(socket.gethostname()))
		# it will play a song for us
	elif(("play" in inp) or("song" in inp)) and("terayaarsong" in inp):
		 pyttsx3.speak("ok here is the song for you")
		 mixer.init()
		 mixer.music.load("e:/song/Tera Yaar Hoon Main.mp3")
		 mixer.music.play()
		 # it will rename trytry.txt to try2.txt
	elif (("rename" in inp) or ("change" in inp)) and ("filename" in inp):
		 pyttsx3.speak("yes your filename updated ")
		 fd="try2.txt"
		 os.rename(fd,'try4.txt')
		 print("done")

		 # sending email
	elif ("send" in inp) and (("email" in inp) or ("mail" in inp)):
		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		pyttsx3.speak("Enter your email address")
		sender_email = input("Enter your email address")  # Enter your address
		pyttsx3.speak("Enter your receiver  address")
		receiver_email = input("Enter receiver address")  # Enter receiver address
		
		password = input("Type your password ")
	
		message = input("type your message")

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:

			server.login(sender_email, password)

			server.sendmail(sender_email, receiver_email, message)
			pyttsx3.speak("sent successfully")
			print("sent successfully")
		 
		 # quit

	elif("exit" in inp) or ("quit" in inp):
		break
	else:
		pyttsx3.speak("oops no support for this")
		print("oops no support for this")

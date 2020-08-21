import pyttsx3
import os
import webbrowser
import socket
from pygame import mixer


pyttsx3.speak("hello user lets chat")
while True:
	print("Hey lets chat" , end='')
	inp=input()
	# run chrome
	if(("run" in inp) or ("open" in inp)) and ("chrome" in inp):
		os.system("chrome")
		# run notepad
	elif(("run" in inp) or("execute" in inp)) and (("notepad" in inp) or("editor" in inp)):
		os.system("notepad")
		# run wmplayer
	elif("run" in inp) and("player" in inp) and ("media" in inp):
		os.system("wmplayer")
		# run paint
	elif(("run" in inp) or("open" in inp)) and("paint" in inp):
		os.system("mspaint")
		# run word
	elif(("run" in inp) or("open" in inp)) and("word" in inp):
		os.system("winword")
		# run excel
	elif(("run" in inp) or("open" in inp)) and("excel" in inp):
		os.system("excel")
		# run power point
	elif(("run" in inp) or("open" in inp)) and("power point" in inp):
		os.system("powerpnt")
		# run onenote
	elif(("run" in inp) or("open" in inp)) and("one note" in inp):
		os.system("onenote")
		# run outlook
	elif(("run" in inp) or("open" in inp)) and("outlook" in inp):
		os.system("outlook")
		# run current date
	elif(("run" in inp) or("show" in inp) or ("display" in inp)) and("date" in inp):
		os.system("date")
		# run current time
	elif(("run" in inp) or("show" in inp) or ("display" in inp)) and("time" in inp):
		os.system("time")
		# open amazon website
	elif(("run" in inp) or("open" in inp) or ("go" in inp)) and("amazon" in inp):
		webbrowser.open("amazon.in")
		# open yahoo website
	elif(("run" in inp) or("open" in inp) or ("go" in inp)) and("yahoo" in inp):
		webbrowser.open("yahoo.com")
		# open youtube
	elif(("run" in inp) or("open" in inp) or ("go" in inp)) and("youtube" in inp):
		webbrowser.open("youtube.com")
		# open calculator
	elif(("run" in inp) or("open" in inp)) and("calculator" in inp):
		os.system("calc")
		# it will give us hostname
	elif(("run" in inp) or("show" in inp)) and("hostname" in inp):
		print(socket.gethostname())
		# it will give ip address
	elif(("run" in inp) or("show" in inp)) and("ip address" in inp):
		print (socket.gethostbyname(socket.gethostname()))
		# it will play a song for us
	elif(("play" in inp) or("song" in inp)) and("terayaarsong" in inp):
		 mixer.init()
		 mixer.music.load("e:/song/Tera Yaar Hoon Main.mp3")
		 mixer.music.play()
		 # it will rename trytry.txt to try2.txt
	elif (("rename" in inp) or ("change" in inp)) and ("filename" in inp):
		 fd="trytry.txt"
		 os.rename(fd,'try2.txt')
		 print("done")
		 # quit

	elif("exit" in inp) or ("quit" in inp):
		break
	else:
		print("oops no support for this")

import pyttsx3
import subprocess as sp
import os
import speech_recognition as  sr
import webbrowser
def process_running():
	path=os.getcwd()               	#give the actual path of this file location
	sp.getoutput(f"tasklist >{path}\pro.txt") #add the output of the tasklist(gives the list of process running in win10)
												# from command shell and put in pro.txt file
	
speak=True                                    #for checking when to speak
pyttsx3.speak("Welcome\n \n")
print("Welcome\n \n")
pyttsx3.speak("enter your requirements... i am listening...")
print("enter your requirements... i am listening...")
r=sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio=None
		if speak:
			pyttsx3.speak(" Now start saying...")
			print("Now start saying...")
			audio=r.listen(source)
	
	try :
		ch=str(r.recognize_google(audio)).lower()
	#	print(f"u spoke {ch}")            			#what i have spoke 
	except Exception as e :
			f=open("pro.txt","r")       			#file opened
			word=f.read()							#read the file till the End of Line
			if "iexplore.exe" not in word:			#search the word chrome.exe in the file.
													#if found doesn't speak else speak the below command
				pyttsx3.speak(" please speak what u want to do ")
				print(" please speak what u want to do")
				speak=True
				continue 
	else:
		if(("run" in ch) or ("open" in ch)) and ("chrome" in ch): #chrome
			pyttsx3.speak("yes I run chrome")
			os.system("chrome")	
		
			speak=False
			process_running()

		elif  "calendar" in ch:
			webbrowser.open("http://192.168.43.250/cgi-bin/os2.py")
			speak=False 

		elif("date" in ch) and (("run" in ch ) or ("execute" in ch)):
			webbrowser.open("http://192.168.43.250/cgi-bin/os.py")
			speak=False 

		elif(("run" in ch) or("open" in ch) or ("go" in ch)) and("amazon" in ch): #amazon
			pyttsx3.speak("yes I run amazon website for you")
			webbrowser.open("amazon.in")
			speak=False

		elif(("run" in ch) or("execute" in ch)) and (("notepad" in ch) or("editor" in ch)): #notepad
			pyttsx3.speak("yes I open notepad for you")
			os.system("notepad")
			speak=False

		elif(("run" in ch) or("open" in ch)) and("calculator" in ch):
			pyttsx3.speak("ok I run calculator for you")
			os.system("calc")
			speak=False

			
			process_running()
		elif "exit" in ch:
			pyttsx3.speak("Ok Thank You for using me see u again..")
			break
		else:
			pyttsx3.speak("no support for this command")
			print("no support for this command")
	process_running()
			
			
import pyttsx3
import os
import time
print("Welcome.")

pyttsx3.speak("Hello. How can i help u with")

while True:
	print("What is your requirement:", end="")

	p=input()
	

	
	if(("Run" in p) or ("run" in p)) and (("mozilla" in p) or ("firefox" in p) or ("browser" in p)):
		print("Your requirement is",p)
		time.sleep(2)
		os.system("firefox")

	elif (("Run" in p) or ("run" in p) or ("Execute" in p)) and (("gedit" in p) or ("editor" in p) or ("notepad" in p)):
		print("Your requirement is",p)
		time.sleep(2)
		os.system("gedit")

	elif (("Run" in p) or ("run" in p)) and (("player" in p) or ("media" in p) or ("vlc" in p)):
		print("Your requirement is",p)
		time.sleep(2)
		os.system("vlc")

	elif ("exit" in p) or ("end" in p) or ("quit" in p):
		print("Thank You")
		pyttsx3.speak("Thank You")
		break
	else:
		print("Invalid Requirement.Doesn't Support")


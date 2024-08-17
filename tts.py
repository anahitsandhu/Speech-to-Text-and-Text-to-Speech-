import pyttsx3

converter=pyttsx3.init()
converter.setProperty('rate',150) #speed of speech
converter.setProperty('volume',1) #Volume level, 1 is max
voices=converter.getProperty('voices')
converter.setProperty('voice',voices[0].id)
text=input("Enter the text that you want to convert \n")

converter.say(text)
converter.runAndWait()


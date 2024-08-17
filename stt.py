#SPEECH TO TEXT 
import speech_recognition as sr

def speechTotext():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, Please wait")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening..")

        audio=recognizer.listen(source,timeout=5) #records until a pause is detected

        try:
            text=recognizer.recognize_google(audio) #recognize speech using google's speech recognition API
            print("You said:"+text)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.") #waits for 5 secs to display this 5 secs is specified as timeout
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e)) #problem connecting to Google API

if __name__=="__main__":
    speechTotext()

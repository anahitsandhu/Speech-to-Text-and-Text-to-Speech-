# Speech-to-Text-and-Text-to-Speech

This repository contains two files, first is an stt.py file that is a speech to text converter, here an Google Speech Recognition API is used to recognize the speech. speech_recognition library is imported, and the speech is listened to until a pause is detected, then the API recognizes the speech and converts it to text and it is printed on the terminal. If no speech is detected within 5 seconds then an error message is detected.
Second file is an tts.py file that is a text to speech converter. The pyttsx3 library is imported for the same. The text that needs to be converted to speech is made to be input by the user, and it is read out through the speaker of your device.
Both the files are done in the venv virtual environment.

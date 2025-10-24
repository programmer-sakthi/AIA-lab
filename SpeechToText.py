#experiment 11


# First, make sure you install the required packages:
# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now.")

        # Listen to the microphone
        audio = recognizer.listen(source)

    # Try recognizing the speech
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if _name_ == "_main_":
    recognize_speech_from_mic()
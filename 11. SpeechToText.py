# this wont work in collab
# you have to run it locally
# and most probably clg computers wont have a mic. So just display the code in that case

# perfrom these installations
# pip install sounddevice numpy SpeechRecognition scipy


import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write


def record_audio(duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording complete.")
    return np.int16(audio * 32767)


def speech_to_text():
    fs = 16000
    audio_data = record_audio(duration=5, fs=fs)

    # Convert to AudioData for SpeechRecognition
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), fs, 2)  # 2 bytes per sample

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("API error:", e)


speech_to_text()

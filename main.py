import pyttsx3
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

# Initialize Text-to-Speech Engine
tts_engine = pyttsx3.init()

def text_to_speech(text):
    """
    Convert text to speech and play it.
    """
    tts_engine.say(text)
    tts_engine.runAndWait()

def record_audio(filename, duration=5, fs=16000):
    """
    Record audio using the sounddevice library and save as a WAV file.
    """
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()  # Wait until the recording is finished
    wav.write(filename, fs, audio_data)
    print(f"Audio recorded and saved as {filename}")

def speech_to_text(audio_file):
    """
    Convert speech in a WAV file to text using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        print("Recognizing...")
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Text to Speech")
        print("2. Speech to Text")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to convert to speech: ")
            text_to_speech(text)

        elif choice == "2":
            print("Recording your voice...")
            audio_file = "temp_audio.wav"
            record_audio(audio_file, duration=5)  # Record 5 seconds of audio
            result = speech_to_text(audio_file)
            if result:
                text_to_speech(f"You said: {result}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

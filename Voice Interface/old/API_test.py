import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source, timeout=5)

try:
    recognized_text = recognizer.recognize_google(audio)
    print(f"You said: {recognized_text}")
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")

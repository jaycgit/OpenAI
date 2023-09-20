import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to capture speech and convert to text
def capture_speech():
    try:
        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source, timeout=5)  # Listen for audio for up to 5 seconds

        # Use Google Web Speech API to recognize speech
        text = recognizer.recognize_google(audio)

        return text
    except sr.WaitTimeoutError:
        print("Speech recognition timed out.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    spoken_text = capture_speech()

    if spoken_text:
        print(f"You said: {spoken_text}")


# Author: Jay Crispo
# Description: Flask app for sending speech to ChatGPT using OpenAI's GPT-3.
# Date: 9/21/2023

import logging
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

# Function to capture speech and convert to text using CMU Sphinx
def capture_speech():
    try:
        with sr.Microphone() as source:
            logging.info("Say something...")

            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source, timeout=10)  # Listen for audio for up to 10 seconds

        # Use CMU Sphinx to recognize speech (offline)
        text = recognizer.recognize_sphinx(audio)
        logging.info(f'Recognized Text: {text}')  # Log recognized text

        return text
    except sr.WaitTimeoutError:
        logging.error("Speech recognition timed out.")
    except sr.UnknownValueError:
        logging.error("Could not understand audio.")
    except sr.RequestError as e:
        logging.error(f"Could not request results; {e}")

if __name__ == "__main__":
    spoken_text = capture_speech()

    if spoken_text:
        print(f"You said: {spoken_text}")



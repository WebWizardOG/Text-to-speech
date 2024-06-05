from gtts import gTTS
import os

def robo_speaker(text, language='en'):
    # Create a text-to-speech object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech as an audio file
    tts.save("output.mp3")

    # Play the audio file
    os.system("start output.mp3")

if __name__ == "__main__":
    while True:
        # Take input from the user
        text_to_speak = input("Enter the text you want the robo speaker to say (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if text_to_speak.lower() == 'exit':
            print("Exiting the robo speaker. Goodbye!")
            break

        # Use the robo_speaker function with the user input
        robo_speaker(text_to_speak)

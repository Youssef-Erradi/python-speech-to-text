import speech_recognition as sr


def speech_to_text(file="french-audio.wav"):
    recognizer = sr.Recognizer()
    text = ""
    with sr.AudioFile(file) as audio_file:
        audio_text = recognizer.listen(audio_file)
        try:
            text = recognizer.recognize_google(audio_text, language="fr-Ca")
        except:
            print("Error : Probably you are not connected to the internet")
    return text


if __name__ == "__main__":
    text = speech_to_text()
    print(text)

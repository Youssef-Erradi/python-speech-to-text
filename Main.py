import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


def speech_to_text(file):
    recognizer = sr.Recognizer()
    text = ""
    with sr.AudioFile(file) as audio_file:
        audio_text = recognizer.listen(audio_file)
        try:
            text = recognizer.recognize_google(audio_text, language="fr-Ca")
        except:
            print("Error : Probably you are not connected to the internet")
    return text


def long_speech_to_text(file):
    sound = AudioSegment.from_wav(file)
    chunks = split_on_silence(
        sound, min_silence_len=1000, silence_thresh=sound.dBFS-14, keep_silence=500)
    folder_name = "chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        text += speech_to_text(chunk_filename)
    return text


if __name__ == "__main__":
    import time

    start_time = time.time()
    FILE = "audio/french-film-podcast.wav" #insert the path of an audio file here
    text = long_speech_to_text(FILE)
    print(text)
    print(f"----- The program took {time.time() - start_time} seconds to finish -----")

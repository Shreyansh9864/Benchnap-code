import pyaudio
import wave
import keyboard
import time
from pathlib import Path
from playsound import playsound
from openai import OpenAI
import warnings
import os
import speech_recognition as sr
warnings.simplefilter('ignore')
# Initialize OpenAI client
openai_api_key = OpenAI(api_key="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")


def speak(user):
    try:
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = openai_api_key.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=user,
        )

        response.stream_to_file(speech_file_path)

        if os.access(speech_file_path, os.R_OK):
            playsound(str(speech_file_path))
        else:
            print("Permission denied: Unable to play the audio file.")

    except Exception as e:
        print("An error occurred:", e)


def record_audio(output_file="Recording.wav"):
    FORMAT = pyaudio.paInt16
    RATE = 44100
    CHUNKS = 1024
    CHANNELS = 1

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, rate=RATE, channels=CHANNELS, input=True, frames_per_buffer=CHUNKS)
    frames = []

    print("Press space bar to start recording...")
    keyboard.wait('space')
    print("Recording... Press space bar to stop")
    time.sleep(0.2)
    while True:
        try:
            data = stream.read(CHUNKS)
            frames.append(data)
        except KeyboardInterrupt:
            break

        if keyboard.is_pressed('space'):
            print("Saving your audio, please wait...")
            time.sleep(0.5)  # Give a moment to finish recording
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wave_file = wave.open(output_file, "wb")
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    print("Recording saved as", output_file)


def transcribe_audio():
    try:
        audio_file = open("Recording.wav", "rb")
        transcription = openai_api_key.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
        return transcription
    except Exception as e:
        print("An error occurred during transcription:", e)
        return ""


def chat_with_openai(user_input):
    try:
        response = openai_api_key.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}],
        )
        return response.choices[0].message.content
    except Exception as e:
        print("An error occurred during chat:", e)
        return "I'm sorry, I couldn't understand."


while True:
    record_audio()
    transcription = transcribe_audio()
    print("Transcription:", transcription)

    if transcription.lower() == "quit":
        break

    response = chat_with_openai(transcription)
    speak(user=response)

    print("Response:", response)

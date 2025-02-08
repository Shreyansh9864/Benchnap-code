# from pathlib import Path
# from openai import OpenAI
# import playsound
# import warnings
# import openai
# import pyaudio
# import wave
# import keyboard
# import time
#
# # Ignore DeprecationWarning
# warnings.filterwarnings("ignore", category=DeprecationWarning)
#
# client = OpenAI()
# apikey = "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"
# openai_api_key = openai.OpenAI(api_key=apikey)
#
#
#
#
# def record_audio(output_file="Recording.wav"):
#     FORMAT = pyaudio.paInt16
#     RATE = 44100
#     CHUNKS = 1024
#     CHANNELS = 1
#
#     audio = pyaudio.PyAudio()
#     stream = audio.open(
#         format=FORMAT,
#         rate=RATE,
#         channels=CHANNELS,
#         input=True,
#         frames_per_buffer=CHUNKS,
#     )
#     frames = []
#
#     print("Press space bar to start recording...")
#     keyboard.wait('space')
#     print("Recording... Press space bar to stop")
#     time.sleep(0.2)
#     while True:
#         try:
#             data = stream.read(CHUNKS)
#             frames.append(data)
#         except KeyboardInterrupt:
#             break
#
#         if keyboard.is_pressed('space'):
#             print("Saving your audio, please wait...")
#             time.sleep(0.5)  # Give a moment to finish recording
#             break
#
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#
#     with wave.open(output_file, "wb") as wave_file:
#         wave_file.setnchannels(CHANNELS)
#         wave_file.setsampwidth(audio.get_sample_size(FORMAT))
#         wave_file.setframerate(RATE)
#         wave_file.writeframes(b''.join(frames))
#
#     print("Recording saved as", output_file)
#     FORMAT = pyaudio.paInt16
#     RATE = 44100
#     CHUNKS = 1024
#     CHANNELS = 1
#
#     audio = pyaudio.PyAudio()
#     stream = audio.open(
#         format=FORMAT,
#         rate=RATE,
#         channels=CHANNELS,
#         input=True,
#         frames_per_buffer=CHUNKS,
#     )
#     frames = []
#
#     print("Press space bar to start recording...")
#     keyboard.wait('space')
#     print("Recording... Press space bar to stop")
#     time.sleep(0.2)
#     while True:
#         try:
#             data = stream.read(CHUNKS)
#             frames.append(data)
#         except KeyboardInterrupt:
#             break
#
#         if keyboard.is_pressed('space'):
#             print("Saving your audio, please wait...")
#             time.sleep(0.5)  # Give a moment to finish recording
#             break
#
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#
#     with wave.open(output_file, "wb") as wave_file:
#         wave_file.setnchannels(CHANNELS)
#         wave_file.setsampwidth(audio.get_sample_size(FORMAT))
#         wave_file.setframerate(RATE)
#         wave_file.writeframes(b''.join(frames))
#
#     print("Recording saved as", output_file)
#
#
#     try:
#         audio_file = open("Recording.wav", "rb")
#         transcription = client.audio.transcriptions.create(
#             model="whisper-1",
#             file="Recording.wav",
#         )
#         print(transcription)
#     except Exception as e:
#         print("An error occurred:", e)
#
#
#
#     try:
#        response= openai_api_key.chat.completions.create(
#             model="gpt-4-turbo",
#             messages=[{"role": "user", "content": transcription}],
#         )
#         print(response)
#     except Exception as e:
#         print("Error", e)
#
#
#
#     try:
#         speech_file_path = Path(__file__).parent / "speech.mp3"
#         response = openai_api_key.audio.speech.create(
#             model="tts-1",
#             voice="shimmer",
#             input=response,
#         )
#
#         response.stream_to_file(speech_file_path)
#         playsound.playsound("speech.mp3")
#
#     except Exception as e:
#         print("An error occurred:", e)
#     else:
#         print("Speech generation and playback completed successfully.")
#
from pathlib import Path
from openai import OpenAI
import playsound
import warnings
import openai
import pyaudio
import wave
import keyboard
import time

# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

client = OpenAI()
apikey = "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"
openai_api_key = openai.OpenAI(api_key=apikey)

def record_and_transcribe_audio(output_file="Recording.wav"):
    try:
        FORMAT = pyaudio.paInt16
        RATE = 44100
        CHUNKS = 1024
        CHANNELS = 1

        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=FORMAT,
            rate=RATE,
            channels=CHANNELS,
            input=True,
            frames_per_buffer=CHUNKS,
        )
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

        with wave.open(output_file, "wb") as wave_file:
            wave_file.setnchannels(CHANNELS)
            wave_file.setsampwidth(audio.get_sample_size(FORMAT))
            wave_file.setframerate(RATE)
            wave_file.writeframes(b''.join(frames))

        print("Recording saved as", output_file)

    #     audio_file = open(output_file, "rb")
    #     transcription = client.audio.transcriptions.create(
    #         model="whisper-1",
    #         file=output_file,
    #     )
    #     print("Transcription:", transcription)
    #
    #     response = openai_api_key.chat.completions.create(
    #         model="gpt-4-turbo",
    #         messages=[{"role": "user", "content": transcription}],
    #     )
    #     print("Response:", response)
    #


record_and_transcribe_audio()

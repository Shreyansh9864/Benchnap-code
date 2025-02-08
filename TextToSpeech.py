from openai import OpenAI
openai_api_key = OpenAI(api_key="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")

response = openai_api_key.audio.speech.create(
        model = "tts-1",
        input="Please like and subscribe to benchNap.",
        voice="shimmer",
        response_format="speech.mp3",
)
response.stream_to_file("speech.mp3")
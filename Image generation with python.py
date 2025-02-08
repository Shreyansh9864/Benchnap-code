import openai
apikey = "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"
openai_api_key = openai.OpenAI(api_key=apikey)
user = str(input("prompt:"))
image = openai_api_key.images.generate(
    prompt=user,
    model= "dall-e-3",
    size = "1024x1024",
    quality="standard",
    n=1,

)
print(image)



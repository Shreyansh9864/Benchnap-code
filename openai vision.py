#Hello guy tody we will learn how to use OpenAI vvvvison to find the image
#1. Get Api key from The OpenAI website
#Let me copy my api key
import openai
from openai import OpenAI
apikey = "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"
openai_api_key = openai.OpenAI(api_key=apikey)
url = input("Enter the url:\n")  # user asking question to the OpenAi power bot
#Ohh forgot about the url
user = str(input("question:\n"))
response = openai_api_key.chat.completions.create(

  model="gpt-4-turbo", #The model name
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": user},
        {
          "type": "image_url",
          "image_url": {
            "url": url,
            "detail": "high"
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)
#Let us take a image from the google
#Plz like and sub scirbe tot he video for aamzing video like these so.,bye 
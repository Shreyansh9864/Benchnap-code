import google.generativeai as genai
# pip install google.generativeai
#You can get the api key from the the google studio website
api = genai.configure(api_key="AIzaSyDqhePOWzHwNpkOsB_jAoRAetkQD_t_hs0")
model = genai.GenerativeModel("gemini-pro")
#You can get the list of model at website # while True - infinite loop unitl it is true
while True:
    try:
        user = input("User:")

        response = model.generate_content(user)
        print(response.text)

    except Exception as e:
        print(e)

#   For free better alternative of Openai and you donot need key
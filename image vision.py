import cv2
import time
import requests
import base64

cap = cv2.VideoCapture(0)
result, recording = cap.read()
brightness = 50

if result:
    print("Taking the clip...")
    time.sleep(2)
    print("Taking the image")
    cv2.imwrite("My pic123.jpg", recording)

    with open("images.png", 'rb') as f:
        f.read()
        # OpenAI API Key
        api_key = "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"

        # Function to encode the image
        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

        user = input("Query:")
        # Path to your image
        image_path = r"C:\Users\rahul\PycharmProjects\Yt videos\images.png"

        # Getting the base64 string
        base64_image = encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        # Print the content from the JSON response
        print("Response Content:")
    import cv2
    import time
    import requests
    import base64

    cap = cv2.VideoCapture(0)
    result, recording = cap.read()
    brightness = 50

    if result:
        print("Taking the clip...")
        time.sleep(2)
        print("Taking the image")
        cv2.imwrite("My pic123.jpg", recording)

        with open("images.png", 'rb') as f:
            f.read()
            # OpenAI API Key
            api_key = "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"


            # Function to encode the image
            def encode_image(image_path):
                with open(image_path, "rb") as image_file:
                    return base64.b64encode(image_file.read()).decode('utf-8')


            user = input("Query:")
            # Path to your image
            image_path = r"C:\Users\rahul\PycharmProjects\Yt videos\images.png"

            # Getting the base64 string
            base64_image = encode_image(image_path)

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }

            payload = {
                "model": "gpt-4-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": user
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 300
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

            # Print the content from the JSON response


       wwww=onse.json
        if 'choices' in json_response:
            choices = json_response['choices']
            for choice in choices:
                print(choice['message']['content'])

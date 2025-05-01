from google import genai
from dotenv import load_dotenv
import os

load_dotenv() 
GEMINI_API_KEY = os.getenv("MY_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
def chat_with_bot(prompt):
    response = client.models.generate_content(
        model= "gemini-2.0-flash",
        contents= prompt
    )

    return response.text


if __name__ == "__main__":
    while True:
        user_input = input("You : ")
        if user_input in ["exit", "quit", "bye"]:
            break

        response = chat_with_bot(user_input)
        print("Chatbot : ", response)
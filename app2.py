from google import genai
from config import API

client=genai.Client(
    api_key=API

)

print("======="*50)
print("THIS is GEMINI POWERED CHAT BOT")
print("\n IF YOU WRITE EXIT THEN AI BOT WILL STOP")
print("===="*50)

while True:
    user_input=input("\n YOUR QUESTION:")
    if user_input.lower()=="exit":
        print("\n GOOD BYE")
        break

    response=client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_input
    )

    print("\n BOT ANSWER:",response.text)
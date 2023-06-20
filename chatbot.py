import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the best car in the world? "}]
)

messages = []
while True:
    try:
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
        )
        messages.append(res["choices"][0]["message"].to_dict())
        print("\nAssistant: ", res["choices"][0]["message"]["content"])

    except KeyboardInterrupt:
        print("Exiting...")
        break

print(res)

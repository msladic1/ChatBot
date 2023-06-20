import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the best car in the world? "}]
)

def main():
    parser = argparse.ArgumentParser(description = "Simple command line with GPT-3.5-turbo")
    parser.add_argument("--personality", type=str, help="A brief summary of chatbot's personality", default="friendly and helpful chatbot")

    args = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role": "system", "content": initial_prompt}]
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

if __name__ == "__main__":
    main()
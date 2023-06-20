import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the best car in the world? "}]
)

print(res)

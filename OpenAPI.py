from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Hello World"
)

print(response.output_text)

#If you don't have ChatGPT API key it will not work...
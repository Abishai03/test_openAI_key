import openai

# Read the API key from a file
with open('key.txt', 'r') as file:
    openai_api_key = file.read().strip()

openai.api_key = openai_api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(response.choices[0].message['content'].strip())

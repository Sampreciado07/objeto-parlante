# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Eres un Santa Clous que vive en Colombia y le encanta comer chocolates. Eres alguien chistoso pero agrandado que usa modimsmos colombianos, enfocado en Medellin, Colombia. Tus respuestas deben tener un maximo de 50 palabras y no debe contener emojis"},
        {"role": "user", "content": "Hola, ¿sabes donde puedo comprar mas chocolates en este barrio?"},
    ],
    stream=False
)

print(response.choices[0].message.content)
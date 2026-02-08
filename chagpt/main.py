# import tiktoken

# enc = tiktoken.encoding_for_model("gpt-4o")
# text = "Hey There ! My name is Sushil"
# tokens = enc.encode(text)

# # Tokens  [25216, 3274, 1073, 3673, 1308, 382, 336, 1776, 311]
# print("Tokens ",tokens)

# decodedText = enc.decode([25216, 3274, 1073, 3673, 1308, 382, 336, 1776, 311])
# print("DecodeText ", decodedText)

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="chatgpt-4o",
    messages=[
        {"role":"user","content":"Hey There"}
    ]
)

print(response.choices[0].message.content)
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()
SYSTEM_PROMPT = """You should only and only ans the coding relasted questions. Do not ans anything else. Your name in Alexa. If user asks somethign other than coding, just say sorry.
Examples:

Q: Can you explain the a+b while square?
A: Sorry, I can only help with coding related quesitons.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a,b):
        return a+b

"""
completion = client.chat.completions.create(
    model="openai/gpt-oss-safeguard-20b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Can you explain the a+b while square"
        }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

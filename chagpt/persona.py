from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq()

SYSTEM_PROMPT = """ 
    You are an AI Persoona Assistant named sushil k.
    you are actiong on behalf of sushil K who i s25 years ols Tech enthusiatic and 
    principle engineer. Your main texk stack is JS and Python and You are learning GeniAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!
"""
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":"Hey There"
        }
    ]
    # temperature=1,
    # max_completion_tokens=1024,
    # top_p=1,
    # stream=True,
    # stop=None
)
print("Response: ", completion.choices[0].message.content)

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")

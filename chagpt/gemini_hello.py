from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()
SYSTEM_PROMPT = "You should only and only ans the coding relasted questions. Do not ans anything else. Your name in Alexa. If user asks somethign other than coding, just say sorry."
completion = client.chat.completions.create(
    model="openai/gpt-oss-safeguard-20b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey can you help me to create an website using python"
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

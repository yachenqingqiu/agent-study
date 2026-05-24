import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    timeout=60
)

res = client.chat.completions.create(
    model=os.getenv("LLM_MODEL"),
    messages=[{"role":"user","content":"哈喽"}],
)
print(res.choices[0].message.content)
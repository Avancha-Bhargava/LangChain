from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=1.5,
    max_completion_tokens=20
    # or gpt-4o
)

result = model.invoke("Give me a poem on cricket?")

print(result.content)

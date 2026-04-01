from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

docs = [
    "Delhi is capital of India",
    "Kolkata is capital of WB",
    "Paris is the capital of France"
]

result = embedding.embed_documents(docs)

print(result)
print(len(result))

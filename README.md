# LangChain 🦜⛓️

> Hands-on LangChain experiments covering LLM models, chat models, embeddings, and document similarity — by **Bhargava Avancha**, AI/ML Engineer.

---

## Overview

This repository contains practical Python scripts exploring the **LangChain** framework integrated with **OpenAI** and **HuggingFace** APIs. The experiments cover the full spectrum from basic LLM invocation to advanced semantic document similarity using vector embeddings.

---

## Repository Structure

```
LangChain/
└── LLM Models/
    ├── llm_demo.py                  # Basic LLM call using OpenAI GPT-3.5 Turbo
    ├── chatmodel-openai.py          # Chat model using GPT-4o-mini with temperature control
    ├── chatmodel_hf_api.py          # Chat model using HuggingFace Mistral-7B via Inference API
    ├── embedding_openai_docs.py     # Document embedding using OpenAI text-embedding-3-large
    └── document_similarity.py       # Semantic document similarity using cosine similarity
```

---

## LLM Models

### `llm_demo.py`
Demonstrates basic LLM invocation using **LangChain's OpenAI wrapper** with the `gpt-3.5-turbo-instruct` model.
- Uses `load_dotenv` for secure API key management
- Calls `llm.invoke()` with a natural language query

### `chatmodel-openai.py`
Explores **ChatOpenAI** with the `gpt-4o-mini` model.
- Configures `temperature` (creativity level) and `max_completion_tokens`
- Uses `model.invoke()` with a prompt and extracts `result.content`

### `chatmodel_hf_api.py`
Uses **HuggingFace Inference API** via LangChain's `HuggingFaceEndpoint` to run the **Mistral-7B-Instruct** model.
- Connects to HuggingFace Hub using `HUGGINGFACEHUB_API_TOKEN`
- Configures `max_new_tokens`, `temperature`, and `task`

### `embedding_openai_docs.py`
Generates **vector embeddings** for multiple documents using **OpenAI's `text-embedding-3-large`** model.
- Embeds a list of sentences as 32-dimensional vectors
- Uses `embedding.embed_documents()` for batch embedding

### `document_similarity.py`
Implements **semantic document similarity search** using cosine similarity.
- Embeds a corpus of cricket player descriptions
- Embeds a user query and finds the most semantically similar document
- Uses `sklearn.metrics.pairwise.cosine_similarity` for scoring

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| LangChain | LLM orchestration framework |
| OpenAI API | GPT-3.5, GPT-4o, text-embedding-3-large |
| HuggingFace Hub | Mistral-7B-Instruct via Inference API |
| Scikit-learn | Cosine similarity computation |
| NumPy | Numerical computation |
| python-dotenv | Secure API key management |

---

## Getting Started

### Prerequisites

```bash
pip install langchain langchain-openai langchain-huggingface scikit-learn numpy python-dotenv
```

### Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

### Run a Script

```bash
git clone https://github.com/Avancha-Bhargava/LangChain.git
cd LangChain/LLM\ Models
python llm_demo.py
```

---

## Author

**Bhargava Avancha**  
AI/ML Engineer | Data Scientist | Cloud AI Architect  
Passionate about Conversational AI, NLP, and Scalable ML  
[LinkedIn](https://www.linkedin.com/in/avancha-bhargava/) | [GitHub](https://github.com/Avancha-Bhargava)

---

## License

This project is open source and available under the [MIT License](LICENSE).

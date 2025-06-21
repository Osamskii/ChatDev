import os
import requests


def test_ollama_chat():
    base_url = os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1")
    model = os.getenv("OLLAMA_MODEL", "llama3")
    data = {
        "model": model,
        "messages": [{"role": "user", "content": "Hello, world!"}],
        "stream": False,
    }
    resp = requests.post(f"{base_url}/chat/completions", json=data, timeout=5)
    resp.raise_for_status()
    js = resp.json()
    assert "choices" in js
    assert "message" in js["choices"][0]

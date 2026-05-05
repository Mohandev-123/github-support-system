"""List available free models on OpenRouter."""
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

print("Fetching available models from OpenRouter...\n")

try:
    response = requests.get(
        "https://openrouter.ai/api/v1/models",
        headers={"Authorization": f"Bearer {api_key}"}
    )

    if response.status_code == 200:
        models = response.json().get("data", [])

        # Filter free models
        free_models = [m for m in models if m.get("pricing", {}).get("prompt") == "0"]

        print(f"Found {len(free_models)} FREE models:\n")

        for i, model in enumerate(free_models[:15], 1):
            name = model.get("id", "unknown")
            print(f"{i:2}. {name}")

        print("\nPick one and update .env with MODEL=<id>")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Error: {e}")
    print("\nManual suggestions - try these model IDs:")
    print("  - gpt-3.5-turbo")
    print("  - meta-llama/llama-2-7b-chat")
    print("  - nousresearch/nous-hermes-2-mistral-7b-dpo")

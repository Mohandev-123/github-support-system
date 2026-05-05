"""Validate OpenRouter setup and test connection."""
import sys
from utils.llm_client import LLMClient, LLMConfig


def test_connection():
    """Test LLM connection."""
    print("🔍 Testing OpenRouter Connection")
    print("=" * 50)

    try:
        config = LLMConfig()
        print(f"✓ Provider: {config.api_provider}")
        print(f"✓ Model: {config.model}")
        print(f"✓ API Key loaded: {bool(config.openrouter_api_key)}")

        llm = LLMClient(config)

        # Test message
        messages = [
            {"role": "user", "content": "Say 'Connection successful!' in one sentence."}
        ]

        print("\n📤 Sending test message...")
        response = llm.generate(messages)
        print(f"✓ Response: {response}\n")
        print("✅ Connection test passed!\n")
        return True

    except Exception as e:
        print(f"❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)

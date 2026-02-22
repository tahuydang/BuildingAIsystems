import os
from dotenv import load_dotenv
from openai import OpenAI

def build_message(user_text: str)-> list[dict[str, str]]:
    return [
        {
            "role": "system", 
            "content": ("You are helpful assistant"
                        "Be concise, correct, and do not invent facts. "
                        "if unsure, say you are unsure")
        },
        {
            "role": "user", 
            "content": user_text
        }
    ]

def call_llm(client: OpenAI, user_text:str) -> str:
    messages = build_message(user_text)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=messages,
        max_tokens=1000,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return  
    
    client = OpenAI(base_url='https://openrouter.ai/api/v1', api_key=api_key)
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting the assistant. Goodbye!")
            break
        
        if not user_input:
            print("Please enter a valid message.")
            continue

        try:
            response = call_llm(client, user_input)
            print("Assistant:", response)
        except Exception as e:
            print(f"Error calling the language model: {e}")
            continue    

if __name__ == "__main__":
    main()
        

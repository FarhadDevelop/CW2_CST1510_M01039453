from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize client
client = OpenAI(api_key=api_key)    

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("ChatGPT Console Chat (type 'quit' to exit)")
print("-" * 50)

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Get AI response
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # Extract response
    assistant_message = completion.choices[0].message.content

    # Add assistant message to history
    messages.append({"role": "assistant", "content": assistant_message})

    # Display response
    print(f"AI: {assistant_message}\n")
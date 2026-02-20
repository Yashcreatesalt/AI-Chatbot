import time

def chatbot():
    print("--- AI Chatbot Initialized ---")
    print("Type 'quit' to exit.")
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm functioning at 100% capacity. Thank you for asking!",
        "who made you": "I am a project created for a GitHub portfolio.",
        "help": "I can answer simple greetings or tell you the time."
    }

    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        print("Chatbot: ", end="", flush=True)
        
        # Simple logic to find a response
        response = responses.get(user_input, "That's interesting! Tell me more about that.")
        
        # Simulate "thinking" speed
        for word in response.split():
            print(word, end=" ", flush=True)
            time.sleep(0.1)
        print("\n")

if __name__ == "__main__":
    chatbot()
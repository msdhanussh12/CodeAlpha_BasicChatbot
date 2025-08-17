import random

# Predefined responses
responses = {
    "hello": ["Hi there! 😊", "Hey! 👋", "Hello! How's your day going?"],
    "how are you": ["I'm doing great! Thanks for asking ❤️", "Feeling awesome today! 😄", "All good here! What about you?"],
    "bye": ["Goodbye! 👋", "See you later! 🌟", "Take care! ❤️"]
}

def chatbot():
    print("🤖 Chatbot: Hi! I'm your friendly assistant. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("💬 You: ").lower().strip()
        
        if user_input in responses:
            # Pick a random reply from the list
            reply = random.choice(responses[user_input])
            print(f"🤖 Chatbot: {reply}")
            
            if user_input == "bye":
                break
        else:
            print("🤖 Chatbot: Hmm 🤔 I don't know how to respond to that.")

# Run the chatbot
chatbot()

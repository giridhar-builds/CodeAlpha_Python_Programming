# =====================================================================
# TASK 4: BASIC CHATBOT
# =====================================================================
import sys

def get_bot_response(user_input):
    processed_input = user_input.strip().lower()

    if "hello" in processed_input or "hi" in processed_input:
        return "Hi there! I am your CodeAlpha helper bot. How can I assist you today?"
    elif "how are you" in processed_input:
        return "I'm doing great, thank you! Ready to help you write some code."
    elif "your name" in processed_input:
        return "I am AlphaBot, a simple rule-based AI built in Python."
    elif "bye" in processed_input or "goodbye" in processed_input:
        return "Goodbye! Have a fantastic day and happy coding!"
    else:
        return "I'm sorry, I didn't quite catch that. Could you please try asking differently?"

def run_chatbot():
    print("==========================================")
    print("      Welcome to AlphaBot Chat Service    ")
    print("   (Type 'bye' or 'exit' to end the chat) ")
    print("==========================================")
    
    while True:
        try:
            user_input = input("\nYou: ")
            
            if user_input.strip().lower() in ['exit', 'bye', 'goodbye']:
                print(f"Bot: {get_bot_response('bye')}")
                break
                
            response = get_bot_response(user_input)
            print(f"Bot: {response}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session interrupted. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    run_chatbot()

import json

def rule_based_chatbot():
    try:
        with open('responses.json', 'r') as file:
            responses = json.load(file)
    except FileNotFoundError:
        print("Error: 'responses.json' not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON in 'responses.json'.")
        return

    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    
    
    
    
    
    while True:
        user_input = input("You: " ,)
        clean_input = user_input.strip().lower()
        
        if(clean_input == "bye"):
            print("Chatbot: ",responses["bye"])
            break
        
        reply = responses.get(clean_input, "I'm sorry, I don't understand that question.")
        
        print("Chatbot: ",reply)

if __name__ == "__main__":
    rule_based_chatbot()
    
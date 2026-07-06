# Import the json module to work with JSON files
import json

# Function to run the chatbot
def rule_based_chatbot():

    # Try to open the JSON file and load the responses
    try:
        with open('responses.json', 'r') as file:
            responses = json.load(file)

    # If the file is not found, show an error message
    except FileNotFoundError:
        print("Error: 'responses.json' not found.")
        return

    # If the JSON file has invalid format, show an error
    except json.JSONDecodeError:
        print("Error: Invalid JSON in 'responses.json'.")
        return

    # Welcome message
    print("Chatbot: Hello! Type 'bye' to exit the chat.")

    # Keep asking the user for input until they type "bye"
    while True:

        # Take input from the user
        user_input = input("You: ")

        # Remove extra spaces and convert input to lowercase
        clean_input = user_input.strip().lower()

        # Check if the user wants to end the chat
        if clean_input == "bye":
            print("Chatbot:", responses["bye"])
            break

        # Find the response in the dictionary
        # If not found, return a default message
        reply = responses.get(
            clean_input,
            "I'm sorry, I don't understand that question."
        )

        # Print the chatbot's response
        print("Chatbot:", reply)

# Run the chatbot program
if __name__ == "__main__":
    rule_based_chatbot()
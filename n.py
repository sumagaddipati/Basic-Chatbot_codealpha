import spacy
import random

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a set of responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "name_query": ["I'm ChatBot.", "You can call me ChatBot.", "I'm a simple chatbot."],
    "name_provide": ["Nice to meet you, {name}!", "Hello {name}!", "Great to meet you, {name}!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "how_are_you": ["I'm just a program, but I'm here to help!", "I'm good, thanks for asking!", "I'm here to assist you!"],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "I'm here to help!"]
}

# Function to classify user input
def classify_input(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        elif token.lemma_ in ["bye", "goodbye", "later"]:
            return "farewell"
        elif token.lemma_ in ["name"]:
            return "name_query"
        elif token.lemma_ in ["thanks", "thank"]:
            return "thanks"
        elif token.lemma_ in ["how", "be"]:
            if any(t.lemma_ == "you" for t in doc):
                return "how_are_you"
        elif token.lemma_ in ["my", "i"]:
            if any(t.lemma_ == "name" for t in doc):
                return "name_provide"
    return "default"

# Function to generate a response based on the classification
def generate_response(classification, user_input=None):
    if classification == "name_provide":
        name = user_input.split()[-1]  # Assuming the name is the last word in the input
        return random.choice(responses[classification]).format(name=name)
    return random.choice(responses[classification])

# Main chatbot function
def chatbot():
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        classification = classify_input(user_input)
        response = generate_response(classification, user_input)
        print(f"ChatBot: {response}")

if _name_ == "_main_":
    chatbot()
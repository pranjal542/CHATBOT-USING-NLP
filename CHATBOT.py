import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')
nltk.download('stopwords')

pairs = [
    # General Greetings
    (r'hi|hello|hey', ['Hello! Welcome to [Your Store Name]. How can I assist you with our clothing products today?']),
    (r'how are you?', ['I am doing great, thank you for asking! How can I help you with your fashion needs today?']),
    (r'what is your name?', ['I am your clothing assistant chatbot. You can call me FashionBot!']),
    
    # Product-related Queries
    (r'what products do you sell?', ['We offer a variety of clothing including shirts, dresses, trousers, jackets, and accessories. What are you looking for?']),
    (r'(.*) dress(.*)', ['We have a wide selection of dresses, from casual to formal. What type of dress are you looking for?']),
    (r'(.*) shirt(.*)', ['We have many shirt styles—casual, formal, and graphic tees. What kind of shirt are you interested in?']),
    (r'(.*) trouser(.*)', ['We offer a variety of trousers for both men and women. What size are you looking for?']),
    (r'(.*) jacket(.*)', ['Our jacket collection includes both winter and fashion jackets. Would you like to know more?']),

    # Size-related Queries
    (r'what sizes do you offer?', ['We offer a range of sizes from XS to XXL for most of our clothing. Are you looking for a particular size?']),
    (r'what size is (.*)', ['Could you specify which item you are referring to? We offer different sizes for different clothing categories.']),
    
    # Pricing Queries
    (r'how much is (.*)', ['Our prices vary depending on the item. Could you specify which product you are interested in?']),
    (r'(.*) discount(.*)', ['We currently have a 20% discount on all items in our summer collection. Would you like to browse our discounted items?']),
    
    # Stock Availability
    (r'(.*) is in stock', ['Could you please specify the product you are looking for? I can check if it’s available.']),
    (r'(.*) size (.*) available', ['Let me check the availability of that size for you. Could you specify the item and size?']),
    
    # Order-related Queries
    (r'what is my order status?', ['I can check the status of your order. Could you please provide your order number?']),
    (r'(.*) order status(.*)', ['Please share your order number and I will fetch the details for you.']),
    
    # Business Location and Hours
    (r'where is your store located?', ['Our store is located at [Insert Address]. Would you like directions?']),
    (r'what are your store hours?', ['We are open from 9 AM to 6 PM, Monday to Saturday. Closed on Sundays.']),
    
    # Customer Support 
    (r'(.*) return(.*)', ['Our return policy allows returns within 30 days of purchase. Do you need help with a return?']),
    (r'(.*) exchange(.*)', ['We offer exchanges within 30 days of purchase. Would you like to exchange an item?']),
    
    #General Queries
    (r'(.*)', ['I’m sorry, I didn’t understand that. Could you please rephrase? Feel free to ask me about our clothing items or services.'])
]


chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

def start_chat():
    print("Hi! I'm your clothing store assistant. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("FashionBot: Goodbye! We hope to see you soon at our store!")
            break
        response = chatbot_response(user_input)
        print("FashionBot:", response)

if __name__ == "__main__":
    start_chat()

import random

responses = {
    'hi':['hello', 'Hey!'],
    'how are you':['Fine...', 'Good. thanks for asking'],
    'yes':['ok'],
    'default':['Ask another question', 'I cant understand']
}

def chat_res(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return random.choice(responses['default'])

print("Hello, I am a chatbot....")
while True:
    user_input = input()
    if(user_input.lower() == 'bye'):
        print('Goodbye...')
        break
    else:
        print(chat_res(user_input))

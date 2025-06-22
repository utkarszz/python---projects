from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
def chat_with_bot(user_input):
    # Generate a response from the chatbot
    response = chatbot(
        user_input,
          max_length=100,
            pad_token_id=50256,
         truncation = True,)
    
    return response[0]['generated_text']

print("\nStart chatting with the bot (type 'bye' to stop):")
while True:
    user_input = input("you:")
    if 'bye' in user_input.lower():
        print("Goodbye!")
        break
    response = chat_with_bot(user_input)
    print("bot:", response)
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
#from flask import Flask, request, jsonify
from userrespond import respond_to_user

'''app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['user_input']
    response = respond_to_user(user_input)
    return jsonify({'response': response})'''
from flask import Flask, render_template, request, jsonify


from transformers import AutoModelForCausalLM, AutoTokenizer
#import torch


'''tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")'''


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chatbot.html')

@app.route('/get_greeting', methods=['GET'])
def get_greeting():
    return "Hello, I'm a chatbot! How can I assist you today?"


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    
    if text.strip() == "":
        # If the user input is empty, then the chatbot sends a greeting message
        response = "Hello! How can I assist you today?"
    else:
    # Let's chat for 5 lines
    #for step in range(5):
        '''# encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)'''

        # pretty print last ouput tokens from bot
        response = respond_to_user(text)
    return response


if __name__ == '__main__':
    app.run()
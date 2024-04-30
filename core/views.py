from django.shortcuts import render
import openai, os
from dotenv import load_dotenv

load_dotenv()
api_key='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'
def process_message(message):
    # This is just an example. Replace this with your actual processing code.
    return f"You said: {message}"
def chatbot(request):
    chatbot_response = ''
    if request.method == 'POST':
        message = request.POST.get('message')
        chatbot_response = process_message(message)
        
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine ='gpt-3.5-turbo-instruct',
            prompt = prompt,
            max_tokens=256,
            temperature=0.5
        )
        print(response)
        chatbot_response = response["choices"][0]["text"]
        
    return render(request, 'main.html', {"response": chatbot_response})

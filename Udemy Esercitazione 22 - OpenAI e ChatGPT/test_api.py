import openai

#import os
#variabile = os.getenv("OPENAI_API_KEY")
#print(variabile)

#Definisce la propria api_key segreta, creata da Openai.com
openai.api_key = "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"

def test_api():
    risposta = openai.Completion.create(
        engine = "gpt-3.5-turbo-instruct",
        prompt = "Chi ha creato il linguaggio Python?",
        max_tokens = 50,
        n = 1,
        stop = None,
        temperature = 0.9,
    )
    print(risposta.choices[0].text.strip())

test_api()
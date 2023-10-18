import openai

#Definisce la propria api_key segreta, creata da Openai.com
#QUESTA QUI SOTTO NON E' PIU VALIDA, OCCORRE CREARNE UNA NUOVA DA OPENAI.COM
openai.api_key = "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"

#La classe ChatCompletion permette di implementare una
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo", #modello di chatgpt utilizzato.
    #La lista messages[] contiene degli oggetti che rappresentano i messaggi scambiati tra l'utente
    #e l'assistente virtuale. Ogni oggetto ha tre attributi principali:
    # "role": specifica il ruolo del messaggio
    #   - "system" => usato per fornire informazioni preliminari sulla conversazione all'assistente virtuale
    #   - "user" => richiesta da parte dell'utente.
    #   - "assistant" => generato dall'assistente in risposta ad una richiesta da "user"
    # "content": corpo del messaggio
    messages = [
        {"role": "user", "content": "Qual è il capoluogo della Toscana?"}
    ]
)
print(completion.choices[0].message.content)


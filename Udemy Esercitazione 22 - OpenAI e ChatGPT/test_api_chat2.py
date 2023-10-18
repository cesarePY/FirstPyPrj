import openai

#Definisce la propria api_key segreta, creata da Openai.com
openai.api_key = "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"


def chat_with_openai():
    #Dichiara chat_history come lista vuota
    chat_history = []

    #Loop infinito
    while True:
        #Chiede input a utente
        user_input = input("User: ")

        #Aggiungiamo alla lista il messaggio da passare all'API remote
        chat_history.append({"role": "user", "content": user_input})

        #Passiamo tutta la lista chat_history di messaggi precedentemente
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",  # modello di chatgpt utilizzato.
            messages = chat_history
        )

        #acquisiamo la risposta dell'assistente e la assegniamo ad una variabile assistant_response
        assistant_response = response.choices[0].message.get("content")
        print("Assistant: ", assistant_response)
        #Appendiamo la risposta alla lista chat_history
        chat_history.append({"role": "assistant", "content": assistant_response})
        #se l'input è fine usciamo dal loop infinito
        if user_input.lower() == "fine":
            break

chat_with_openai()

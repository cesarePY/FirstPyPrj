#Script che implementa un producer, cioè un programma che produce dati. Questo producer sfornerà 100000 messaggi
#sotto forma di stringa che rappresenta un numero che sale fino a 100000.
#Per fare questo utilizziamo una libreria "pika" che permette di interfacciarsi ad un message broker
#chiamato RabbitMQ, che deve essere preventivamente installato sulla macchina e deve essere in esecuzione
#se si vuole che questo script vi si possa collegare


#Importa la libreria pika che permette di interfacciarsi a RabbitMQ
import pika

print("Collegamento Producer a RabbitMQ...")

#instanzia una collezione di parametri, che nel nostro caso è semplicemente l'host al quale occorre collegarsi
#che è il server stesso. Questo vuol dire che sullo stesso computer stiamo eseguendo RabbitMQ da un
#terminale.
params = pika.ConnectionParameters(host="localhost")
#inizializza una connessione al broker
connection = pika.BlockingConnection(params)
#crea un canale sulla connessione, canale sul quale poi comunicherà
channel = connection.channel()

#definisce la coda di smistamento, questo caso è semplice, una sola coda, che verrà
#condivisa da tutti i consumer che si collegheranno.
channel.queue_declare(queue='worker_queue')

print("...collegamento eseguito")

#Qui sotto c'è un loop che produrra 100000 messaggi incrementali e li pubblicherà
#sul canale RabbitMQ appena creato
i = 0
while True:
    message = str(i)
    i += 1
    #istruzione che effettua la pubblicazione del messaggio creato ad ogni iterazione
    channel.basic_publish(exchange='', routing_key='worker_queue', body=message)
    print(f"Inviato messaggio {message}")
    if i > 100_000:
        break

#chiude la connessione alla fine
connection.close()
print("Connessione chiusa.")

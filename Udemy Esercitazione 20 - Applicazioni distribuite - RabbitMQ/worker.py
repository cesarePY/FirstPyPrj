import pika

print("Collegamento Worker a RabbitMQ...")

params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(params)
channel = connection.channel()
#Dichiara la coda che userà
channel.queue_declare(queue='worker_queue')

print("...collegamento eseguito")


#Definiamo una funzione per
def callback(ch, method, properties, body):
    print(f"Ricevuto {body}")


channel.basic_consume(on_message_callback=callback, queue='worker_queue', auto_ack=True)
channel.start_consuming()


#Chiude connessione
connection.close()
print("Connessione chiusa.")
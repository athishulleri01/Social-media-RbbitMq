import pika

# params = pika.URLParameters('amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml')
params = pika.URLParameters('amqps://imolrpcp:Bp9NYy5nBcacCY8Yv6vszmTS-u2om3i7@armadillo.rmq.cloudamqp.com/imolrpcp')


# params = pika.URLParameters('amqp://localhost:5672/')

try:
    connection = pika.BlockingConnection(params)
    print("Connection successful!")
    
except pika.exceptions.AMQPConnectionError as e:
    print(f"Error connecting to RabbitMQ: {e}")
    

channel = connection.channel()

queue_name = 'admin'

channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()

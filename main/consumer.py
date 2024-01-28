import pika
import json
# from product.models import Product
# params = pika.URLParameters('amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml')
# params = pika.URLParameters('amqp://localhost:5672/')
params = pika.URLParameters('amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml')


connection = pika.BlockingConnection(params)

channel = connection.channel()



# Declare the queue (create it if it doesn't exist)
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(data)
    print(properties.content_type)
    print("product createddddddd")
    
    # if properties.content_type =='product_created':
    #     product = Product()
    #     product.id = data['id']
    #     product.title = data['title']
    #     product.image = data['image']
    #     product.save()
    #     print(product)
    # elif properties.content_type =='product_updated':
    #     product = Product.objects.get(id=data['id'])
    #     product.title = data['title']
    #     product.image = data['image']
    #     product.save()
    # elif properties.content_type =='product_deleted':
    #     product = Product.objects.get(id=data['id'])
    #     product.delete()
    

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started consuming")
print(".........................................")

channel.start_consuming()



channel.close()


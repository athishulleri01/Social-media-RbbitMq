# amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml
import pika
import json
params = pika.URLParameters('amqps://rpqwkxml:4tTcurda2kDqPtwiQMSUcar7vFhA_W9a@armadillo.rmq.cloudamqp.com/rpqwkxml')
# params = pika.URLParameters('amqp://localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method,body):
    properties = pika.BasicProperties(method)
    print(properties,"......................")
    channel.basic_publish(exchange='', routing_key='main',body=json.dumps(body),properties=properties)
    
# publish()
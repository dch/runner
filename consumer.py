#!/usr/bin/env python2.7
import pika

params = pika.URLParameters('amqp://guest:guest@127.0.0.1:5672/koans')

conn = pika.BlockingConnection(parameters = params)
chan = conn.channel()
method_frame, header_frame, body = chan.basic_get('pubsub')
if method_frame:
    print(method_frame, header_frame)
    chan.basic_ack(method_frame.delivery_tag)
else:
    print('No message returned')

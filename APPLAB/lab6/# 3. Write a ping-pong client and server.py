# 3. Write a ping-pong client and server application. When a client sends a ping message to the
# server, the server will respond with a pong message. Other messages sent by the client can be
# safely dropped by the server.

from threading import *
from time import time
def respose(user):
    if (user=="ping"):
        print("pong")
    time.sleep(1)
t1=Thread(target=respose,args=("ping",))
t2=Thread(target=respose,args=("ting",))
t1.start()
t2.start()
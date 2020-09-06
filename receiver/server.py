# #!/usr/bin/python
# import socket
# import time
# HOST = '0.0.0.0'
# PORT = 9000
# BUF_SIZE = 98
#
# def listen():
#   # print 'Starting to listen'
#   fp = open('data.csv', 'a')
#   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   s.bind((HOST, PORT))
#   s.listen(3)
#   # conn, addr = s.accept()
#   # print 'Connection from: ' + str(addr)
#   while True:
#     conn, addr = s.accept()
#     conn_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
#     print 'New connection: ' + conn_time + ' ' + str(addr)
#     while True:
#       data = conn.recv(BUF_SIZE)
#       if not data:
#         break
#       fp.write(data + '\n')
#       fp.flush()
#       # print data
#
# if __name__ == '__main__':
#   listen()

from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError


class CarLocationServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b"\n")
                print(f'Received data: {data}')
                # await stream.write(data)
            except StreamClosedError:
                break
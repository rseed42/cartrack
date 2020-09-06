from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError


class CarLocationServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b'#')
                print(f'Received data: {data}')
            except StreamClosedError as err:
                print(f'--- Error ---')
                print(err)
                break

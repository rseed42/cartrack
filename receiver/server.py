from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
import logging


class CarLocationServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b'#')
                logging.debug(data)
            except StreamClosedError as err:
                logging.error(err)
                break

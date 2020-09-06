from tornado.ioloop import IOLoop
from receiver.util import load_config
from receiver.server import CarLocationServer
CONFIG_FILE = 'config.json'


def start_server():
    config = load_config(CONFIG_FILE)
    server = CarLocationServer()
    server.listen(config.port, config.host)
    IOLoop.current().start()


if __name__ == '__main__':
    print('--- Car Tracking Server ---')
    start_server()


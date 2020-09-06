from tornado.ioloop import IOLoop
from receiver.util import load_config
from receiver.server import CarLocationServer
from receiver.config import CarTrackerConfig
import logging.config


def start_server(config: CarTrackerConfig):
    server = CarLocationServer()
    server.listen(config.port, config.host)
    IOLoop.current().start()


if __name__ == '__main__':
    configuration = load_config('config.json')
    logging.config.dictConfig(configuration.logging)
    logging.info('--- Start Car Tracking Server ---')
    start_server(configuration)


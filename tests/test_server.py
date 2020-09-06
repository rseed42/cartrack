from pytest import fixture
from receiver.util import load_config
from receiver.config import CarTrackerConfig
from tornado.tcpclient import TCPClient
import random
CONFIG_FILE = '../config.json'


@fixture
def config() -> CarTrackerConfig:
    return load_config(CONFIG_FILE)


async def test_send_data(config: CarTrackerConfig):
    # Make sure to start the server beforehand!
    stream = await TCPClient().connect(config.host, config.port)
    for i in range(16384000):
        message = f'Please, check your number: {random.randint(0, 100):0>8}#'
        await stream.write(message.encode('utf-8'))
    pass


def test_cfg(config: CarTrackerConfig):
    assert config.host == '0.0.0.0'
    assert config.port == 9000

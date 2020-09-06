from pytest import fixture
from receiver.util import load_config
from receiver.config import CarTrackerConfig
CONFIG_FILE = '../config.json'


@fixture
def config() -> CarTrackerConfig:
    return load_config(CONFIG_FILE)


def test_server():
    pass


def test_cfg(config: CarTrackerConfig):
    assert config.host == '0.0.0.0'
    assert config.port == 9000

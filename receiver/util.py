import json
from .config import CarTrackerConfig


def load_config(config_file: str) -> CarTrackerConfig:
    with open(config_file) as fp:
        cfg = json.load(fp)
    return CarTrackerConfig(
        cfg['host'],
        cfg['port']
    )

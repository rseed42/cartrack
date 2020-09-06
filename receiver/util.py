from pathlib import Path
from .config import CarTrackerConfig


def load_config(config_path: Path) -> CarTrackerConfig:
    return CarTrackerConfig('0.0.0.0', 9000)

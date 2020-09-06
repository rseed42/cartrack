from dataclasses import dataclass


@dataclass(frozen=True)
class CarTrackerConfig:
    host: str
    port: int
    logging: dict

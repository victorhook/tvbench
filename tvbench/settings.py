from dataclasses import dataclass, asdict
from pathlib import Path
import os
import json


_PATH = Path(__file__).parent.joinpath('settings.json')


@dataclass
class Settings:
    color: str = '#ff3300'
    RPI = 'RPI' in os.environ
    DEBUG = 'DEBUG' in os.environ

    @classmethod
    def get(cls, key: str = None):
        try:
            with open(_PATH) as f:
                data = json.load(f)
        except FileNotFoundError:
            print('No previous settings found.')
            return {}

        if key is not None:
            return data[key]
        return data

    @classmethod
    def save(cls, key, value):
        settings = cls.get()
        settings[key] = value
        with open(_PATH, 'w') as f:
            json.dump(settings, f, indent=4)

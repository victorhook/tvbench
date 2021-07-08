from dataclasses import dataclass, asdict
from pathlib import Path
import json


_PATH = Path(__file__).parent.joinpath('settings.json')


@dataclass
class Settings:
    color: str = '#ff3300'

    @classmethod
    def load(cls) -> object:
        try:
            with open(_PATH) as f:
                return cls(**json.load(f))
        except json.decoder.JSONDecodeError:
            print('Failed to load settings from disk. Create new default ones.')
            return Settings()

    def save(self):
        with open(_PATH, 'w') as f:
            return json.dump(asdict(self), f, indent=4)


if __name__ == '__main__':
    settings = Settings.load()
    print(settings)
    settings.save()
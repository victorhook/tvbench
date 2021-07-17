from dataclasses import dataclass, asdict
import subprocess
from typing import List
import pickle
import re
import os

from settings import Settings


@dataclass
class Network:
    name: str
    channel: int
    rate: str
    signal: int
    active: bool

    def asdict(self):
        data = asdict(self)
        data.pop('active')
        return data


def sh(*args):
    pipe = subprocess.Popen(args, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = pipe.stderr.read()
    if err:
        print(f'ERROR: {err}')
    return pipe.stdout.read().decode('utf-8')


class Wifi:

    _nic = None

    @classmethod
    def _get_nic(cls):
        if cls._nic is None:
            try:
                response = sh('ip', 'link', 'show')
                match = re.search('[0-9]: (w.*)?:', response)
                cls._nic = match.group(1)
            except Exception as e:
                print(e)
                return None

        return cls._nic

    @classmethod
    def _valid_name(cls, ssid: str):
        return True

    @classmethod
    def get_networks(cls) -> List[Network]:
        if Settings.DEBUG:
            try:
                with open('cached_network', 'rb') as f:
                    return pickle.load(f)
            except:
                pass

        nic = cls._get_nic()

        lines = sh('nmcli', 'device', 'wifi').split('\n')
        lines = [re.sub('\s+', ' ', line) for line in lines]
        lines = list(filter(len, lines))

        networks = []
        for line in lines[1:]:
            line = line.split()

            active=line[0] == '*'
            offset = 1 if active else 0

            if Settings.RPI:
                name=line[offset+0]
                channel=line[offset+2]
                rate=line[offset+3] + ' ' + line[offset+4]
                signal=int(line[offset+5])
            else:
                name=line[offset+1]
                channel=line[offset+3]
                rate=line[offset+4] + ' ' + line[offset+5]
                try:
                    signal=int(line[offset+6])
                except:
                    signal=int(line[offset+7])

            if name == '--':
                continue

            try:
                networks.append(
                    Network(
                        name,
                        channel,
                        rate,
                        signal,
                        active
                    )
                )
            except Exception as e:
                print(line)
                print(e)


        if Settings.DEBUG:
            with open('cached_network', 'wb') as f:
                pickle.dump(networks, f)

        return networks

    @classmethod
    def is_connected(cls):
        return cls.get_state() == 'connected'

    @classmethod
    def get_state(cls):
        nic = cls._get_nic()
        lines = sh('nmcli', 'device').splitlines()
        lines = [re.sub('\s+', ' ', line) for line in lines[1:]]
        for line in lines:
            device, type_, state, con = line.split()
            if device == nic:
                return state

    @classmethod
    def connect(cls, ssid: str, password: str) -> None:
        res = sh('nmcli', 'device', 'wifi', 'connect', ssid, 'password', password)
        return 'successfully activated' in res

    @classmethod
    def disconnect(cls) -> bool:
        res = sh('nmcli', 'device', 'disconnect', cls._get_nic())
        return 'successfully disconnected' in res

    @classmethod
    def get_connected_network(cls, networks: List[Network]) -> Network:
        for network in networks:
            if network.active:
                return network

    @classmethod
    def get_ip(cls) -> str:
        try:
            ip = re.search('inet4 (.*)/', sh('nmcli')).group(1)
        except:
            ip = '127.0.0.1'
        return ip


def sanity_test():
    print('Networks: ')
    print('\n'.join(str(n) for n in Wifi.get_networks()))
    print('Ip: %s' % Wifi.get_ip())
    print('State: %s' % Wifi.get_state())
    print('Nic: %s' % Wifi._get_nic())


if __name__ == '__main__':
    sanity_test()
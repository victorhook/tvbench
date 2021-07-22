from flask import Flask, render_template, jsonify, request
import os
app = Flask(__name__)

from wifi import Wifi
from settings import Settings
from ledstrip import Ledstrip, Color


led = Ledstrip()
if Settings.get('on'):
    led.on()
else:
    led.off()

LISTEN_PORT = os.environ.get('PORT', '?')

@app.route('/')
def index():
    networks = Wifi.get_networks()
    connection = Wifi.get_connected_network(networks)
    return render_template('index.html',
        **{
            'ip': Wifi.get_ip(),
            'port': LISTEN_PORT,
            'color': Settings.get('color'),
            'light_on': Settings.get('on'),
            'networks': networks,
            'connection': connection
        }
    )

@app.route('/on/')
def on():
    print('on')
    led.on()
    return jsonify({'result': 'OK'})


@app.route('/off/')
def off():
    print('off')
    led.off()
    return jsonify({'result': 'OK'})


@app.route('/color/<string:color>/')
def set_color(color):
    led.save_color('#' + color)
    led.show()
    return jsonify({'result': 'OK'})


def resultify(boolean_result):
    return 'OK' if boolean_result else 'NOT_OK'


@app.route('/connect/<string:wifi>/<string:password>/')
def connect(wifi, password):
    connected = Wifi.connect(wifi, password)
    return jsonify({'result': resultify(connected)})


@app.route('/disconnect/')
def disconnect():
    result = Wifi.disconnect()
    return jsonify({'result': resultify(result)})


@app.route('/reboot/')
def reboot():
    if Settings.RPI:
        os.system('reboot')

    return jsonify({'result': 'OK'})

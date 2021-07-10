from flask import Flask, render_template, jsonify
app = Flask(__name__)

from wifi import Wifi
from ledstrip import Ledstrip, Color


led = Ledstrip()

@app.route('/')
def hello_world():
    networks = Wifi.get_networks()
    connection = Wifi.get_connected_network(networks)
    return render_template('index.html',
        **{
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
    color = Color(
        int(color[:2], 16),
        int(color[2:4], 16),
        int(color[4:6], 16)
    )
    led.set_color(color)

    return jsonify({'result': 'OK'})

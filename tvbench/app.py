from flask import Flask, render_template
app = Flask(__name__)

from wifi import Wifi


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
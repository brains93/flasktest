from flask import Flask, request, render_template
import requests
import subprocess
import os

app = Flask(__name__)
#wifi = subprocess.check_output(['nmcli', 'dev', 'wifi'])
#type(wifi)

internet = ""
interfaces = []
 
@app.route('/')
def index():
    interfaces = os.listdir('/sys/class/net/')
    try: 
        requests.get("https://www.google.com")
        internet = "Internet connected"
    except:
        internet = "no internet connection"
    return render_template('index.html', internet=internet, interfaces=interfaces)

@app.route('/connect')
def command():
    #ssid = request.args.get("ssid")
    #password = request.args.get("password")
    #subprocess.check_output([f"nmcli dev wifi connect {ssid} password {password}"], shell=True)
    return subprocess.check_output(["nmcli", "dev", "wifi", "connect", f"{ssid}", "password" f"{password}", "iface", "wlan0"], shell=True)

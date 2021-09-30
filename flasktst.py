from flask import Flask, request, render_template, redirect, url_for
#from wireless import Wireless
#import connection as Finder
import requests
import subprocess
import os

app = Flask(__name__)
#wifi = subprocess.check_output(['nmcli', 'dev', 'wifi'])
#type(wifi)

internet = ""
interfaces = []
#wireless = wireless()
 
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
    ssid = request.args.get("ssid")
    password = request.args.get("password")
    print(ssid, password)
    #subprocess.check_output(["/usr/bin/nmcli", "dev", "wifi", f"connect {ssid}", f"password {password}", "iface", "wlan0"], shell=True)
    #return wireless.connect(ssid=ssid, password=passwor
    bashCommand = f"/usr/bin/nmcli dev wifi connect {ssid} password {password}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


    return redirect("/")

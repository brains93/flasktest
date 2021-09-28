from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)
#wifi = subprocess.check_output(['nmcli', 'dev', 'wifi'])
#type(wifi)



 
@app.route('/')
def index():
    result_success = subprocess.check_output(["ifconfig"], shell=True)
    return render_template('index.html')

@app.route('/connect')
def command():
    ssid = request.args.get("ssid")
    password = request.args.get("password")
    #subprocess.check_output([f"nmcli dev wifi connect {ssid} password {password}"], shell=True)
    work = subprocess.check_output(["nmcli", "dev", "wifi", "connect", f"{ssid}", "password" f"{password}", "iface", "wlan0"], shell=True)
    return work
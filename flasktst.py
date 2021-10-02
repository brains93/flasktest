<<<<<<< HEAD
from flask import Flask, request, render_template, redirect, url_for
#from wireless import Wireless
#import connection as Finder
=======
from flask import Flask, request, render_template, redirect
>>>>>>> fac185ef378dcece2cf007d4666fc0b015014862
import requests
import subprocess
import os

app = Flask(__name__)

#sets up verables 
internet = ""
interfaces = []

#function to run shell commands
def runshell(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
 
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
<<<<<<< HEAD
    #take input from the HTTP Get request and assigns it to a vaerable
    #Needs changed to Post requests 
    ssid = request.args.get("ssid")
    password = request.args.get("password")
    interface = request.args.get("interface")
    
    #sets up WiFi connection command 
    Command = f"/usr/bin/nmcli dev wifi connect {ssid} password {password} ifname {interface}"
    runshell(Command)
    #redirects back to main page 
=======
    ssid = request.args.get("ssid")
    password = request.args.get("password")
    command = f"/usr/bin/nmcli dev wifi connect {ssid} password {password}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
>>>>>>> fac185ef378dcece2cf007d4666fc0b015014862
    return redirect("/")

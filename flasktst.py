from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/script')
def command():
    result_success = subprocess.check_output(["ifconfig"], shell=True)
    return result_success
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vmd_timestamp')
def vmd_timestamp():
    return render_template('vmd_timestamp.html')
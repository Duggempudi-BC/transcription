import argparse
import io
import os
import whisper
import torch
from datetime import datetime, timedelta
from queue import Queue
from tempfile import NamedTemporaryFile
from time import sleep
from sys import platform

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

transcription = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files['audio']
    temp_file = NamedTemporaryFile().name
    audio.save(temp_file)

    model = "medium"
    audio_model = whisper.load_model(model)

    result = audio_model.transcribe(temp_file, fp16=True)  # Enable fp16 for GPU usage
    text = result['text'].strip()

    return jsonify({'text': text})

if __name__ == "__main__":
    app.run(debug=True)
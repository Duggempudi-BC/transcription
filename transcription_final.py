# import torch
# import torchaudio
# from flask import Flask, render_template, request
# import whisper

# app = Flask(__name__)

# # Load the Whisper model
# model = whisper.load_model('medium.en')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process-audio', methods=['POST'])
# def process_audio():
#     # audio = request.files['audio']
#     # waveform, sample_rate = torchaudio.load(audio, normalize=True)

#     # # Convert the audio to mono if required
#     # if waveform.shape[0] > 1:
#     #     waveform = torchaudio.transforms.DownmixMono()(waveform)

#     # # Preprocess the audio if required
#     # # For example, resample the audio to the expected sample rate
#     # if sample_rate != 16000:
#     #     resampler = torchaudio.transforms.Resample(sample_rate, 16000)
#     #     waveform = resampler(waveform)
#     #     sample_rate = 16000

#     # # Run the Whisper model on the audio waveform
#     # input_values = model.feature_extractor(waveform, mask=False).input_values
#     # with torch.no_grad():
#     #     logits = model(input_values).logits

#     # # Transcribe the logits using the model's transcribe() method
#     # transcription = model.transcribe(logits)

#     audio_file = request.files['audio']
#             # Save the audio file to a desired location
#     audio_file.save('static/wav/audio.webm')
#     transcription = model.transcribe('static/wav/audio.webm')

#     # Return the transcription to the client
#     return transcription

# if __name__ == '__main__':
#     app.run(debug=True)



import torch
import torchaudio
from flask import Flask, render_template, request
import whisper
import socketio
import time

app = Flask(__name__)

# Load the Whisper model
model = whisper.load_model('medium.en')

transcription = ""
current_file_index = 0

transcription = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-audio', methods=['POST'])
def process_audio():
    global transcription
    audio_file = request.files['audio']
    
    audio_file.save('static/wav/audio.webm')

    
    time.sleep(5)
    # Transcribe the current audio chunk
    current_transcription = model.transcribe('static/wav/audio.webm')

    # If transcription is empty, assign the current transcription
    # if transcription == "":
    #     transcription = current_transcription
    # else:
    #     # Append the current transcription to the existing transcription
    #     transcription += " " + current_transcription

    # Emit the current transcription to the frontend using Socket.IO
    # socketio.emit('transcription_update', {'transcription': current_transcription}, broadcast=True)

    # Return the transcription to the client (optional)
    time.sleep(1)
    return current_transcription



    # global transcription
    # global current_file_index

    # audio_file = request.files['audio']
    
    # # Determine the filename based on the current file index
    # filename = f'static/wav/audio{current_file_index}.webm'
    
    # # Save the audio file
    # audio_file.save(filename)

    # # Transcribe the current audio file
    # current_transcription = model.transcribe(filename)

    # # If transcription is empty, assign the current transcription
    # if transcription == "":
    #     transcription = current_transcription
    # else:
    #     # Append the current transcription to the existing transcription
    #     transcription += " " + current_transcription

    # # Increment the file index for the next audio file
    # current_file_index = 1 - current_file_index

    # # Return the transcription to the client (optional)
    # return current_transcription

if __name__ == '__main__':
    app.run(debug=True)

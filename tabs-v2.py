from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Store conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcription', methods=['POST'])
def transcription():
    data = request.json
    transcript = data.get('transcript')
    if transcript:
        conversation_history.append(transcript)
        socketio.emit('new_transcript', {'transcript': transcript})
    return jsonify({"status": "received"}), 200

@app.route('/message_click', methods=['POST'])
def message_click():
    data = request.json
    message = data.get('message')
    # Handle the message click (call your endpoint or perform some action)
    print(f"Message clicked: {message}")
    return jsonify({"status": "clicked"}), 200

if __name__ == '__main__':
    socketio.run(app, port=5000)
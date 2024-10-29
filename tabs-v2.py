from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import markdown2  # We'll use markdown2 to convert markdown to HTML

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
    # Handle the message click (return markdown content)
    markdown_content = f"""
### ⚠️ Fact Check: Likely false ⚠️

The last 851 times Sharon said she was “not hungry”, she was actually very hungry.

|statement|valid|result|
|---|---|---|
|I am not hungry|❌|Sharon ate 7 chicken wings|
|I will be there in 5 minutes|❌|Sharon arrived 30 minutes later|
|I don't need a dessert|❌|Sharon ordered a chocolate cake|
|I will start my diet tomorrow|❌|Sharon ate a pizza for breakfast|
    """
    html_content = markdown2.markdown(markdown_content, extras=["tables"])
    return jsonify({"html_content": html_content}), 200

if __name__ == '__main__':
    socketio.run(app, port=5000)
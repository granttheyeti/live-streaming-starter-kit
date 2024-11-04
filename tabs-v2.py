from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import markdown2
import time

from tabs_black_box_sdk import FoundryClient
from foundry_sdk_runtime.auth import UserTokenAuth
from tabs_black_box_sdk.types import ActionConfig, ActionMode, ValidationResult, ReturnEditsMode

auth = UserTokenAuth(hostname="https://granttheyeti.usw-16.palantirfoundry.com/", token=os.environ["FOUNDRY_TOKEN"])
client = FoundryClient(auth=auth, hostname="https://granttheyeti.usw-16.palantirfoundry.com/")

app = Flask(__name__)
socketio = SocketIO(app)

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
    result = client.ontology.queries.fact_check_statement(
        statement=message
    )
    html_content = markdown2.markdown(result, extras=["tables"])
    return jsonify({"html_content": html_content}), 200

if __name__ == '__main__':
    socketio.run(app, port=5000)
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import markdown2  # We'll use markdown2 to convert markdown to HTML
import time

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

|time|statement|valid|correction|
|---|---|---|---|
|10/22 @ 2:32 pm|I am not hungry|❌|Sharon ate 7 chicken wings|
|10/15 @ 8:45 pm|I don't want a dessert|❌|Sharon ate all of Jay's ice cream|
|10/10 @ 3:20 pm|I won't have any snacks today|❌|Sharon ate 3 bags of chips|
|10/3 @ 4:00 pm|I am full|❌|Sharon asked for a second serving|
|...|...|...|...|
    """

    markdown_content2 = f"""
### 💸 Jay's Generosity Tracker 💸

Jay has generously picked up the bill the last 4 times they dined out. Here are the details:

|time|meal|payer|amount|
|---|---|---|---|
|10/22 @ 2:32 pm|McDonald's|Jay|$20|
|10/15 @ 7:15 pm|Pizza Hut|Jay|$35|
|10/10 @ 1:00 pm|Subway|Jay|$15|
|10/3 @ 6:45 pm|KFC|Jay|$25|
|...|...|...|...|
"""

    markdown_content3 = f"""
### 🚗 Sharon's Car Wash Requests 🚗

Sharon has asked Jay to wash the car approximately 1.2 million times. Here are a few examples:

|time|request|
|---|---|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 2:00 am|wash the car|
|10/22 @ 1:59 am|wash the car|
|10/22 @ 1:59 am|wash the car|
|...|...|
"""
    time.sleep(2)
    html_content = markdown2.markdown(markdown_content3, extras=["tables"])
    return jsonify({"html_content": html_content}), 200

if __name__ == '__main__':
    socketio.run(app, port=5000)
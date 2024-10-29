from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transcription', methods=['POST'])
def transcription():
    data = request.json
    print(data)
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
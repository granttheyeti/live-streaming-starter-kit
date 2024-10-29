import requests
import time

def send_transcription(transcript):
    url = "http://127.0.0.1:5000/transcription"
    response = requests.post(url, json={"transcript": transcript})
    print(f"Transcription Response: {response.json()}")

if __name__ == "__main__":
    test_transcriptions = [
        "Hello, how are you?",
        "I'm testing the Flask endpoints.",
        "This is a test message.",
        "Clicking on this message should return markdown.",
        "Another test message to verify."
    ]

    # Send transcription data
    for transcript in test_transcriptions:
        send_transcription(transcript)
        time.sleep(0.25)  # Wait a bit between requests to simulate real-time data


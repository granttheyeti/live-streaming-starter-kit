import requests
import time

def send_transcription(transcript):
    url = "http://127.0.0.1:5000/transcription"
    response = requests.post(url, json={"transcript": transcript})
    print(f"Transcription Response: {response.json()}")

if __name__ == "__main__":
    test_transcriptions = [
        "What do you want to eat?",
        "I'm not hungry",
        "Not hungry, huh?",
        "What are you doing?",
    ]

    test_transcriptions2 = [
        "hey, I'll pay this time because you paid last time",
        "and the time before that",
        "What?",
        "I actually paid for the past 5 times totally $143",
        "Oh right, I forgot you are keeping tabs"
    ]

    test_transcriptions3 = [
        "Well, since you like keeping tabs. I told you a million times to wash the car",
        "You did not. You…",
    ]
    # Send transcription data
    for transcript in test_transcriptions3:
        send_transcription(transcript)
        time.sleep(0.25)  # Wait a bit between requests to simulate real-time data


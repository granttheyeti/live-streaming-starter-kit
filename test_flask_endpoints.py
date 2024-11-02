import requests
import time
import os

from tabs_pass_thru_logic_test_sdk import FoundryClient
from foundry_sdk_runtime.auth import UserTokenAuth
from tabs_pass_thru_logic_test_sdk.types import ActionConfig, ActionMode, ValidationResult, ReturnEditsMode

auth = UserTokenAuth(hostname="https://granttheyeti.usw-16.palantirfoundry.com/", token=os.environ["FOUNDRY_TOKEN"])
client = FoundryClient(auth=auth, hostname="https://granttheyeti.usw-16.palantirfoundry.com/")

def send_statement(statement):
    response = client.ontology.actions.create_statement_pass_thru_logic_action(
        action_config=ActionConfig(
            mode=ActionMode.VALIDATE_AND_EXECUTE,
            return_edits=ReturnEditsMode.ALL),
        statement=statement
    )
    # Check if the validation was successful
    print(response.validation)
    if response.validation.validation_result == ValidationResult.VALID:
        # If ReturnEditsMode.ALL is used, new and updated objects edits will contain the primary key of the object
        if response.edits.type == "edits":
            print(response.edits)

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

    # what are you doing
    # mouse moves to I'm not hungry

    test_transcriptions2 = [
        "hey, I'll pay this time because you paid last time",
        "and the time before that",
        "What?",
        "I actually paid for the past 5 times totaling $143",
        "Oh right, I forgot you are keeping tabs"
    ]

    test_transcriptions3 = [
        "Well, since you like keeping tabs. I told you a million times to wash the car",
        "No, you did not.",
    ]

    send_statement("Thank you Jay for paying for $200 cheeze pizza.")

    # Send transcription data
    for transcript in test_transcriptions3:
        # send_transcription(transcript)
        time.sleep(2)  # Wait a bit between requests to simulate real-time data

# thanks Jay for paying for my $25 BBQ ribs potato at this airport bbq
# thanks Jay for paying for my $15 baked potato at this airport bbq

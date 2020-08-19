import requests
import json


def send():
    print("--> Sending message to Slack")

    r = requests.post(
        "https://hooks.slack.com/services/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",
        json={"text": "Knock, knock"},
    )

    print("*** Sent message to Slack ***")

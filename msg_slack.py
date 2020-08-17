import requests
import json


def send():
    r = requests.post(
        "https://hooks.slack.com/services/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",
        json={"text": "Knock, knock"},
    )

    print("** Sent message to Slack **")

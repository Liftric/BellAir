import requests
import json


def send():
    print("--> Sending message to Microsoft Teams")

    json = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": "Knock, knock",
        "sections": [
            {
                "activityTitle": "![TestImage](https://s3.eu-central-1.amazonaws.com/static.coolgift.com/media/cache/sylius_shop_product_large_thumbnail/product/Cat%20Doorbell%206.jpg)Somebody is at the door!",
                "activitySubtitle": "Please open",
                "activityImage": "https://s3.eu-central-1.amazonaws.com/static.coolgift.com/media/cache/sylius_shop_product_large_thumbnail/product/Cat%20Doorbell%206.jpg",
                "facts": [
                    {"name": "Time of ring", "value": "2 seconds ago"},
                    {"name": "Status", "value": "Still not open"},
                ],
                "markdown": True,
            }
        ],
        "potentialAction": [
            {
                "@type": "ActionCard",
                "name": "I'm on it",
                "actions": [
                    {
                        "@type": "HttpPOST",
                        "name": "... can't remove properly...",
                        "target": "http://...",
                    }
                ],
            },
            {
                "@type": "ActionCard",
                "name": "I'm busy",
                "actions": [
                    {
                        "@type": "HttpPOST",
                        "name": "... can't remove properly...",
                        "target": "http://...",
                    }
                ],
            },
            {
                "@type": "ActionCard",
                "name": "Comment",
                "inputs": [
                    {
                        "@type": "TextInput",
                        "id": "comment",
                        "isMultiline": False,
                        "title": "Add a comment here for this task",
                    }
                ],
                "actions": [
                    {"@type": "HttpPOST", "name": "Add comment", "target": "http://..."}
                ],
            },
        ],
    }

    r = requests.post(
        "https://outlook.office.com/webhook/1f22a732-2111-4907-9630-96f345a6b3fb@acfcc1cc-3b63-45f2-922f-3d276cf082cd/IncomingWebhook/014090b7aafb464e87ae82417bc45ea6/61af98de-7dab-467c-a757-8ca655d94c50",
        json=json,
    )

    print("--> Sent message to Microsoft Teams")

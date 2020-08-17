import requests
import json


def send():
    json = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": "Larry Bryant created a new task",
        "sections": [
            {
                "activityTitle": "![TestImage](https://47a92947.ngrok.io/Content/Images/default.png)Larry Bryant created a new task",
                "activitySubtitle": "On Project Tango",
                "activityImage": "https://teamsnodesample.azurewebsites.net/static/img/image5.png",
                "facts": [
                    {"name": "Assigned to", "value": "Unassigned"},
                    {
                        "name": "Due date",
                        "value": "Mon May 01 2017 17:07:18 GMT-0700 (Pacific Daylight Time)",
                    },
                    {"name": "Status", "value": "Not started"},
                ],
                "markdown": True,
            }
        ],
        "potentialAction": [
            {
                "@type": "ActionCard",
                "name": "Add a comment",
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
            {
                "@type": "ActionCard",
                "name": "Set due date",
                "inputs": [
                    {
                        "@type": "DateInput",
                        "id": "dueDate",
                        "title": "Enter a due date for this task",
                    }
                ],
                "actions": [
                    {"@type": "HttpPOST", "name": "Save", "target": "http://..."}
                ],
            },
            {
                "@type": "ActionCard",
                "name": "Change status",
                "inputs": [
                    {
                        "@type": "MultichoiceInput",
                        "id": "list",
                        "title": "Select a status",
                        "isMultiSelect": "false",
                        "choices": [
                            {"display": "In Progress", "value": "1"},
                            {"display": "Active", "value": "2"},
                            {"display": "Closed", "value": "3"},
                        ],
                    }
                ],
                "actions": [
                    {"@type": "HttpPOST", "name": "Save", "target": "http://..."}
                ],
            },
        ],
    }

    r = requests.post(
        "https://outlook.office.com/webhook/1f22a732-2111-4907-9630-96f345a6b3fb@acfcc1cc-3b63-45f2-922f-3d276cf082cd/IncomingWebhook/014090b7aafb464e87ae82417bc45ea6/61af98de-7dab-467c-a757-8ca655d94c50",
        json=json,
    )

    print("** Sent message to MS Teams **")

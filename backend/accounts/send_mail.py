from mailjet_rest import Client
from django.conf import settings

api_key = settings.MAILJET_KEY
api_secret = settings.MAILJET_SECRET

def send(receiver, subject, body):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": settings.EMAIL_FROM,
                    "Name": settings.EMAIL_FROM_NAME
                },
                "To": [
                    {
                        "Email": receiver,
                    }
                ],
                "Subject": subject,
                "TextPart": "",
                "HTMLPart": body,
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    mailjet.send.create(data=data)

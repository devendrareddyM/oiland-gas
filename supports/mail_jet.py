from mailjet_rest import Client
import base64
from api_framework.credential_config import *


def sent_mail(to, pdf_name, subject):
    with open("test.pdf", "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')

    api_key = API_KEY
    api_secret = API_SECRET
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "covipssupport@livnsense.com",
                    "Name": "SUSHANT"
                },
                "To": [
                    {
                        "Email": to,
                        "Name": "USER"
                    }
                ],
                "Subject": subject,
                "TextPart": "Greetings from COVIPS!",
                "HTMLPart": "<h3>TICKET INFO </h3><br />PDF ATTACHED TO THIS MAIL PLEASE VIEW",
                "Attachments": [
                    {
                        "ContentType": "application/pdf",
                        "Filename": pdf_name,
                        "Base64Content": encoded_string
                    }
                ]
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def sent_password_reset_mail(to, subject, body):
    api_key = "0099e5b8efdbbda46075f897bf6dea4e"
    api_secret = "dc3221294f6178b74ea315e93d7088ba"
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "covipssupport@livnsense.com",
                    "Name": "LivNSense Team"
                },
                "To": [
                    {
                        "Email": to,
                        "Name": "USER"
                    }
                ],
                "Subject": subject,
                "TextPart": "Greetings from COVIPS!",
                "HTMLPart": "<h3>CLICK LINK TO RESET PASSWORD </h3><br /> {body} ".format(body=body)
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def task_allocation_mail(to, subject, body):
    api_key = API_KEY
    api_secret = API_SECRET
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "covipssupport@livnsense.com",
                    "Name": "LivNSense Team"
                },
                "To": [
                    {
                        "Email": to,
                        "Name": "USER"
                    }
                ],
                "Subject": subject,
                "TextPart": "TASK ALLOCATION",
                "HTMLPart": "<h3>NEED HELP </h3><br /> {body} ".format(body=body)
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def sent_assessment_mail(to, subject, body):
    api_key = API_KEY
    api_secret = API_SECRET
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "covipssupport@livnsense.com",
                    "Name": "LivNSense Team"
                },
                "To": [
                    {
                        "Email": to,
                        "Name": "USER"
                    }
                ],
                "Subject": subject,
                "TextPart": "COVID ALERT ASSESSMENT",
                "HTMLPart": "<h3>CLICK LINK TO GO INTO ASSESSMENT </h3><br /> {body} ".format(body=body)
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

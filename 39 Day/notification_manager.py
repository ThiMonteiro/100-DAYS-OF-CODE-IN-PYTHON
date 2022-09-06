from twilio.rest import Client

TWILIO_SID = " " # SID da sua conta
TWILIO_AUTH_TOKEN = " " # Seu token auth
TWILIO_VIRTUAL_NUMBER = " " # Seu número virtual
TWILIO_VERIFIED_NUMBER = " " # Seu número verificado


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

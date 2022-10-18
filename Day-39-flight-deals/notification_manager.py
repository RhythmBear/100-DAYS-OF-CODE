from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_text(self, message):

        MY_ACCOUNT_SID = "ACc0d617f3c2fe7c20630cc447683652b9"
        MY_AUTH_TOKEN = "88afaea9937dbe15930b16658f2a4a26"
        MY_TWILIO_PHONE = "+17073833614"
        MY_PHONE_NUMBER = "+2347080304532"

        client = Client(MY_ACCOUNT_SID, MY_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=MY_TWILIO_PHONE,
            to=MY_PHONE_NUMBER
        )

        print(message.status)

    pass
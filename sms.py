
# Download the helper library from https://www.twilio.com/docs/python/install
import os

from twilio.rest import Client

class Twilio():
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    def send_message(self, phone, market, start_datetime, end_datetime):
        message = client.messages \
                        .create(
                             body="Great news! " + str(market) + " is open from " + str(start_datetime) + " to " + str(end_datetime) + ".",
                             from_='+14159172945',
                             to=str(phone)
                         )

        print(message.sid)
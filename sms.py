
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from sms.rest import Client

class Twilio():
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['AC750faaed82fa5ef391332e2742b446c9']
    auth_token = os.environ['ac6ca0e5e9bc994b769f8f5edd403503']
    client = Client(account_sid, auth_token)

    def send_message(self, client_phone, market, time_start, time_end):
        message = client.messages \
                        .create(
                             body="Great news! " + str(market) + " is open from " + str(time_start) + " to " + str(time_end) + ".",
                             from_='+14159172945',
                             to=str(client_phone)
                         )

        print(message.sid)
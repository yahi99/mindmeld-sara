import os
from twilio.rest import Client

client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your personal WhatsApp Messaging number
to_whatsapp_number='whatsapp:+919977216617'

message = client.messages.create(body='its your twitter profile right, Yash?',
                       media_url='https://pbs.twimg.com/profile_images/1274045729170808833/2vT239Ac_400x400.jpg',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

print(message.sid)
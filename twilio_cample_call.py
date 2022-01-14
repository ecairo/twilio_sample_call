# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

to_phone = os.environ['TO_PHONE']
from_phone = os.environ['FROM_PHONE']

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say voice="alice" language="es-ES" loop="2">Hola, te llamo porque tienes una alerta. Revisa el correo.</Say></Response>',
                        to=to_phone,
                        from_=from_phone
                    )

print(call.sid)
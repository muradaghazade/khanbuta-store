from http import client
from twilio.rest import Client

sid = 'AC7517889a27aa7701f5bd0ecfb5df82c7'
token = 'eeffd77bdf049c33df57e28ce75cbe9c'

client = Client(sid, token)


def send_sms(code, number):
    try:
        message = client.messages.create(
            body=f'Your verification code is {code}',
            from_='+19036183687',
            to=f'{number}'
        )
        print(message.sid)
    except:
        print('Please verify number, you are on free trial :)')


# send_sms('885522', '+994552405017')
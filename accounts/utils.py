from http import client
from twilio.rest import Client

sid = 'AC7517889a27aa7701f5bd0ecfb5df82c7'
token = 'dcd1023e9e3e7a30406015bcc48b1348'

client = Client(sid, token)


def send_sms(code, number):
    try:
        message = client.messages.create(
            body=f'Sizin təstiq kodunuz {code}',
            from_='IPEKYOLU',
            to=f'{number}'
        )
        print(message.sid)
    except:
        print('Please verify number, you are on free trial :)')


# send_sms('885522', '+994552405017')
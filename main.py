# 1 twilio client setup
# 2 user input
# 3 scheduling logic
# 4 send message
from unicodedata import name

from twilio.rest import Client
from datetime import datetime, timedelta
import time


# Twilio credentials
account_sid = 'your account sid'
auth_token='your auth token'

clent=Client(account_sid, auth_token)
def send_whatsapp_message(recipient_number,message_body):
    try:
        message=clent.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'message sent sucessfully MESSAGE SID: {message.sid} ')
    except Exception as e:
        print("an error occured:")


name=input("enter the recipient name=")
recipient_number=input("enter the recipient number with countary code=")
message_body=input("enter the message body=")
date_str=input("enter the data to send the message(YYYY-MM-DD): ")
time_str=input("enter the time to send the message(HH:MM): ")

schedule_datetime=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime=datetime.now()
time_diff=(schedule_datetime-current_datetime)
delay_seconds=time_diff.total_seconds()

if delay_seconds <=0:
    print("the scheduled time is in the past. please enter a future time.")
else:
    print(f'message scheduled to be sent to {name} at {schedule_datetime}')
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number,message_body)





    

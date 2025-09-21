from twilio.rest import Client
from datetime import datetime, timedelta
import time


account_sid = 'ACc84b6c99fae2287e02cc322cb32a67dc'
auth_token = 'ad5aa186ea51ddc942e2438c52f45545'


client = Client(account_sid, auth_token)


def send_message(recipent_number, message_body):
    try:
        message = Client.messages.create(
            from_= 'whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{recipent_number}'
        )
        print(f"Message sent to {recipent_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {recipent_number}: {e}")


name = input("Enter your name: ")
recipent_number = input("Enter the recipient's WhatsApp number (with country code): ")
message_body = input("enter the message you want to send to {name}: ")


date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")


scheduled_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()


time_difference = (scheduled_datetime - current_datetime)
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The scheduled time must be in the future.")
else:
    print(f"Message scheduled to be sent at {scheduled_datetime}. Waiting...")
    time.sleep(delay_seconds)
    send_message(recipent_number, message_body)
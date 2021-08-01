#gpiozero library
import gpiozero
#pause function from signal library
from signal import pause
#twilio library
from twilio.rest import Client
#import time stamp
import datetime

#twilio credentials
account_sid = "AC2aa0bc55508405e573786a2acd72bd63"
auth_token = "xxx"

#twilio login function
client = Client(account_sid, auth_token)


#when circuit is open
def float_down():
	dt = datetime.datetime.now()
    print("Water Low", dt)
    message = client.messages.create(
    to="+18018429047",
    from_="+14159961014",
    body="Cows are THIRSTY", dt)
    print(message.sid)

#when circuit is closed
def float_up():
	dt = datetime.datetime.now()
    print("Water Level OK", dt)

#Define pins switch (button) is connected to
button = gpiozero.Button(2)

#what happens when status of switch (button) changes
button.when_pressed = float_up

button.when_released = float_down

pause()

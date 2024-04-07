import time
from twilio.rest import Client

def send_sms(message):
    """Send SMS notification."""
    account_sid = 'AC3e7b43014fef891faec1a0c1fee1ade5'
    auth_token = '222531a6cedd7cf8e1a4f5b321c59cc9'
    sender_number = '+19095211963'  # Twilio phone number
    receiver_number = '+919354082061'  # Recipient's phone number

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Send SMS message
        message = client.messages.create(
            body=message,
            from_=sender_number,
            to=receiver_number
        )
        print("SMS notification sent successfully!")
    except Exception as e:
        print(f"Failed to send SMS notification: {e}")

def check_speed(initial_speed):
    """Continuously monitors car speed and sends a warning SMS if it drops suddenly.

    Args:
        initial_speed: The initial speed of the car in kilometers per hour (kmph).
    """

    current_speed = initial_speed
    time_t = 0

    while True:
        time_t += 1
        new_speed = float(input("Enter the current speed (kmph): "))

        # Check for sudden speed drop
        if new_speed < current_speed - 40:
            warning_message = "WARNING: Speed dropped suddenly by more than 40kmph!"
            print(warning_message)
            send_sms(warning_message)

        current_speed = new_speed

        # Simulate time passage (replace with actual speed monitoring logic)
        print(f"Time: {time_t} seconds, Speed: {current_speed} kmph")

# Get initial speed from user
initial_speed = float(input("Enter the initial speed of the car (kmph): "))

check_speed(initial_speed)

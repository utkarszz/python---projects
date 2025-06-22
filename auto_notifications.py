# ...existing code...
from plyer import notification
import time

while True:
    notification.notify(
        title="*** take a break ***",
        message="You have been working for a while. It's time to take a break!",
        timeout=10
    )
    time.sleep(3600)  # Waits for 1 hour before next notification
# ...existing code...


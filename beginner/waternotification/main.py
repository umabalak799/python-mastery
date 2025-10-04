import time
from plyer import notification

interval = 30 * 60

while True:
    notification.notify(
        title="Drink water",
        message="tiem to drink a glass of water and stay hydrated",
        timeout=10
    )
    time.sleep(interval)
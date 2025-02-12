import datetime
import os
import time

target_year = 2025
target_month = 5
target_day = 22
target_hour = 20

def countdown(target_date):
    """Counts down the days, hours, minutes, and seconds until the target date."""

    while True:
        time_remaining = target_date - datetime.datetime.now()
        if time_remaining.total_seconds() <= 0:
            print("Countdown complete!")
            break

        days = time_remaining.days
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return(f"{z(days)}:{z(hours)}:{z(minutes)}:{z(seconds)}")

def z(number):
    return str(number).zfill(2)

def countdown_cli(target_date):

    running = True
    while running:
        os.system("clear")
        time_remaining = countdown(target_date)
        print(time_remaining)
        time.sleep(1)

if __name__ == "__main__":
    target_date = datetime.datetime(target_year, target_month, target_day, target_hour)
    countdown_cli(target_date)
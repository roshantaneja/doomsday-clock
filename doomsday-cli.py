import datetime
import os
import time
from PIL import Image, ImageDraw, ImageFont

target_year = 2025
target_month = 5
target_day = 22
target_hour = 20

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
        countdown_ascii(target_date)
        time.sleep(1)



def countdown_ascii(target_date):
    #generate ascii art text of the target date number
    time_remaining = countdown(target_date)
    font = ImageFont.truetype('digital-7 (mono).ttf', 40) #load the font
    size = font.getbbox(time_remaining)[2:]  #calc the size of text in pixels
    image = Image.new('1', size, 1)  #create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), time_remaining, font=font) #render the text to the bitmap
    for rownum in range(size[1]): 
    #scan the bitmap:
    # print ' ' for black pixel and 
    # print '#' for white one
        line = []
        for colnum in range(size[0]):
            if image.getpixel((colnum, rownum)): line.append(' '),
            else: line.append(bcolors.FAIL + '#' + bcolors.ENDC),
        print(''.join(line))





if __name__ == "__main__":
    target_date = datetime.datetime(target_year, target_month, target_day, target_hour)
    countdown_cli(target_date)
    #countdown_ascii(target_date)
import datetime
import pygame

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

        return(f"{days}:{hours}:{minutes}:{seconds}")

def countdown_gui(target_date):

    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Countdown to Doomsday")

    font = pygame.font.Font(None, 200)
    text = font.render("", True, (255, 255, 255))
    text_rect = text.get_rect(center=(700, 700))

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        time_remaining = countdown(target_date)
        title = font.render("Countdown to Homecomp", True, (255, 255, 255))
        text = font.render(time_remaining, True, (255, 75, 75))
        screen.blit(text, text_rect)
        screen.blit(title, (200, 100))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    target_year = 2024
    target_month = 11
    target_day = 16
    target_hour = 10

    target_date = datetime.datetime(target_year, target_month, target_day, target_hour)
    countdown_gui(target_date)
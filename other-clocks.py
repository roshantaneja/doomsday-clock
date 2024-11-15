import datetime
import pygame

day_siva_scored = datetime.datetime(2023, 12, 10, 0)
day_aarav_left = datetime.datetime(2024, 9, 7, 0)


def days_since(target_date):

    time_since = datetime.datetime.now() - target_date
    return time_since.days

def days_until(target_date):

    time_until = target_date - datetime.datetime.now()
    return time_until.days

def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # First, split the text into words
    words = text.split()

    # Now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # Get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # Add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # Now we've split our text into lines that fit into the width, actually
    # render them

    # We'll render each line below the last, so we need to keep track of
    # the cumulative height of the lines we've rendered so far
    y_offset = 0
    line_spacing = font.get_linesize()  # Use the font's line height

    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        # Increment y_offset by line height for the next line
        y_offset += line_spacing  # Add space for the next line

def countdown_gui(siva, aarav):
        pygame.init()
        info = pygame.display.Info()
        # screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
        WIDTH = info.current_w
        HEIGHT = info.current_h
 

        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Countdown to Doomsday")
    
        font = pygame.font.Font("digital-7 (mono).ttf", HEIGHT//4)
        caption_font = pygame.font.Font("F25_Bank_Printer.ttf", HEIGHT//20)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            time_since_siva = days_since(siva)
            time_since_aarav = days_since(aarav)
        
            screen.fill((0, 0, 0))
            renderTextCenteredAt("Days since Siva scored for the wrong team", caption_font, (255, 255, 255), WIDTH//2 - WIDTH//4, HEIGHT//6, screen, WIDTH//4)
            renderTextCenteredAt(str(time_since_siva), font, (255, 75, 75), WIDTH//2 + WIDTH//5, HEIGHT//6, screen, WIDTH)


            renderTextCenteredAt("Days since Aarav left", caption_font, (255, 255, 255), WIDTH//2 - WIDTH//4, HEIGHT//2, screen, WIDTH//4)
            renderTextCenteredAt(str(time_since_aarav), font, (255, 75, 75), WIDTH//2 + WIDTH//5, HEIGHT//2 - HEIGHT//20, screen, WIDTH)



            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    countdown_gui(day_siva_scored, day_aarav_left)

import pygame
from sys import exit


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_FPS = 500


pygame.init() #Start pygame
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Rozmiar okna
pygame.display.set_caption('Paint') #Nazwa okna
clock = pygame.time.Clock() #Zegar
lines_count = 0


def quit_game():
    pygame.quit()
    exit()

def screen_clear():
    screen.fill('Black')

def handle_event():
    global lines_count
    global secret
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quit_game() #Kończy program na zamknięcie okna
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: quit_game() #Kończy program na ESC
            elif event.key == pygame.K_r: screen_clear()
            elif event.key == pygame.K_1: lines_count = 1
            elif event.key == pygame.K_2: lines_count = 2
            elif event.key == pygame.K_3: lines_count = 3
            elif event.key == pygame.K_4: lines_count = 4
            elif event.key == pygame.K_0: lines_count = 0


def draw_lines(lines):
    if lines == 0:
        pass
    if lines >= 1:
        pygame.draw.line(screen,'Red',(0,0),(pygame.mouse.get_pos()))
    if lines >= 2:
        pygame.draw.line(screen,'Blue',(SCREEN_WIDTH,0),(pygame.mouse.get_pos()))
    if lines >= 3:
        pygame.draw.line(screen,'Green',(SCREEN_WIDTH,SCREEN_HEIGHT),(pygame.mouse.get_pos()))
    if lines >= 4:
        pygame.draw.line(screen,'Yellow',(0,SCREEN_HEIGHT),(pygame.mouse.get_pos()))




while True: #Game loop
    handle_event()

    draw_lines(lines_count)

    pygame.display.update() #Rysuje klatkę
    clock.tick(MAX_FPS) #Max FPS

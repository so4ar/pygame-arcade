import pygame
from sys import exit


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_FPS = 60
PLAYER1_BASE_SPEED = 10
PLAYER1_SIZE = 5
ROUND_TIME = 60

PLAYER2_BASE_SPEED = 15
PLAYER2_SIZE = 3


pygame.init() #Start pygame
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Rozmiar okna
pygame.display.set_caption('My Game') #Nazwa okna
clock = pygame.time.Clock() #Zegar
score = 0
timer = ROUND_TIME
last_time = 0
player1_speed = PLAYER1_BASE_SPEED + score/50
player2_speed = PLAYER1_BASE_SPEED + 5

player1_pos_x, player1_pos_y = 100, 100
player2_pos_x, player2_pos_y = 500, 100

player1_img = pygame.image.load('niggerX1.png').convert_alpha()
player1_img = pygame.transform.scale_by(player1_img,PLAYER1_SIZE)
player1_rect = player1_img.get_rect(center=(player1_pos_x,player1_pos_y))

player2_img = pygame.image.load('niggerX1.png').convert_alpha()
player2_img = pygame.transform.scale_by(player2_img,PLAYER2_SIZE)
player2_rect = player2_img.get_rect(center=(player2_pos_x,player2_pos_y))

score_font = pygame.font.Font(None, 450)
score_surf = score_font.render(f"{score}", (225,225,225), "Black")
score_rect = score_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

timer_font = pygame.font.Font(None, 100)
timer_surf = timer_font.render(f"{timer}", (225,225,225), "Black")
timer_rect = timer_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/6))


def quit_game():
    pygame.quit()
    exit()

def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quit_game() #Kończy program na zamknięcie okna
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: quit_game() #Kończy program na ESC
            if event.key == pygame.K_p: pause()


def update():
    global player1_rect, player2_rect, score_rect, timer_rect, score_surf, player1_speed
    player2_rect = player2_img.get_rect(center=(player2_pos_x,player2_pos_y))
    player1_rect = player1_img.get_rect(center=(player1_pos_x,player1_pos_y))
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    timer_rect = timer_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/6))
    score_surf = score_font.render(f"{score}", (225,225,225), "Black")
    player1_speed = PLAYER1_BASE_SPEED + score/50



def hit():
    global score,score_surf,score_rect
    if player1_rect.colliderect(player2_rect):
        print(f"HIT: {score}")
        score += 1
        score_surf = score_font.render(f"{score}", (225,225,225), "Black")

def sec():
    global timer, timer_surf
    if timer <= 0:
        pause()
    else:
        timer -= 1
        timer_surf = timer_font.render(f"{timer}", (225,225,225), "Black")

def pause():
    global timer, score
    print("STOP")
    while True:
        print("STOP")

        screen.fill('Grey') #Czyści ekran
        screen.blit(score_surf,score_rect)
        screen.blit(timer_surf,timer_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit_game() #Kończy program na zamknięcie okna
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    timer = ROUND_TIME
                    score = 0
                    return
        
        pygame.display.update() #Rysuje klatkę
        clock.tick(MAX_FPS) #Max FPS

while True: #Game loop
    handle_event()
    update()

    now = pygame.time.get_ticks()
    if now - last_time >= 1000:
        last_time = now
        sec()

    if player1_pos_x < 0:player1_pos_x = SCREEN_WIDTH - 1
    if player1_pos_x > SCREEN_WIDTH:player1_pos_x = 1
    if player1_pos_y < 0:player1_pos_y = SCREEN_HEIGHT - 1
    if player1_pos_y > SCREEN_HEIGHT:player1_pos_y = 1

    if player2_pos_x < 0:player2_pos_x = SCREEN_WIDTH - 1
    if player2_pos_x > SCREEN_WIDTH:player2_pos_x = 1
    if player2_pos_y < 0:player2_pos_y = SCREEN_HEIGHT - 1
    if player2_pos_y > SCREEN_HEIGHT:player2_pos_y = 1

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]: player1_pos_y -= player1_speed
    if keys[pygame.K_s]: player1_pos_y += player1_speed
    if keys[pygame.K_a]: player1_pos_x -= player1_speed
    if keys[pygame.K_d]: player1_pos_x += player1_speed
    if keys[pygame.K_LSHIFT]: hit()


    if keys[pygame.K_UP]: player2_pos_y -= player2_speed
    if keys[pygame.K_DOWN]: player2_pos_y += player2_speed
    if keys[pygame.K_LEFT]: player2_pos_x -= player2_speed
    if keys[pygame.K_RIGHT]: player2_pos_x += player2_speed

    screen.fill('Grey') #Czyści ekran
    screen.blit(score_surf,score_rect)
    screen.blit(timer_surf,timer_rect)

    screen.blit(player1_img,player1_rect)
    screen.blit(player2_img,player2_rect)

    pygame.display.update() #Rysuje klatkę
    clock.tick(MAX_FPS) #Max FPS
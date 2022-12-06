import pygame
#inititlize the pygame
pygame.init()
#creating the game clocl
clock = pygame.time.Clock()
#create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load("BackgroundConcept.png")

#Title and Icon
pygame.display.set_caption("SoundWaver")
icon = pygame.image.load('ICON3.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("SoundWaveGuy.png")
UpscaledplayerImg = pygame.transform.scale(playerImg, (128,128))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
playerCollBox = UpscaledplayerImg.get_rect()



def player(x,y):
    screen.blit(UpscaledplayerImg,(playerX - 64,playerY - 64))
    pygame.draw.rect(screen, (255, 0, 0), playerCollBox, 2)

#Player Gun
playerGunImg = pygame.image.load("SoundwaveGunRecale.png")
UpscaledplayerGun = pygame.transform.scale(playerGunImg, (128,128))
playerGunX = 440
playerGunY = 515
playerGunX_change = 0
playerGunY_change = 0
playerGravity = 0


def playerGun(x,y):
    screen.blit(UpscaledplayerGun,(playerGunX - 64,playerGunY - 64))


#GAME LOOP
running = True
while running:
    #RGB (colors)
    screen.fill((0, 0, 0))
    #adding Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # PLAYER MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.5
            if event.key == pygame.K_UP:
                playerGravity = -10
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
    playerGravity += 1
    playerX += playerX_change
    playerY += playerGravity
    playerGunX += playerX_change
    playerGunY += playerY_change
    # OUT OF BOUNDS
    if playerX <= 32:
        playerX = 32
    elif playerX >= 768:
        playerX = 768

    if playerY <= 10:
        playerY = 10
    elif playerY >= 530:
        playerY = 530

    # DRAWING INTO GAME
    player(playerX, playerY)
    playerGun(playerGunX,playerGunY)

    pygame.display.update()
    clock.tick(60)

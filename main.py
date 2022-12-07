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

# Crosshair
CrosshairImg = Sprite(32, 32, "Crosshair.png")
CrosshairImg.scale_image(32, 32)

# Player
player = Sprite(370, 480, "SoundWaveGuy.png")
player.scale_image(128, 128)
player.toggle_hitbox(True)
player.img.get_rect().w = 78  # TODO fix this

# Player Gun
gun = Sprite(445, 545, "SoundwaveGunRecale.png")
gun.scale_image(128, 128)

# Player Beam




def moveSprite(sprite):
    screen.blit(sprite.img, (sprite.x - 64, sprite.y - 64))

    if sprite.show_hitbox:
        sprite.display_hitbox(screen)

    # Gun Sprite Box
    pygame.draw.polygon(screen, (0, 232, 46),
                        [[200, 300], [100, 400],
                         [100, 200]])
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Drawing CrossHair
    pygame.mouse.set_visible(False)
    screen.blit(CrosshairImg.img, (mouse_x - 32, mouse_y - 32))

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
                x = 0
    y += 1  # idk

    player.x += x
    player.y += y
    gun.x += x
    gun.y += y

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

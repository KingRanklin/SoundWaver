import pygame


from Sprite import Sprite


# Initialize the pygame
pygame.init()
# Creating the game clock
clock = pygame.time.Clock()
# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("NewBackground.png")

# Title and Icon
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

#Jump sounds works
jumpSound = pygame.mixer.Sound("JumpSound.wav")


# Player Gun
gun = Sprite(445, 545, "SoundwaveGunRecale.png")
gun.scale_image(128, 128)

# Player Beam
gunBeam = Sprite(500,500, "GunBeam.png")
gunBeam.scale_image(128,128)

def play_audio():

    file = "SoundWaverSongTest2.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.03)

def moveSprite(sprite):
    screen.blit(sprite.img, (sprite.x - 64, sprite.y - 64))

    if sprite.show_hitbox:
        sprite.display_hitbox(screen)




# GAME LOOP
running = True
x = y = 0
while running:
    # RGB (colors)
    screen.fill((0, 0, 0))
    # adding Background image
    screen.blit(background, (0, 0))
    #Music doent work unlock holding the top bar TODO
    play_audio()






    #Drawing the crosshair
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    screen.blit(CrosshairImg.img, (mouse_x - 32, mouse_y - 32))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # PLAYER MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -3.5
            if event.key == pygame.K_RIGHT:
                x = 3.5

            if event.key == pygame.K_UP:
                y = -15
                jumpSound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x = 0

        # Making Beam appear if clicking mouse AND MOVING mouse TODO FIX THIS

        if pygame.mouse.get_pressed() == (1, 0, 0):
                screen.blit(gunBeam.img, (gun.x - 40, gun.y - 160 ))



    y += 1  # idk  ## Is this gravity?

    # What does this do
    player.x += x
    player.y += y
    gun.x += x
    gun.y += y
    #gunBeam.x += x
    #gunBeam.y += y

    # OUT OF BOUNDS
    if player.x <= 32:
        gun.x = 32
        player.x = 32
    elif player.x >= 768:
        player.x = 768
        gun.x = 768

    if player.y <= 10:
        player.y = 10
        gun.y = 8
    elif player.y >= 530:
        player.y = 530
        gun.y = 580

    # DRAWING INTO GAME
    moveSprite(player)
    moveSprite(gun)

    pygame.display.update()
    clock.tick(60)

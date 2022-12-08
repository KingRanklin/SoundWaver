import pygame
#MAJOR TODO LIST
# Fix Background Music - billy fix this
# Fix GunBeam with Mouse Press - please fix this
# Add collision - how do we start?
# Add tiles?? Gonne be reworking game to be tile based.
# Need to set up world class and tile class


from Sprite import Sprite


# Initialize the pygame
pygame.init()
# Creating the game clock
clock = pygame.time.Clock()
# Create the screen


#define game variables
screen_width = 1000
screen_height = 1000

tile_size = 50

screen = pygame.display.set_mode((screen_width, screen_height))


#Loading Images
TileBG = pygame.image.load("TileBackground.png")

# Title and Icon
pygame.display.set_caption("SoundWaver")
icon = pygame.image.load('ICON3.png')
pygame.display.set_icon(icon)

# Crosshair
CrosshairImg = Sprite(32, 32, "Crosshair.png")
CrosshairImg.scale_image(32, 32)

# Player
player = Sprite(370, 480, "SoundWaveGuy.png")
player.scale_image(100, 150)
player.toggle_hitbox(True)
player.img.get_rect().w = 78  # TODO fix this

#Jump sounds works
jumpSound = pygame.mixer.Sound("JumpSound.wav")


# Player Gun
gun = Sprite(445, 545, "SoundwaveGunRecale.png")
gun.scale_image(100, 100)

# Player Beam
gunBeam = Sprite(500,500, "GunBeam.png")
gunBeam.scale_image(128,128)

def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load("Dirt.png")
        grass_img = pygame.image.load("GrassyDirt.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

world = World(world_data)

def play_audio():

    file = "SoundWaverSongTest2.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.03)

def moveSprite(sprite):
    screen.blit(sprite.img, (sprite.rect))  #(100, screen_height - 200))

    if sprite.show_hitbox:
        sprite.display_hitbox(screen)




# GAME LOOP
running = True
x = y = 0
gravity = 0

while running:
    # RGB (colors)
    screen.fill((0, 0, 0))
    # adding Background image
    screen.blit(TileBG, (0, 0))
    world.draw()
    draw_grid()
    #Music doent work unlock holding the top bar TODO FIX
    play_audio()






    #Drawing the crosshair
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    screen.blit(CrosshairImg.img, (mouse_x - 32, mouse_y - 32))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # PLAYER MOVEMENT
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -3.5
            if event.key == pygame.K_RIGHT:
                x = 3.5

            if event.key == pygame.K_UP:
                y = -15
                jumpSound.play()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x = 0

        # Making Beam appear if clicking mouse AND MOVING mouse TODO FIX THIS
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                screen.blit(gunBeam.img, (gun.x - 40, gun.y - 160 ))

    # idk  ## Is this gravity?
    gravity += 1
    if gravity > 10:
            gravity = 10
    y += gravity

    # What does this do. Updates player cordinates?
    player.rect.x += x
    player.rect.y += y
    #gun.x += x
    #gun.y += y
    #gunBeam.x += x
    #gunBeam.y += y

    # OUT OF BOUNDS
    if player.rect.bottom > screen_height:
        player.rect.bottom = screen_height
        player.y = 0











    #if player.x <= 32:
        #gun.x = 32
        #player.x = 32
    #elif player.x >= 768:
        #player.x = 768
        #gun.x = 768

    #if player.y <= 10:
        #player.y = 10
        #gun.y = 8
    #elif player.y >= 530:
        #player.y = 530
        #gun.y = 580

    # DRAWING INTO GAME
    moveSprite(player)
    #moveSprite(gun)

    pygame.display.update()
    clock.tick(60)

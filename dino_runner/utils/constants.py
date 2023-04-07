import pygame
import os
import pygame.mixer 
pygame.mixer.init()
# Global Constants


TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 45


IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUND_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))


RUNNING_FLASH = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunFlash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunFlash2.png")),
]
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_WINGS = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump2.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),   
]

DUCKING_HORN = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck22.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck33.png")),  

]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

ZOMBIE = [
    pygame.image.load(os.path.join(IMG_DIR, "Zombies/zombie1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Zombies/zombie3.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
FISH = pygame.image.load(os.path.join(IMG_DIR, 'other/fish.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
ARC =  pygame.image.load(os.path.join(IMG_DIR, 'Other/arc.png'))

SMALL = pygame.image.load(os.path.join(IMG_DIR, 'Other/small.png'))
SMALL_0 = pygame.image.load(os.path.join(IMG_DIR, 'Other/small0.png'))
TITLE_IMG = pygame.image.load(os.path.join(IMG_DIR, 'Other/tittle.png'))

MY_SUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/MySun.png'))
MY_CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/MyCloud.png'))

KIRBY1 = [
    pygame.image.load(os.path.join(IMG_DIR, 'Kirby/kirby2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Kirby/kirby22.png'))

]
KIRBY = pygame.image.load(os.path.join(IMG_DIR, 'Kirby/kirby.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEARTT = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

OST_MENU =  pygame.mixer.Sound(os.path.join(SOUND_DIR,'sounds/OST_Start_Menu.mp3'))
OST_MENU.set_volume(0.1)

OST_GAME = pygame.mixer.Sound(os.path.join(SOUND_DIR,'sounds/OST_Game.mp3'))
OST_GAME.set_volume(0.5)


HEART_TYPE = "heart"

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"


FONT_STYLE = 'chalkduster.ttf'
FONT_STYLE_2 = 'PressStart2P.ttf'


COLORS = {
    'black' : (0,0,0),
    'white' : (255, 255, 255),
    'blue' : (0, 0, 255),
    'silver': (192, 192, 192),
    'purple': 	(128, 0, 128),
    'cyan': (115, 180, 210)
}

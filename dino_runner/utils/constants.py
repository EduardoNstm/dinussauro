import pygame
import os
pygame.init()

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

# Dino
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun2.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield2.png")),
]
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuck2.png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield2.png")),
]
DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer2.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpShield.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png")
)

# Obstacles
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

# Doodads
CLOUD = pygame.image.load(os.path.join(IMG_DIR, "Other/Cloud.png"))

# Power ups
SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/Shield.png"))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Hammer.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

BANANA_IMPORT = pygame.image.load(os.path.join(IMG_DIR, "Other/banana_jump.png"))
BANANA_IMPORT_2 = pygame.image.load(os.path.join(IMG_DIR, "Other/banana_jum_2.png"))

novo_tamanho = (120, 140)
BANANA = [ 
    pygame.transform.scale(BANANA_IMPORT, novo_tamanho),
    pygame.transform.scale(BANANA_IMPORT_2, novo_tamanho)
    ]
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
pygame.mixer.music.set_volume(0.09)
SOUND_HACK = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/mensagem.wav"))
SOUND_JUMP = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/pulo_1.wav"))
SOUND_JUMP.set_volume(0.06)
SOUND_MENU = pygame.mixer.music.load(os.path.join(IMG_DIR, "Sound/dino_senpai.mp3"))
SOUND_MENU_START = pygame.mixer.music
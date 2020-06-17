"""
Module for managing tiles.
"""
import pygame

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

SHADOW = (128,64,64,55)
LOADER_R = (64,64,60,80)
LOADER_U = (0,0,62,64)
RED_PRESS = (128,320,64,64) 
PLAIN_BLOCK = (384,64,64,64)
BLUE_BUTTON = (128,0,64,64)
HAZ_TOP_TOP = (384,0,64,64)
HAZ_TOP_R = (448,0,63,64)
HAZ_MID_R = (448,64,63,64)
HAZ_BOT_R = (448,128,63,64)
HAZ_BOT = (384,128,64,64)
HAZ_BOT_L = (320,128,64,64)
HAZ_MID_L = (320,64,64,64)
HAZ_TOP_L = (320,0,64,64)
HAZ_BAR_TB = (256,128,64,64)
HAZ_CORNER_TL = (576,64,64,64)
HAZ_CORNER_TLBL = (576,128,64,64)
HAZ_CORNER_TRBR = (704,128,64,64)
# subtract 46 more for the y
BOX_BLANK = (0,149,64,110)
BOX_RED_SCREEN = (64,159,64,97)
BOX_BEHIND = (0,160,64,64)
# Red Door
RED_DOOR = (128,256,64,64)

food = (0,0,28,27)


class Block(pygame.sprite.Sprite):
    """ A Block from a sprite sheet """

    def __init__(self,sprite_sheet_data):
        """ Block constructor. Assumes the constant above are passed. """
        super().__init__()

        # sprite_sheet = SpriteSheet("assets/scifitiles-sheet.png")
        sprite_sheet = SpriteSheet("assets\scifitiles_resizedF.png")
        # Grab the image 
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class Food(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        """ Block constructor. Assumes the constant above are passed. """
        super().__init__()

        self.player = None
        self.level = None

        food_sprite_sheet = SpriteSheet("assets\golden.png")
        # Grab the image
        self.image = food_sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

    def update(self):
        """ Check if player hits apple """

        collect = False
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)

        if hit:
            collect = True


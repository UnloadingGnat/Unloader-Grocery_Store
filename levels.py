import pygame

import constants
import tiles


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
    def __init__(self,player):
        """ Constructor """

        # Lists of sprites used in all levels
        self.block_list = None
    
        # Background image = None
        self.backround = None

        self.block_list = pygame.sprite.Group()
        self.player = player
        

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.block_list.update()


    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(constants.DARK_BLUE)

        # Draw all the sprite lists that we have
        self.block_list.draw(screen)

# Create the map for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self,player):

        Level.__init__(self, player)
        # Array with type of tile, and x, y location of the platform.
        # Every block in the map
        level = [ [tiles.HAZ_BAR_TB,400,300],
                  [tiles.HAZ_CORNER_TLBL,464,300],
                  [tiles.HAZ_MID_L,464,236],
                  [tiles.SHADOW,400,364],
                  [tiles.SHADOW,464,428],
                  [tiles.SHADOW, 528, 428],
                  [tiles.SHADOW, 592, 428],
                  [tiles.HAZ_TOP_L, 464,172],
                  [tiles.HAZ_TOP_TOP,528,172],
                  [tiles.PLAIN_BLOCK,528,236],
                  [tiles.HAZ_TOP_R,592,172],
                  [tiles.HAZ_BOT_L,464,364],
                  [tiles.PLAIN_BLOCK,528,300],
                  [tiles.HAZ_BOT,528,364],
                  [tiles.HAZ_BOT_R,592,364],
                  [tiles.HAZ_MID_R,592,300],
                  [tiles.HAZ_CORNER_TRBR,592,236],
                  [tiles.LOADER_R,656,236],
                  [tiles.HAZ_CORNER_TRBR,336,300],
                  [tiles.HAZ_BOT_R,336,364],
                  [tiles.SHADOW,336,428],
                  [tiles.SHADOW,272,428],
                  [tiles.SHADOW,208,428],
                  [tiles.HAZ_BOT,272,364],
                  [tiles.HAZ_BOT_L,208,364],
                  [tiles.PLAIN_BLOCK,272,300],
                  [tiles.RED_PRESS,208,300],
                  [tiles.BOX_BLANK,144,259],
                  [tiles.BOX_BEHIND,144,207],
                  [tiles.RED_DOOR,208,236],
                  [tiles.LOADER_U,208,172],
                  [tiles.HAZ_TOP_R,336,236],
                  [tiles.BOX_RED_SCREEN,272,204],
                  [tiles.SHADOW, 144, 365],
                 ]


        food_list = [[tiles.food,620,250]]

        # Go through the array above and add tiles
        for mapTile in level:
            block = tiles.Block(mapTile[0])
            block.rect.x = mapTile[1]
            block.rect.y = mapTile[2]
            block.player = self.player
            self.block_list.add(block)


        # seperate array to add the Food object/tile
        apple = tiles.Food(food_list[0][0])
        apple.rect.x = food_list[0][1]
        apple.rect.y = food_list[0][2]
        apple.player = self.player
        apple.level = self
        self.block_list.add(apple)



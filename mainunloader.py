##
# Unloader: Grocery Store Edition
# @author Jaavin M
# @course ICS3UC
# @date 09/06/2020
#




import pygame

import constants
import levels

from player import Player

# add this later
# from player import Player



def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Unloader: Grocery Store Edition")

    # Create the user's player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01())

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]


    active_sprite_list = pygame.sprite.Group()

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        
        current_level.update()


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

##
# Unloader: Grocery Store Edition
# @author Jaavin M
# @course ICS3UC
# @date 09/06/2020
# v 1.1

import pygame

import constants
import levels

from player import Player

# add this later
# from player import Player


def main():
    """ Main Program """
    pygame.init()
    pygame.mixer.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Unloader: Grocery Store Edition")

    # Create the user's player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))

    # Points
    # point = 0
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    player.rect.x = 400
    player.rect.y = 300
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    pygame.mixer.music.load('assets\\Initial D - Deja Vu.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    wall_sound = pygame.mixer.Sound("assets\\iump.ogg")

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
        # Update the player
        if player.play_sound:
            wall_sound.play()
            player.play_sound = False
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

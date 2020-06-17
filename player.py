"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants


from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []


        # What direction is the player facing?
        self.direction = "D"

        sprite_sheet = SpriteSheet("assets\sans.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0,158,33,42)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(34, 155, 33, 42)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(67, 157, 31, 43)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(100, 158, 33, 42)
        self.walking_frames_r.append(image)


        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 158, 33, 42)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(34, 155, 33, 42)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(67, 157, 31, 43)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(100, 158, 33, 42)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 158, 33, 42)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(34, 155, 33, 42)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(67, 157, 31, 43)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(100, 158, 33, 42)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Load all the upward facing images into a list
        image = sprite_sheet.get_image(0, 53, 34, 50)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(34, 158, 34, 42)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(68, 158, 32, 42)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(100, 158, 34, 42)
        self.walking_frames_r.append(image)

        # Load all the downward facing images into a list
        image = sprite_sheet.get_image(0, 0, 34, 51)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(34, 0, 34, 50)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(68, 0, 34, 50)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(102, 0, 34, 50)
        self.walking_frames_r.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_d[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """

        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "D":
            frame = (pos // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]




    # Player-controlled movement:

    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.change_x = 6
        self.direction = "D"

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.change_y = -6
        self.direction = "U"

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

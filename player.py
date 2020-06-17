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
        self.play_sound = False
        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []


        # What direction is the player facing?
        self.direction = "D"

        sprite_sheet = SpriteSheet("assets\Char2.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 158, 33,42)
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
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(34, 53, 34, 42)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(68, 53, 32, 42)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(100, 53, 34, 42)
        self.walking_frames_u.append(image)

        # Load all the downward facing images into a list
        image = sprite_sheet.get_image(0, 0, 34, 51)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(34, 0, 34, 50)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(68, 0, 34, 50)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(102, 0, 30, 50)
        self.walking_frames_d.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_d[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """

        # Move left/right
        if self.rect.x < 200:
            self.rect.x += 1
            self.play_sound = True
        elif self.rect.x > 628:
            self.rect.x -= 1
            self.play_sound = True
        else:
            self.rect.x += self.change_x
        # Move up/down
        if self.rect.y < 140:
            self.rect.y += 1
            self.play_sound = True
        elif self.rect.y > 380:
            self.rect.y -= 1
            self.play_sound = True
        else:
            self.rect.y += self.change_y
        pos = self.rect.x
        posud = self.rect.y
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "D":
            frame = (posud // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
        elif self.direction == "U":
            frame = (posud // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]


    # Player-controlled movement:

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0



    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.change_y = 6
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


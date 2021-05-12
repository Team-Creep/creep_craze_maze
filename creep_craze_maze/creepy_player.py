import pygame
from creep_craze_maze.wall import WeNeedAWallLetsMakeItDifferent, COLORS

class PlayerMcPlayFacePlayingPlay(pygame.sprite.Sprite):
    """ Allow the player to do things. """

    # Start you x and y positions. Like, be creative with the numbers, 0, 0 is used a lot. 

    where_does_x_move_to = 5
    where_does_y_move_to = 10

    def __init__(self, x, y):
        # Inits are widely used and important. 
        # AGAIN, X AND Y ARE INCLUDED IN THE RECT DOCUMENTATION
        # it is now 3:15 am. I am so tired and I have to get up at 8 to drive to NYC and tell people my Father in law is dying. 

        super().__init__()
        # look in the WeNeedAWallLetsMakeItDifferent class, for information on why we use this instead of a regular class. setup. 

        self.the_screen_or_something_like_that = pygame.Surface([30, 30])
        self.the_screen_or_something_like_that.fill(WHITE)


        # THERE IS NOTHING WE CAN DO ABOUT THESE VARIABLES.
        # This sets up our starting position, using the aforementioned docs. 
        self.rect = self.the_screen_or_something_like_that.get_rect()
        self.rect.y = y
        self.rect.x = x

    def player_go_zoom_zoom(self, x, y):
        # Need the x, y, ect. PART OF RECT< SEE DOCS
        self.where_does_x_move_to += x
        self.where_does_y_move_to += y

    def let_the_player_move(self, these_are_barriers_for_the_user_to_enjoy):
        """ Docstring just to tell you the player can move using this. """

        # player can move along the x axis.
        # It is now 330, and there is no end in sight. 
        self.rect.x += self.where_does_x_move_to

        # Lets find out if we are hitting a wall, that way there is resistance in the game
        # ON SPRITE AND SPRITECOLLIDE> these are part of pygame> there is no changing htis basic structure> none of this code is hard. it is what it is.
        is_the_player_intersecting_at_all = pygame.sprite.spritecollide(self, these_are_barriers_for_the_user_to_enjoy, False)
        for h in is_the_player_intersecting_at_all:

            # basic break down is you are setting the sides of the users sprite to the side of the barrier the user came up to. If these were cats, their tails would be fluffy to the max.
            # left and right are built is here
            # https://www.pygame.org/docs/ref/rect.html
            if self.where_does_y_move_to > 0:
                self.rect.bottom = h.rect.top
            else:
                self.rect.top = h.rect.bottom


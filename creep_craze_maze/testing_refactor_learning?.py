import pygame
 
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# PURPLE = (255, 0, 255)
 
 
# class Wall(pygame.sprite.Sprite):
#     """ class for the wall constuctions"""
 
#     def __init__(self, x, y, width, height, color):
 
#         # Call the parent's constructor, 
#         super().__init__()
 
#         # Make a BLUE wall, of the size specified in the parameters
#         self.the_screen_or_something_like_that = pygame.Surface([width, height])
#         self.the_screen_or_something_like_that.fill(color)
 
#         # Make our top-left corner the passed-in location.
#         self.rect = self.the_screen_or_something_like_that.get_rect()
#         self.rect.y = y
#         self.rect.x = x

# def thisisatest_code(x, y):
#     return (x + y)

 
 
class Player(pygame.sprite.Sprite):
    """ What is this Player?  speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough, blah blah"""
 
    # Set speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough vector
    where_does_x_move_to = 0
    where_does_y_move_to = 0
 
    # def __init__(self, x, y):
 
    #     # Call the parent's constructor
    #     super().__init__()
 
        # Set height, width
    #     self.the_screen_or_something_like_that = pygame.Surface([15, 15])
    #     self.the_screen_or_something_like_that.fill(WHITE)
 
    #     # Make our top-left corner the passed-in location.
    #     self.rect = self.the_screen_or_something_like_that.get_rect()
    #     self.rect.y = y
    #     self.rect.x = x
 
    # def speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(self, x, y):
    #     """ Control player speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough, keypress style """
    #     self.where_does_x_move_to += x
    #     self.where_does_y_move_to += y
 
    # def move(self, these_are_barriers_for_the_user_to_enjoy):
    #     """ move the player """
 
    #     # Move left/right
    #     self.rect.x += self.where_does_x_move_to
 
    #     # Did this update cause us to hit a wall?
    #     is_the_player_intersecting_at_all = pygame.sprite.spritecollide(self, these_are_barriers_for_the_user_to_enjoy, False)
    #     for h in is_the_player_intersecting_at_all:
    #         # If we are moving right, set our right side to the left side of
    #         # the item we hit
    #         if self.where_does_x_move_to > 0:
    #             self.rect.right = h.rect.left
    #         else:
    #             # Otherwise if we are moving left, do the opposite.
    #             self.rect.left = h.rect.right
 
    #     # Move up/down
    #     self.rect.y += self.where_does_y_move_to
 
    #     # Check and see if we hit anything
    #     hit = pygame.sprite.spritecollide(self, these_are_barriers_for_the_user_to_enjoy, False)
    #     for h in hit:
 
    #         # Reset our position based on the top/bottom of the object.
    #         if self.where_does_y_move_to > 0:
    #             self.rect.bottom = h.rect.top
    #         else:
    #             self.rect.top = h.rect.bottom
 
 
class play_space(object):
    """ Base class for all play_spaces. """
 
    # Each play_space has a list of these_are_barriers_for_the_user_to_enjoy, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ lists the lists of these_are_barriers_for_the_user_to_enjoy """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class play_space_one(play_space):
    """This creates all the these_are_barriers_for_the_user_to_enjoy in play_space 1"""
    def __init__(self):
        super().__init__()
        # Make the these_are_barriers_for_the_user_to_enjoy. (x_pos, y_pos, width, height)
 
        # This is a list of these_are_barriers_for_the_user_to_enjoy. Each is in the form [x, y, width, height]
        these_are_barriers_for_the_user_to_enjoy = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in these_are_barriers_for_the_user_to_enjoy:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class play_space_two(play_space):
    """This creates all the these_are_barriers_for_the_user_to_enjoy in play_space 2"""
    def __init__(self):
        super().__init__()
 
        these_are_barriers_for_the_user_to_enjoy = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]
 
        for item in these_are_barriers_for_the_user_to_enjoy:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class play_space_three(play_space):
    """This creates all the these_are_barriers_for_the_user_to_enjoy in play_space 3"""
    def __init__(self):
        super().__init__()
 
        these_are_barriers_for_the_user_to_enjoy = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]
 
        for item in these_are_barriers_for_the_user_to_enjoy:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)
 
 
def main():
    """ Call game to life """
 
    # Call this function so the Pygame library can initialize itsel
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 

    pygame.display.set_caption('Creep Craze Maze')
 
    # Create the player
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    play_spaces = []
 
    play_space = play_space_one()
    play_spaces.append(play_space)
 
    play_space = play_space_two()
    play_spaces.append(play_space)
 
    play_space = play_space_three()
    play_spaces.append(play_space)
 
    current_play_space_no = 0
    current_play_space = play_spaces[current_play_space_no]
 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done:
 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(5, 0)
                if event.key == pygame.K_UP:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(0, -5)
                if event.key == pygame.K_DOWN:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(0, 5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(-5, 0)
                if event.key == pygame.K_UP:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(0, 5)
                if event.key == pygame.K_DOWN:
                    player.speed_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough_of_the_users_sprite_bloody_hell_man_is_this_ever_good_enough(0, -5)
 
        # --- Game Logic ---
 
        player.move(current_play_space.wall_list)
 
        if player.rect.x < -15:
            if current_play_space_no == 0:
                current_play_space_no = 2
                current_play_space = play_spaces[current_play_space_no]
                player.rect.x = 790
            elif current_play_space_no == 2:
                current_play_space_no = 1
                current_play_space = play_spaces[current_play_space_no]
                player.rect.x = 790
            else:
                current_play_space_no = 0
                current_play_space = play_spaces[current_play_space_no]
                player.rect.x = 790
 
        if player.rect.x > 801:
            if current_play_space_no == 0:
                current_play_space_no = 1
                current_play_space = play_spaces[current_play_space_no]
                player.rect.x = 0
            elif current_play_space_no == 1:
                current_play_space_no = 2
                current_play_space = play_spaces[current_play_space_no]
                player.rect.x = 0
            else:
                current_play_space_no = 0
                current_play_space = play_spaces[current_play_space_no]
                player.rect.x = 0
 
        # --- Drawing ---
        screen.fill(BLACK)
 
        movingsprites.draw(screen)
        current_play_space.wall_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()

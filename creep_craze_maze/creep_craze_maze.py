import pygame
 
BLACK = (0, 0, 0)
WHITE = (232, 235, 237)
BLUE = (50, 107, 168)
GREEN = (50, 168, 82)
RED = (214, 41, 203)
DARKRED = (204, 0, 0)
PURPLE = (151, 50, 168)

class Wall(pygame.sprite.Sprite):
    """This is to construct a wall. Sets up what we need to create a landscape."""
    # initialize the construction. You need a self, you need axis of x and y, width, height and color get passed in.
    # rect is apart of the pygame library. Information on use can be found here 
    # https://www.pygame.org/docs/ref/rect.html
    def __init__(self, x, y, width, height, color):
        super().__init__()
        # found in the following docs, a super init allows us to set children/parent relationships between contructors. This allows us to pull and use the informatiton instead of passing variables around and pulling them in manually. it is more efficent.  
        # https://www.educative.io/edpresso/what-is-super-in-python

        # pygame allows you to set a variable for the surface
        # https://www.pygame.org/docs/ref/surface.html
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # choose a location to start. 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Player(pygame.sprite.Sprite):
    """ Allow the player to do things. """

    # Sets speed of x, y positions. x needs to be 0, y can be upped, but it's impossible to move after 4!
    where_does_x_move_to = 0
    where_does_y_move_to = 0

    def __init__(self, x, y):
        # Inits are widely used and important. 
        super().__init__()
        # look in the Wall class, for information on why we use this instead of a regular class. setup. 

        # self.image = pygame.Surface([20, 20])
        # self.image.fill(WHITE)
        self.image = pygame.image.load('assets/roger.png')
        self.hexx = pygame.image.load('assets/Hexx.png')
        self.vince = pygame.image.load('assets/vince.png')
        self.john = pygame.image.load('assets/big_john.png')

        # This sets up our starting position, using the aforementioned docs. 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def player_go_zoom_zoom(self, x, y):
        # Need the x, y, ect. PART OF RECT< SEE DOCS
        self.where_does_x_move_to += x
        self.where_does_y_move_to += y

    def let_the_player_move(self, walls):
        """ Docstring just to tell you the player can move using this. """

        # player can move along the x axis.
        self.rect.x += self.where_does_x_move_to

        # Lets find out if we are hitting a wall, that way there is resistance in the game
        is_the_player_intersecting_at_all = pygame.sprite.spritecollide(self, walls, False)
        for h in is_the_player_intersecting_at_all:

            # basic break down is you are setting the sides of the users sprite to the side of the barrier the user came up to. If these were cats, their tails would be fluffy to the max.
            # left and right are built is here
            # https://www.pygame.org/docs/ref/rect.html
            if self.where_does_y_move_to > 0:
                self.rect.bottom = h.rect.top
            else:
                self.rect.top = h.rect.bottom
 
    def move(self, walls):
        """ move the player """
 
        # Move left/right
        self.rect.x += self.where_does_x_move_to
 
        # Did this update cause us to hit a wall?
        is_the_player_intersecting_at_all = pygame.sprite.spritecollide(self, walls, False)
        for h in is_the_player_intersecting_at_all:
            if self.where_does_x_move_to > 0:
                self.rect.right = h.rect.left
            else:
                self.rect.left = h.rect.right
 
        # Move up/down
        self.rect.y += self.where_does_y_move_to
 
        # Did we hit?
        hit = pygame.sprite.spritecollide(self, walls, False)
        for h in hit:
 
            # Reset our player position based on position of object
            if self.where_does_y_move_to > 0:
                self.rect.bottom = h.rect.top
            else:
                self.rect.top = h.rect.bottom
 
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ lists the lists of walls """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room_one(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height, color)
        walls = [[0, 0, 20, 250, BLACK],
                 [0, 350, 20, 250, BLACK],
                 [780, 0, 20, 250, BLACK],
                 [780, 350, 20, 250, BLACK],
                 [20, 0, 760, 20, BLACK],
                 [20, 580, 760, 20, BLACK],
                 [210, 30, 20, 500, DARKRED],
                 [390, 70, 20, 500, DARKRED],
                 [590, 30, 20, 500, DARKRED],
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room_two(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, DARKRED],
                 [0, 350, 20, 250, DARKRED],
                 [780, 0, 20, 250, DARKRED],
                 [780, 350, 20, 250, DARKRED],
                 [20, 0, 760, 20, DARKRED],
                 [20, 580, 760, 20, DARKRED],
                 [190, 20, 20, 500, WHITE],
                 [590, 80, 20, 500, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room_three(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(90, 400, 110):
            for y in range(25, 225, 150):
                wall = Wall(x, y, 20, 200, DARKRED)
                self.wall_list.add(wall)

        for x in range(400, 700, 110):
            for y in range(225, 451, 150):
                wall = Wall(x, y, 20, 200, DARKRED)
                self.wall_list.add(wall)
 
        for x in range(150, 350, 100):
            wall = Wall(x, 400, 20, 600, WHITE)
            self.wall_list.add(wall)

        for x in range(445, 675, 112):
            wall = Wall(x, 40, 20, 300, WHITE)
            self.wall_list.add(wall)


class Room_four(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [100, 20, 20, 100, WHITE],
                 [100, 100, 100, 20, WHITE],
                 [200, 100, 20, 140, WHITE],
                 [200, 240, 50, 20, WHITE],
                #  [600, 80, 20, 100, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        self.bg = pygame.image.load('assets/bg3.png')
        self.logo = pygame.image.load('assets/cf_logo.png')
 
def main():
    """ Call game to life """
 
    # Call this function so the Pygame library can initialize itsel
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 

    pygame.display.set_caption('Creep Craze Maze')
 
    # Create the player
    player = Player(50, 300)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    rooms = []
 
    room = Room_one()
    rooms.append(room)
 
    room = Room_two()
    rooms.append(room)
 
    room = Room_three()
    rooms.append(room)

    room = Room_four()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()

    # timer
    ticks = pygame.time.get_ticks()
 
    done = False
 
    while not done:
        # countdown timer
        # seconds = (pygame.time.get_ticks() - ticks) / 1000
        # if seconds > 30:
        #     break
        # print(seconds)

        # key controls
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.player_go_zoom_zoom(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.player_go_zoom_zoom(5, 0)
                if event.key == pygame.K_UP:
                    player.player_go_zoom_zoom(0, -5)
                if event.key == pygame.K_DOWN:
                    player.player_go_zoom_zoom(0, 5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.player_go_zoom_zoom(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.player_go_zoom_zoom(-5, 0)
                if event.key == pygame.K_UP:
                    player.player_go_zoom_zoom(0, 5)
                if event.key == pygame.K_DOWN:
                    player.player_go_zoom_zoom(0, -5)
 
        # --- Game Logic ---
 
        player.move(current_room.wall_list)
 
        if player.rect.x < -15:
            # if current_room_no == 0:
            #     current_room_no = 2
            #     current_room = rooms[current_room_no]
            #     player.rect.x = 790
            # elif current_room_no == 2:
            #     current_room_no = 1
            #     current_room = rooms[current_room_no]
            #     player.rect.x = 790
            # else:
            current_room_no = 0
            current_room = rooms[current_room_no]
            # player.rect.x = 790
            player.rect.x = 0
 
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                # current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                # current_room_no = 0
                # current_room = rooms[current_room_no]
                player.rect.x = 750
 
        # --- Drawing ---
        if current_room_no == 0:
            screen.blit(room.bg, (0,0))
            screen.blit(player.vince, (60,50))
            screen.blit(player.hexx, (625,80))
        elif current_room_no == 1:
            screen.fill(BLACK)
            screen.blit(player.vince, (350,50))
            screen.blit(player.hexx, (350,350))
        elif current_room_no == 2:
            screen.fill(BLACK)
            screen.blit(room.logo, (30,30))
            screen.blit(room.logo, (30,520))
            screen.blit(room.logo, (725,30))
            screen.blit(room.logo, (725,520))
        elif current_room_no == 3:
            screen.fill(BLACK)
            screen.blit(player.john, (300,150))
            screen.blit(room.logo, (30,30))
            screen.blit(room.logo, (30,520))
            screen.blit(room.logo, (725,30))
            screen.blit(room.logo, (725,520))
        else:
            screen.fill(BLACK)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        pygame.display.flip()
 
        clock.tick(60)

    print("TIME'S UP!")
    pygame.quit()
 
if __name__ == "__main__":
    main()

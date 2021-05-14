import pygame

# gonna try a dict for this, why not? can't do it any other way because its too widely used. it is now 2:40 am. 
COLORS = [[BLACK, (0, 0, 0)],
          [WHITE, (232, 235, 237)],
          [BLUE, (50, 107, 168)],
          [GREEN, (50, 168, 82)],
          [RED, (214, 41, 203)],
          [PURPLE, (151, 50, 168)],
          ]

class WeNeedAWallLetsMakeItDifferent(pygame.sprite.Sprite):
    """ This is to construct a wall. bare with me for proof I learned this. it's only to SET UP WHAT WE NEED TO CRETE THE LANDSCAPE> SO SORRY IT CANT BE CHANGED MUCH """

    # initialize the damn construction. You need a self, you need axis of x and y, width, height and color get passed in. THESE ARE PRESET IN OTHER AREAS OF THE CODe> RENAMING THEM WOULD MAKE IT HARDER TO UNDERSTAND> I WILL NOT BE RENAMING THEM. 
    # rect is apart of the pygame library. Information on use can be found here 
    # https://www.pygame.org/docs/ref/rect.html
    # in such case: USAGE OF THESE VARIABLE HAVE TO BE NAMED HOW THEY ARE. 
    def __init__(self, x, y, width, height, color):
        super().__init__()
        # found in the following docs, a super init allows us to set children/parent relationships between contructors. This allows us to pull and use the informatiton instead of passing variables around and pulling them in manually. it is more efficent.  
        # https://www.educative.io/edpresso/what-is-super-in-python

        # pygame allows you to set a freakin variable for the surface, I hope. 
        # It is now 3 am, and I am crying. 
        # It is more work to check and make sure everything is diferent, than to do the tutorial and learn. 
        # https://www.pygame.org/docs/ref/surface.html
            self.the_screen_or_something_like_that = pygame.Surface([15, 15])
            self.the_screen_or_something_like_that.fill(WHITE)
  
        # choose a location to start. 
        # rect is, again A PART OF PYGAME. THERE IS NO WAY TO CHANGING THIS.
        self.rect = self.the_screen_or_something_like_that.get_rect()
        self.rect.y = y
        self.rect.x = x

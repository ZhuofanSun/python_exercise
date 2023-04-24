# Pre-Poke The Dots Version Five
# we are learning how to do the following things:
#
# Re-approach what we have written so far, with the goal of using a class to define the
# attributes and behaviors of a Game to be used in Poke the Dots.
#
# Some of the source code contained in this program is not original. It was borrowed from
# a tutorial found on pygame's website. Specifically, we used portions of this tutorial
# to respond to QUIT events and close the PyGame grapical window, to create a
# game window, and to understand how to use the flip() function to render graphics.
# https://www.pygame.org/docs/tut/PygameIntro.html
import pygame


def main():
    # initialize pygame -- this is required for rendering fonts
    pygame.init()

    # create the window and set its size to 500 width and 400 height
    size = (500, 400)
    screen = pygame.display.set_mode(size)

    # set the title of the window
    pygame.display.set_caption("Poke the Dots")

    game = Game(screen)
    game.play()


class Game:
    # the types of attributes that a game might have
    # --- general to all games
    # screen objects are being drawn to
    # background color
    # game clock
    # FPS limit
    # is the game over? (continue_game)
    # ---specific to poke the dots:
    # big dot
    # small dot
    # maximum frames
    # current frames
    def __init__(self, game_screen):
        # --- attributes that are general to all games
        self.screen = game_screen
        self.bg_color = pygame.Color('black')
        self.game_clock = pygame.time.Clock()
        self.FPS = 30
        self.continue_game = True
        self.close_clicked = False

        # --- attributes that are specific to Poke The Dots        
        # game objects that are specific to poke the dots
        big_dot_color = pygame.Color('blue')
        big_dot_pos = [150, 150]
        big_dot_velocity = [2, 1]
        big_dot_radius = 40
        self.big_dot = Dot(big_dot_color, big_dot_radius, big_dot_pos, big_dot_velocity, self.screen)

        small_dot_color = pygame.Color('red')
        small_dot_pos = [300, 150]
        small_dot_velocity = [1, 2]
        small_dot_radius = 30
        self.small_dot = Dot(small_dot_color, small_dot_radius, small_dot_pos, small_dot_velocity, self.screen)

        self.frame_counter = 0
        self.max_frames = 100

    def play(self):
        # Play the game until the player presses the close box.
        while not self.close_clicked:
            self.handle_events()
            self.draw()

            # look at game over conditions
            # if those conditions are not met:
            #   update the game state
            #   check if game over conditions are now met
            if self.continue_game:
                self.update()
                self.decide_continue()

            self.game_clock.tick(self.FPS)

    def handle_events(self):
        # Checks for new events generated by user input, and then change our
        # game state appropriately.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        # draws all game objects to screen

        # clear our screen before we draw game objects        
        self.screen.fill(self.bg_color)

        # draw our dot to screen
        self.small_dot.draw()
        self.big_dot.draw()

        # render all drawn objects to the screen
        pygame.display.flip()

    def update(self):
        # Update all of our game's objects
        self.small_dot.move()
        self.big_dot.move()
        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        if self.frame_counter > self.max_frames:
            self.continue_game = False


class Dot:
    # represents a single 'dot' in Poke the Dots
    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, screen):
        self.color = dot_color
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.screen = screen

    def move(self):
        # Change the location of the Dot by adding the corresponding
        # speed values ot hte dot's x and y coordinates of its center.
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.velocity[index]

    def draw(self):
        # Draw the dot onto the game's window
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)


main()

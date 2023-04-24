import pygame
import random


# User-defined functions

def main():
    # Initialize pygame
    pygame.init()
    # create a pygame display window and get its surface
    w_surface = pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Tic Tac Toe')
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True
        # === game specific objects
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.turn = self.player_1
        self.board_size = 3
        self.board = []
        self.filled_count = 0  # NEW how many tiles have been filled in
        self.flashers = []  # NEW tiles that need to flash
        self.create_board()

    def create_board(self):
        # Create the game board.
        # - self is the Game whose board is created
        width = self.surface.get_width() // self.board_size
        height = self.surface.get_height() // self.board_size
        for row_index in range(0, self.board_size):
            row = self.create_row(row_index, width, height)
            self.board.append(row)

    def create_row(self, row_number, width, height):
        # Create one row of the board
        # - self is the Game whose board row is being created
        # - row_number is the int index of the row starting at 0
        # - width is the int width of the row in pixels
        # - height is the int height of the row in pixels
        row = []
        y = row_number * height
        for column_index in range(0, self.board_size):
            x = column_index * width
            tile = Tile(x, y, width, height, self.surface)
            row.append(tile)
        return row

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_event()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_event(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and self.continue_game:
                self.handle_mouse_up(event)

    def handle_mouse_up(self, event):
        # Respond to the player releasing the mouse button by
        # taking appropriate actions.
        # - self is the Game where the mouse up occurred.
        # - event is the pygame.event.Event object to handle
        for row in self.board:
            for tile in row:
                if tile.select(event.pos, self.turn):
                    self.filled_count = self.filled_count + 1
                    self.change_turn()

    def change_turn(self):
        # A player has taken a legal action. Change turns to
        # the other player.
        # - self is the TTT Game.
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color)  # clear the display surface first
        self.select_flasher()
        for row in self.board:
            for tile in row:
                tile.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects.
        # - self is the Game to update
        pass

    def decide_continue(self):
        # Determine if the game should continue
        # - self is the Game to update
        if self.is_win() or self.is_tie():
            self.continue_game = False


    def is_row_win(self):
        # Return True if there are 3 equal non-empty marks in any
        # row. Otherwise, return False.
        win = False
        list_of_lists_of_tiles = self.board
        if self.contains_list_win(list_of_lists_of_tiles):
            win = True
        return win

    def contains_list_win(self, list_of_lists_of_tiles):
        # returns True if the list of lists of tiles has a winning row or column or diagonal
        # False otherwise
        win = False
        for list_of_tiles in list_of_lists_of_tiles:
            if self.is_list_win(list_of_tiles):
                win = True
        return win

    def is_list_win(self, list_of_tiles):
        # return True if all tiles in the list of tiles have the same symbol (X or O)
        # False otherwise
        same = True
        first = list_of_tiles[0]
        for tile in list_of_tiles:
            if not (tile == first):  # use __eq__ method in the Tile class
                same = False
        # if list representing row or column or diagonal is a win add it to self.flashers
        if same:
            for tile in list_of_tiles:
                self.flashers.append(tile)
        return same

    def is_column_win(self):
        # Return True if there are 3 equal non-empty marks in any
        # column. Otherwise, return False.
        win = False
        list_of_lists_of_tiles = []
        for col_index in range(0, self.board_size):
            column = []
            for row_index in range(0, self.board_size):
                tile = self.board[row_index][col_index]
                column.append(tile)
                # print(row_index, col_index)
            list_of_lists_of_tiles.append(column)
        if self.contains_list_win(list_of_lists_of_tiles):
            win = True
        return win

    def is_diagonal_win(self):
        # Return True if there are 3 equal non-empty marks in any
        # diagonal. Otherwise, return False.
        win = False
        list_of_lists_of_tiles = []
        diagonal1 = []
        diagonal2 = []
        for index in range(0, self.board_size):
            # print(self.board_size)
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][self.board_size - index - 1]  # 3-0-1,3-1-1,3-2-1
            # print(index, self.board_size -index - 1)
            diagonal2.append(tile)
        list_of_lists_of_tiles.append(diagonal1)
        list_of_lists_of_tiles.append(diagonal2)
        if self.contains_list_win(list_of_lists_of_tiles):
            win = True
        return win

    def is_win(self):
        # Return True if there are 3 equal non-empty marks in any
        # row, column or diagonal. Otherwise, return False.
        win = False
        row_win = self.is_row_win()
        column_win = self.is_column_win()
        diagonal_win = self.is_diagonal_win()
        if row_win or column_win or diagonal_win:
            win = True
        return win

    def is_tie(self):
        # returns True if all tiles have been filled out
        # False otherwise
        tie = False
        if self.filled_count == self.board_size ** 2:
            tie = True
        # add all tiles to self.flashers
        if tie:
            for row in self.board:
                for tile in row:
                    self.flashers.append(tile)
        return tie

    def select_flasher(self):
        # count = len(self.flashers)
        # if count != 0:
        # time.sleep(self.flash_pause)
        # self.flash_index = (self.flash_index + 1) % count
        # self.flashers[self.flash_index].flash()
        if len(self.flashers) != 0:
            tile = random.choice(self.flashers)
            tile.flash()


class Tile:
    # An object in this class represents a Rectangular tile
    # that contains a string. A new tile contains an empty
    # string. A tile can be selected if the tile contains a
    # position. If an empty tile is selected its string can
    # be changed. If a non-empty tile is selected it will flash
    # the next time it is drawn.

    def __init__(self, x, y, width, height, surface):
        # Initialize a tile to contain a ' '
        # - x is the int x coord of the upper left corner
        # - y is the int y coord of the upper left corner
        # - width is the int width of the tile
        # - height is the int height of the tile
        self.content = ''
        self.rect = pygame.Rect(x, y, width, height)
        self.flashing = False  # new in this version
        self.surface = surface
        self.fg_color = pygame.Color('white')
        self.border_width = 3

    def draw(self):
        # Draw the Tile' content, and a rectangle border or
        # flash it.
        # - self is the Tile
        if self.flashing:
            pygame.draw.rect(self.surface, self.fg_color, self.rect)
            self.flashing = False
        else:
            self.draw_content()
            pygame.draw.rect(self.surface, self.fg_color, self.rect, self.border_width)

    def draw_content(self):
        # Draw the string content of the tile.
        # - self is the Tile
        font_size = 133
        font = pygame.font.SysFont('', font_size)
        text_box = font.render(self.content, True, self.fg_color)
        # text_box is an object of type pygame.Surface
        text_box_width = text_box.get_width()
        text_box_height = text_box.get_height()
        d_x = (self.rect.width - text_box_width) // 2
        x = self.rect.x + d_x
        d_y = (self.rect.height - text_box_height) // 2
        y = self.rect.y + d_y
        location = (x, y)
        self.surface.blit(text_box, location)

    def select(self, position, new_content):
        # A position was selected. If the position is in the Tile
        # and the tile is empty, then fill it and return True.
        # Otherwise, set the tile to flash once and return False.
        # - self is the Tile
        # - position is the selected location (tuple)
        # - new_content is the new str contents of the tile
        selected = False
        if self.rect.collidepoint(position):
            if self.content == '':
                self.content = new_content
                selected = True
            else:
                self.flashing = True
        return selected

    def __eq__(self, other):
        # Return True if the contents of the two tiles are
        # non-empty and equal. Otherwise return False.
        # - self is the Tile
        # - other is the other Tile
        return (self.content == other.content) and (self.content != '')

    def flash(self):
        # Set this tile to flash the next time it is drawn.
        # - self is the Tile
        self.flashing = True


main()

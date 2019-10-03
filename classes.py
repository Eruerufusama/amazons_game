class Game():
    def __init__(self, size):
        self.board = [[None for i in range(size)] for i in range(size)]
        self.turn = 0
        self.round = 0
        self.mode = 0

        self.players = []
        self.players.append(Player("white"))
        self.players.append(Player("black"))

        if size == 4:
            amount_of_pieces = 1
        elif size == 6 or size == 8:
            amount_of_pieces = 2
        elif size == 10:
            amount_of_pieces = 4
        
        # Variable used to approximate the position of placed pieces in starting position.
        offset = round(size / 10 * 4) - 1

        # Places a single piece on the board for each color.
        self.board[size - 1][size - 1 - offset] = Piece("white")
        self.board[0][offset] = Piece("black")

        if size > 5:
            # Places one addtional piece for each color onto the board.
            self.board[size - 1 - offset][size - 1] = Piece("white")
            self.board[offset][0] = Piece("black")

        if size > 8:
            # Places two additional pieces for each color onto the board.
            self.board[size - 1][offset] = Piece("white")
            self.board[size - 1 - offset][0] = Piece("white")
            self.board[offset][size - 1] = Piece("black")
            self.board[0][size - 1 - offset] = Piece("black")
        
    
    def destroy_square(self, target):
        # If square is not occupied, destroy it with an arrow.
        if self.board[target[0]][target[1]] == None:
            self.board[target[0]][target[1]] = 0


    def validate_end_pos(self, start, end):
        if start[0] == end[0]:
            if start[1] != end[1]: return True
            else: return False
        if start[1] == end[1]:
            return True
        else:
            if start[0] - start[1] == end[0] - end[1]: return True
            if start[0] + start[1] == end[0] + end[1]: return True
            else: return False


    def move_piece(self, start, end):
        # Check if selected move is a vertical, horizontal, or diagonal move.
        if self.validate_end_pos(start, end):

            # Check if what is being moved is actually a playable piece.
            if self.board[start[0]][start[1]] != None or self.board[start[0]][start[1]] != 0:
                
                # Validate every square along the path the piece will move
                if self.validate_path(self.get_path(start, end)) == True:

                    # Swap piece on board with empty square.
                    self.board[start[0]][start[1]], self.board[end[0]][end[1]] = self.board[end[0]][end[1]], self.board[start[0]][start[1]]
                    
                    # Increase counter of total moves performed.
                    self.board[end[0]][end[1]].moves_performed += 1


    def validate_path(self, list_of_coordinates):
        # Checks if every square along the path the piece will move is not occupied by a piece,
        # nor if it's occupied by an arrow.
        for coordinates in list_of_coordinates:
            if self.board[coordinates[0]][coordinates[1]] != None:
                return False
        return True


    def get_path(self, start, end):
        direction = "diagonal"
        x = 1
        y = 1
        if start[0] > end[0]:
            x = -1
        if start[0] == end[0]:
            direction = "horizontal"
        if start[1] > end[1]:
            y = -1
        if start[1] == end[1]:
            direction = "vertical"

        if direction == "diagonal":
            return [(i, j) for i, j in zip(
                    range(start[0] + x, end[0] + x, x),
                    range(start[1] + y, end[1] + y, y))
                    ]
        elif direction == "vertical":
            return [(i, start[1]) for i in range(start[0] + x, end[0] + x, x)]
        elif direction == "horizontal":
            return [(start[0], i) for i in range(start[1] + y, end[1] + y, y)]


    def increment_time(self):
        self.mode += 1

        if self.mode == 2:
            self.mode = 0
            self.round += 1

            if self.round == 2:
                self.round = 0
                self.turn += 1

                if self.turn == 2:
                    self.turn = 0

                    
class Piece:
    def __init__(self, color):
        self.color = color
        self.moves_performed = 0
        self.arrows_shot = 0

class Player:
    def __init__(self, color):
        self.color = color
        self.arrows_fired = 0
        self.moves = 0
    
    def fire_arrow(self):
        self.arrows_fired += 1
    
    def move(self):
        self.move += 1
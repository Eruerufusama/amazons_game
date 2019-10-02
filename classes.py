class Board:
    def __init__(self, size):
        self.board = [[None for i in range(size)] for i in range(size)]

        if size == 4:
            amount_of_pieces = 1
        elif size == 6 or size == 8:
            amount_of_pieces = 2
        elif size == 10:
            amount_of_pieces = 4
        
        
        offset = round(size / 10 * 4) - 1

        self.board[size - 1][size - 1 - offset] = Piece("white")
        self.board[0][offset] = Piece("black")

        if size > 5:
            self.board[size - 1 - offset][size - 1] = Piece("white")
            self.board[offset][0] = Piece("black")

        if size > 8:
            self.board[size - 1][offset] = Piece("white")
            self.board[size - 1 - offset][0] = Piece("white")
            self.board[offset][size - 1] = Piece("black")
            self.board[0][size - 1 - offset] = Piece("black")
        
    
    def destroy_square(self, target):
        self.board[target[0]][target[1]] = 0

    def move_piece(self, start_pos, end_pos):
        print(type(self.board[start_pos[0]][start_pos[1]]))
        if self.board[start_pos[0]][start_pos[1]] != None or self.board[start_pos[0]][start_pos[1]] != 0:
            if self.validate_squares(self.get_path(start_pos, end_pos)) == True:
                self.board[start_pos[0]][start_pos[1]], self.board[end_pos[0]][end_pos[1]] = self.board[end_pos[0]][end_pos[1]], self.board[start_pos[0]][start_pos[1]]
                self.board[end_pos[0]][end_pos[1]].moves_performed += 1

    def validate_squares(self, list_of_coordinates):
        for coordinates in list_of_coordinates:
            if self.board[coordinates[0]][coordinates[1]] != None:
                return False
        return True
    def get_path(self, start_pos, end_pos):
        direction = "diagonal"
        x = 1
        y = 1
        if start_pos[0] > end_pos[0]:
            x = -1
        if start_pos[0] == end_pos[0]:
            direction = "horizontal"
        if start_pos[1] > end_pos[1]:
            y = -1
        if start_pos[1] == end_pos[1]:
            direction = "vertical"

        if direction == "diagonal":
            return [
                (i, j)
                for i, j in zip(
                    range(start_pos[0] + x, end_pos[0] + x, x),
                    range(start_pos[1] + y, end_pos[1] + y, y))
                    ]
        elif direction == "vertical":
            return [(i, start_pos[1]) for i in range(start_pos[0] + x, end_pos[0] + x, x)]
        elif direction == "horizontal":
            return [(start_pos[0], i) for i in range(start_pos[1] + y, end_pos[1] + y, y)]

class Piece:
    def __init__(self, color):
        self.color = color
        self.moves_performed = 0
        self.arrows_shot = 0
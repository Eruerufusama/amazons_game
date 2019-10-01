class Board():
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for i in range(size)]     

current_board = Board(8)
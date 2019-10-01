class Board():
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for i in range(size)]
    
    def move(self, direction):
        pass
        # TODO
        # check if move is valid (horizontal, vertical, or diagonal)
        # check if there is an obstacle in the way.
        # perform move

    def shoot(self, target):
        pass
        # TODO
        # check if target is not already destroyed, or a player is on the target.
        # Destroy target coordinate.

###########################################
##                                       ##
##    ####     ###    ###   ##  ######   ##
##   ##       ##  #   ## # # #  ##       ##
##   ##  ##  #######  ##  #  #  ####     ##
##   ##   #  ##    #  ##     #  ##       ##
##    ####   ##    #  ##     #  ######   ##
##                                       ##
###########################################

class GameManager():
    def __init__(self, size):
        self.board_size = size
        self.create_board(size)
        self.create_counters()
        self.players = []
        self.create_players()

        # Variable used to approximate the position of placed pieces in starting position.
        offset = round(size / 10 * 4) - 1
        
        for player in self.players:
            player.create_pieces(player.color, size)
        # Player 1
            # Assigns coordinates to selected piece
        self.players[0].pieces[0].position = (size-1, size-1-offset)
            # Places piece on board.
        self.board[size-1][size-1-offset] = self.players[0].pieces[0]

        # Player 2
            # Assigns coordinates to selected piece.
        self.players[1].pieces[0].position = (0, offset)
            # Places piece on board.
        self.board[0][offset] = self.players[1].pieces[0]

        if size > 5:
            # Player 1
                # Assigns coordninates to selected piece.
            self.players[0].pieces[1].position = (size-1-offset, size-1)
                # Places one addtional piece on board.
            self.board[size-1-offset][size-1] = self.players[0].pieces[1]
            
            # Player 2
                # Assigns coordinates to selected piece.
            self.players[1].pieces[1].position = (offset, 0)
                # Places one additional piece on board.
            self.board[offset][0] = self.players[1].pieces[1]

        if size > 8:
            # Player 1
                # Assigns coordnates to pieces.
            self.players[0].pieces[2].position = (size-1, offset)
            self.players[0].pieces[3].position = (offset, size-1)
                # Places two additional pieces onto the board.
            self.board[size-1][offset] = self.players[0].pieces[2]
            self.board[offset][size-1] = self.players[0].pieces[3]

            # Player 2
                # assigns coordnates to pieces.
            self.players[1].pieces[2].position = (size-1-offset, 0)
            self.players[1].pieces[3].position = (0, size-1-offset)
                # places two additional pieces onto the board.
            self.board[size-1-offset][0] = self.players[1].pieces[2]
            self.board[0][size-1-offset] = self.players[1].pieces[3]


    def create_board(self, size):
        self.board = [[None for i in range(size)] for i in range(size)]
    
    def create_players(self):
        self.players.append(Player("white"))
        self.players.append(Player("black"))
    
    def create_counters(self):
        self.turn = 0
        self.round = 0
        self.mode = 0

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

################################################
##                                            ##
##   #####   ####   ######    ####   ######   ##
##   ##   #   ##   ##      ##    #  ##        ##
##   #####    ##   ####    ##       ####      ##
##   ##       ##   ##      ##    #  ##        ##
##   ##      ####   ######    ####   ######   ##
##                                            ##
################################################
                    
class Piece:
    def __init__(self, color):
        self.color = color
        self.moves_performed = 0
        self.position = ()
    
    def validate_path(self, list_of_coordinates, gameobject):
        for coordinates in list_of_coordinates:
            if gameobject.board[coordinates[0]][coordinates[1]] != None:
                return False
        return True

    def get_path(self, start, end):
        direction = "diagonal"
        x, y = 1, 1
        
        if start[0] > end[0]: x = -1
        if start[0] == end[0]: direction = "horizontal"
        if start[1] > end[1]: y = -1
        if start[1] == end[1]: direction = "vertical"

        if direction == "diagonal":
            return [(i, j) for i, j in zip(
                    range(start[0] + x, end[0] + x, x),
                    range(start[1] + y, end[1] + y, y))
                    ]
        elif direction == "vertical":
            return [(i, start[1]) for i in range(start[0] + x, end[0] + x, x)]
        elif direction == "horizontal":
            return [(start[0], i) for i in range(start[1] + y, end[1] + y, y)]

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


    def move(self, end):
                # Check if selected move is a vertical, horizontal, or diagonal move.
        if self.validate_end_pos(self.position, end):

            # Check if what is being moved is actually a playable piece.
            if self.board[self.position[0]][self.position[1]] != None or self.board[self.position[0]][self.position[1]] != 0:
                
                # Validate every square along the path the piece will move
                if self.validate_path(self.get_path(self.position, end)) == True:

                    # Swap piece on board with empty square.
                    self.board[self.position[0]][self.position[1]], self.board[end[0]][end[1]] = self.board[end[0]][end[1]], self.board[self.position[0]][self.position[1]]
                    
                    # Increase counter of total moves performed.
                    self.board[end[0]][end[1]].moves_performed += 1
        self.position = end


#########################################################
##                                                     ##
##   #####   ##        ###    ##   #  ######  #####    ##
##   ##   #  ##       ##  #    ## #   ##      ##   #   ##
##   #####   ##       #####     ##    ####    ####     ##
##   ##      ##      ##    #    ##    ##      ##  #    ##
##   ##      ######  ##    #    ##    ######  ##   #   ##
##                                                     ##
#########################################################

class Player:
    def __init__(self, color):
        self.color = color
        self.arrows_fired = 0
        self.moves = 0
        self.pieces = []
    

    def create_pieces(self, color, board_size):
        if board_size == 4:
            amount_of_pieces = 1
        elif board_size == 6 or board_size == 8:
            amount_of_pieces = 2
        elif board_size == 10:
            amount_of_pieces = 4

        self.pieces =  [Piece(color) for i in range(amount_of_pieces)]


    def fire_arrow(self, target):
        # If square is not occupied, destroy it with an arrow.
        if self.board[target[0]][target[1]] == None:
            self.board[target[0]][target[1]] = 0
            self.arrows_fired += 1
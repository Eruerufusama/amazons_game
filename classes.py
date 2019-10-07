from functions import val_end_pos, get_path

##########################################################################################################
##                                                                                                      ##
##    ####     ###    ###   ##  ######    ##   ##    ###    ##    #    ###     ####   ######  #####     ##
##   ##       ##  #   ## # # #  ##        ### # #   ##  #   ###   #   ##  #   ##      ##      ##   #    ##
##   ##  ##  #######  ##  #  #  ####      ## #  #  #######  ## #  #  #######  ##  ##  ####    #####     ##
##   ##   #  ##    #  ##     #  ##        ##    #  ##    #  ##  # #  ##    #  ##   #  ##      ##  ##    ##
##    ####   ##    #  ##     #  ######    ##    #  ##    #  ##   ##  ##    #   ####   ######  ##   ##   ##
##                                                                                                      ##
##########################################################################################################

class Game():
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

    def destroy_square(self, target):
        # If square is not occupied, destroy it with an arrow.
        if self.board[target[0]][target[1]] == None:

            # Destroy square.
            self.board[target[0]][target[1]] = 0

            # increment counter for player firing arrow.
            self.players[self.turn].inc_arrows_fired()
        
        self.increment_time()

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
        # Mode is the lowest amount of time that can pass. Increment this on every iteration.
        self.mode += 1

        # There are only 2 modes. Increment round if it reaches 2, and reset mode.
        # round decides which players 'turn' it is.
        if self.mode == 2:
            self.mode = 0
            self.round += 1
        
            # There are only 2 players. Thus, reset the turn-counter once it reaches 2.
            # Increment round. This is never reset.
            if self.turn == 2:
                self.turn = 0
                self.round += 1

    def validate_path(self, list_of_coordinates):
        for coordinates in list_of_coordinates:
            if self.board[coordinates[0]][coordinates[1]] != None:
                return False
        return True

    def move_piece(self, piece, end):
        start = (piece.position[0], piece.position[1])

        # Check if selected move is a vertical, horizontal, or diagonal move.
        if val_end_pos(piece.position, end):

            # Check if what is being moved is actually a playable piece.
            if self.board[start[0]][start[1]] != None or self.board[start[0]][start[1]] != 0:

                path = get_path(start, end)

                # Validate every square along the path the piece will move
                if self.validate_path(path) == True:

                    # Swap piece on board with empty square.
                    self.board[start[0]][start[1]], self.board[end[0]][end[1]] = self.board[end[0]][end[1]], self.board[start[0]][start[1]]

                    # Increase counter of total moves performed.
                    self.board[end[0]][end[1]].moves_performed += 1

        piece.position = end
        self.increment_time()

################################################
##                                            ##
##   #####   ##   ######    ####   ######     ##
##   ##   #  ##   ##      ##    #  ##         ##
##   #####   ##   ####    ##       ####       ##
##   ##      ##   ##      ##    #  ##         ##
##   ##      ##   ######    ####   ######     ##
##                                            ##
################################################
                    
class Piece:
    def __init__(self, color):
        self.color = color
        self.moves_performed = 0
        self.position = ()
    
    def inc_moves(self):
        self.moves_performed += 1

#########################################################
##                                                     ##
##   #####   ##        ###    ##   #  ######  #####    ##
##   ##   #  ##       ##  #    ## #   ##      ##   #   ##
##   #####   ##      #######    ##    ####    #####    ##
##   ##      ##      ##    #    ##    ##      ## ##    ##
##   ##      ######  ##    #    ##    ######  ##  ##   ##
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

    def inc_arrows_fired(self, target):
        self.arrows_fired += 1

    def inc_moves(self):
        total = 0
        for piece in self.pieces:
            total += piece.moves_performed
        self.moves += total

####################################################################
##                                                                ##
##    ####   #####     ##    #####   ##   #  ##   ####    ####    ##
##   ##      ##   #   ## #   ##   #  ##   #  ##  ##   #  ##   #   ##
##   ##  ##  #####   ##   #  #####   ######  ##  ##        ##     ##
##   ##   #  ## ##   ######  ##      ##   #  ##  ##   #  #   ##   ##
##    ####   ##  ##  ##   #  ##      ##   #  ##   ####    ####    ##
##                                                                ##
####################################################################


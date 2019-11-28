class Game:

    def __init__(self, id):
        self.p_one_moved = False
        self.p_two_moved = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move

        if player == 0:
            self.p_one_moved = True
        else:
            self.p_two_moved = True

    def connected(self):
        return self.ready

    def both_p_moved(self):
        return self.p_one_moved and self.p_two_moved

    def winner(self):
        p_one = self.moves[0].upper()[0]
        p_two = self.moves[1].upper()[0]

        winner = -1

        if p_one == "R" and p_two == "S":
            winner = 0
        elif p_one == "S" and p_two == "R":
            winner = 1
        elif p_one == "P" and p_two == "R":
            winner = 0
        elif p_one == "R" and p_two == "P":
            winner = 1
        elif p_one == "S" and p_two == "P":
            winner = 0
        elif p_one == "P" and p_two == "S":
            winner = 1

        return winner

    def reset_moves(self):
        self.p_one_moved = False
        self.p_two_moved = False

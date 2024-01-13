"""
**Battleship Game**

Amazon is building a 2 player game inspired by Battleship. 
We want you to design and code the APIs and objects required for 2 people to play the game against each other.

### About Battleship game

It is a 2 player game where each player gets a NxN board.
Each player begins by placing ships on their board, which are hidden to opponent.
During play, each player shoots the opponents board with an aim to sink the ship.
Player who sinks all of the opponent ships wins.

### Rules:
* Size of the board is 10x10
* Each player gets to place 5 ships (1 of each type) which may be placed vertically/horizontally
* Ship types are:
    Destroyer (fills 2 blocks):
    Submarine (fills 3 blocks):
    Cruiser (fills 3 blocks):
    Battleship (fills 4 blocks):
    Aircraft Carrier (fills 5 blocks):

* All the grids must be hit to sink the ship
* If a players hits a ship, they can play again.
"""

from itertools import cycle


class Board:
    def __init__(self) -> None:
        self.ROWS, self.COLS = 10, 10
        self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.ship_types = {
            "destroyer": 2,
            "submarine": 3,
            "cruiser": 3,
            "battleship": 4,
            "aircraft-carrier": 5,
        }

    def boundary_check(self, x, y):
        if 0 <= x < self.ROWS and 0 <= y < self.COLS:
            return True
        print("LOG: out of boundary!")
        return False


class Player:
    def __init__(self, ships, locations) -> None:
        self.board = Board()
        self.opponent_board = None
        self.assign_ships(ships, locations)

    def assign_ships(self, ships, locations):
        """
        ships: types of ships to be placed.
        locations: (x, y, k) starting (x, y) cordinates of the ship where to be placed on the board.
                    k determines the orientation horizontal/vertical.
        """
        for ship, location in zip(ships, locations):
            x, y, k = location
            if self.board.boundary_check(x, y):
                # horizontal
                if k == 1:
                    for i in range(self.board.ship_types[ship]):
                        _y = y + i
                        if self.board.boundary_check(x, _y):
                            self.board.board[x][_y] += 1
                # vertical
                else:
                    for i in range(self.board.ship_types[ship]):
                        _x = x + i
                        if self.board.boundary_check(_x, y):
                            self.board.board[_x][y] += 1

    def shoot_opponent(self, x, y):
        if self.board.boundary_check(x, y) and self.opponent_board[x][y] > 0:
            self.opponent_board[x][y] -= 1
            print("LOG: shot!")
            return True
        return False


class GameAPI:
    def __init__(self) -> None:
        pass

    def init_game(self) -> None:
        self.player_1 = Player(ships=["destroyer"], locations=[(0, 0, 1)])
        self.player_2 = Player(ships=["destroyer"], locations=[(0, 0, 1)])
        # assign opponent boards
        self.player_1.opponent_board = self.player_2.board.board
        self.player_2.opponent_board = self.player_1.board.board

    def play(self, player, x, y) -> None:
        if player == 1:
            return self.player_1.shoot_opponent(x, y)
        else:
            return self.player_2.shoot_opponent(x, y)

    def _check_winner(self, player):
        for row in player.opponent_board:
            for val in row:
                if val != 0:
                    return False
        return True

    def get_winner(self):
        if self._check_winner(player=self.player_1):
            return "player-1"
        if self._check_winner(player=self.player_2):
            return "player-2"
        return None

    def _display_board(self, player):
        for row in player.board.board:
            for val in row:
                print(val, end=" ")
            print(end="\n")

    def display_boards(self):
        print("\n---------- Player 1 Board ---------- \n")
        self._display_board(player=self.player_1)
        print("\n---------- Player 2 Board ---------- \n")
        self._display_board(player=self.player_2)


game = GameAPI()
game.init_game()
game.display_boards()


players = cycle([1, 2])
shot = False
winner = None
while not winner:
    if not shot:
        player = next(players)
    x, y = list(map(int, input(f"\nplayer-{player}: ").split(",")))
    if (x, y) != (-1, -1):
        shot = game.play(player, x, y)
    else:
        shot = True
        game.display_boards()

    winner = game.get_winner()

print(f"winner: {winner}")

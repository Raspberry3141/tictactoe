class Tictactoe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = "0"
        self.player_count = 1
        self.running = True
        self.mainloop()

    def mainloop(self):
        while self.running:
            print(self.running)
            self.printout()
            self.ask()
            if self.check_winner():
                self.running = False

    def ask(self):
        if self.player_count == 1:
            self.player = "X"
        elif self.player_count == 0:
            self.player = "0"
        row = int(input(f"row?{self.player}: "))
        column = int(input(f"column?{self.player}: "))
        if self.board[row][column] == " " and 0 <= row < 3 and 0 <= column < 3:
            self.board[row][column] = self.player
            self.player_count = 1 - self.player_count
        else:
            print("occupied")

    def printout(self):
        print("  0|1|2")
        for i in range(len(self.board)):
            print("  " + "-" * 5)
            print(f"{i}:{"|".join(self.board[i])}")
        print("  " + "-" * 5)

    def check_winner(self):
        # Check rows
        for row in self.board:
            if all(cell == self.player for cell in row):
                print(f"{self.player} won!")
                return True

        # Check columns
        for i in range(3):
            if all(self.board[j][i] == self.player for j in range(3)):
                print(f"{self.player} won!")
                return True

        # Check diagonals
        if all(self.board[i][i] == self.player for i in range(3)) or \
                all(self.board[i][2 - i] == self.player for i in range(3)):
            print(f"{self.player} won!")
            return True

        return False


if __name__ == "__main__":
    tictactoe = Tictactoe()

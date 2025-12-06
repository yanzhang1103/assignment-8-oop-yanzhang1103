class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
      
        for i, row in enumerate(self.grid):
            print(" | ".join(cell if cell != " " else " " for cell in row))

            if i < len(self.grid) - 1:
                print("-" * 9)



    def update_board(self, row: int, col: int, symbol: str) -> bool:
        
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
  

        for row in self.grid:
            if row[0] != " " and row[0] == row[1] == row[2]:
                return row[0]

    # Check columns
        for col in range(3):
            if (
                self.grid[0][col] != " "
                and self.grid[0][col] == self.grid[1][col] == self.grid[2][col]
        ):
                return self.grid[0][col]

    # Check diagonal (top-left → bottom-right)
        if (
            self.grid[0][0] != " "
            and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]
    ):
         return self.grid[0][0]

    # Check diagonal (top-right → bottom-left)
        if (
            self.grid[0][2] != " "
            and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]
    ):
            return self.grid[0][2]

    # No winner
        return ""


    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)

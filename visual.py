

class GridVisual:

    def show_board(grid):
        ROWS = grid.ROWS
        COLS = grid.COLS

        for x in range(1, ROWS - 1):
            print('----------------------')
            out = '| '
            for y in range(1, COLS - 1):
                if (x, y) == grid.state:
                    out += '2 | '  # 2 for the agent location
                elif grid.board[x][y] == 3:
                    out += 'G | '  # for the goal cell
                elif grid.board[x][y] == 1:
                    out += '# | '  # draw # for walls or obstacles
                elif grid.board[x][y] == 0:
                    out += '  | '  # 0  == 'space' for empty cell
            print(out)
        print('-----------------------')

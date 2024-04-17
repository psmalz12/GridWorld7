from env import Grid
from visual import GridVisual

if __name__ == "__main__":
    grid = Grid(state=(5, 1))  # the start location
    print('//////// agent current Location "2" ////////')
    GridVisual.show_board(grid)
    grid.action(1000)  # number of actions/iterations in the environment

    


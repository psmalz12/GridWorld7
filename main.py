from env import Grid
from visual import GridVisual

# need to add a loop here for the num of iter 16/04
if __name__ == "__main__":
    grid = Grid(state=(5, 1))  # the start location
    print('//////// agent current Location "2" ////////')
    GridVisual.show_board(grid)
    grid.action(1000)  # number of actions/iterations in the environment

    
# will add random action choice  16/04
# add print action, reward, and term (achieve the goal or not) 


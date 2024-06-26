import random
import visual

ROWS = 7
COLS = 7
Goal = (1, 5)
walls = [(2, 5), (2, 4), (2, 3), (3, 2)]

class Grid:
    def __init__(self, state):
        self.state = state
        self.board = []
        self.ROWS = ROWS
        self.COLS = COLS
        self.num_iter = 0  # to print later the num of iter in action fun
        self.lis_state_pair = []  # tuple list to save the state that has been visted during the learning / not needed  16/04
        self.action_state_pairs = {}  # init action_state_pairs as an empty dictionary for the whole iter  

        for x in range(ROWS): # the grid should start normal not upside down that mean the bottom left corner should be (1,1) 16/04
                row = []
                for y in range(COLS):
                    if (x == 0 or y == 0 or x == ROWS - 1 or y == COLS - 1) or (x, y) in walls:
                        row.append(1)  # walls & border
                    elif (x, y) == Goal:
                        row.append(3)
                    else:
                        row.append(0)  # empty cells
                self.board.append(row)

    def reset(self):
        return self.state    # Later I might def this as a reset method to randomly start from any location in the grid not from the same location every time

    def action(self, num_iter):
        self.num_iter = num_iter  # update the num iter
        actions = { # not needed because I will pass the random action num to agent_move fun 16/04
            "up": 0,
            "down": 1,
            "right": 2,
            "left": 3
        }
        for _ in range(num_iter):
            random_action_code = random.randint(0, 3)      # as discussed move to main to pick a random action 16/04
            random_action = list(actions.keys())[random_action_code]
            print(f"Next Move: {random_action}")
            current_state = self.state
            new_state = self.agentmove(random_action)

            # to check if the new state is the same as the current state (agent hit a wall)
            if new_state == current_state:
                print("Agent hit a wall or obstacle") 
                continue  # Skip storing the action-state pair / this is not correct should record this as a - reward  16/04

            # Update the action-state pairs
            if current_state not in self.action_state_pairs:
                self.action_state_pairs[current_state] = {}
            if random_action_code not in self.action_state_pairs[current_state]:
                self.action_state_pairs[current_state][random_action_code] = []

            # Store the action-state pair
            self.action_state_pairs[current_state][random_action_code].append(new_state)

            # Visualize the board and print relevant information
            visual.GridVisual.show_board(self)
            print(f"State, Action, Next State: {current_state}, {random_action}, {new_state}") # need to work better in data structure and find a better way to represent this 16/04
            print(f"Action-state pairs: {self.action_state_pairs}")
            print("-------------*********************************---------------")

       # print(f'Number of Iterations: {self.num_iter}') 
        return self.action_state_pairs, random_action

    def agentmove(self, direction, print_move=True):
        current_state = self.state
        fcol, frow = self.state
        # no need to use str here just change it to num 16/04
        if direction == "left":
            fcol = self.state[0]
            frow = self.state[1] - 1
        elif direction == "right":
            fcol = self.state[0]
            frow = self.state[1] + 1
        elif direction == "up":
            fcol = self.state[0] - 1
            frow = self.state[1]
        elif direction == "down":
            fcol = self.state[0] + 1
            frow = self.state[1]

        # check if the movement is within the grid boundaries
        if 0 <= fcol < self.ROWS and 0 <= frow < self.COLS:
            # Check if the new position is not a wall
            if self.board[fcol][frow] != 1:
                next_state = (fcol, frow)
                if print_move:
                    print(f'Agent moved from {current_state} to {next_state}')
                self.state = next_state
            else:
                if print_move:
                    print(f'Wall at {fcol, frow}')
                # If the agent hits a wall, update the action-state pair to record the wall
                if current_state not in self.action_state_pairs:
                    self.action_state_pairs[current_state] = {}
                if direction not in self.action_state_pairs[current_state]:
                    self.action_state_pairs[current_state][direction] = "Wall"
        else:
            if print_move:
                print(f'Agent cannot move {direction}.')


        return self.state

    def reward(self, current_state, action):
        # count the new state based on the action
        new_state = self.agentmove(action, print_move=False)
        reward = 0             # need to check the validity of the reward fun 16/04
        if self.board[new_state[0]][new_state[1]] == 0:
            reward = -0.1  # if the new state is 0 tha agent will take a -0.1 reward
        elif self.board[new_state[0]][new_state[1]] == 1:
            reward = -0.1  #  if the new state is 1 tha agent will take a -0.1 reward (wall and obstacles)
        elif self.board[new_state[0]][new_state[1]] == 3:
            reward = 1  #  if the new state is 3 tha agent will take a +1 reward (achive the goal)

        return reward


#[0][0] [0][1] [0][2] [0][3] [0][4] [0][5] [0][6]
#[1][0] [1][1] [1][2] [1][3] [1][4] [1][5] [1][6]
#[2][0] [2][1] [2][2] [2][3] [2][4] [2][5] [2][6]
#[3][0] [3][1] [3][2] [3][3] [3][4] [3][5] [3][6]
#[4][0] [4][1] [4][2] [4][3] [4][4] [4][5] [4][6]
#[5][0] [5][1] [5][2] [5][3] [5][4] [5][5] [5][6]
#[6][0] [6][1] [6][2] [6][3] [6][4] [6][5] [6][6]

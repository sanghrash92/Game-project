"""Conway's Game of life.
The classic cellular automata simulation. Press ctrl-c to stop."""

import copy, random, sys, time

# Set up the constants.
WIDTH =  79 # The width of the cell grid.
HEIGHT = 20 # The height of the cell grid.

# Try changing ALIVE to '#' or another character.
ALIVE = 'O' # The character representing a living cell.
# Try changing DEAD to '.' or another character.
DEAD = ' ' # The character representing a dead cell.

# (!) Try changing ALIVE to '|' and DEAD to '-'.

# The cells and nextCells are dictionaries for the state of the game.
# Their kes are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
nextCells = {}
# Put random dead and alive cells into nextCells.
for x in range(WIDTH): # Loop over every possible column.
    for y in range(HEIGHT): # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE # Add a living cell.
        else:
             nextCells[(x, y)] = DEAD # Add a dead cell.

while True: 
    # Each iteration of this loop is a step of the simulation.
    
    print('\n' * 50) # Seperate each step with newlines.
    cells = copy.deepcopy(nextCells)
    
    # Print cells on the screen.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='') # Print the # or space.
        print() # Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')
    
    # Calculate the next step's cells based on current step's cells.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighbouring coordinates of (x, y), even if they
            # wrap around the edge.
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
            
            # Count the number of living neighbors.
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1 # Top-left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1 # Top-right neighbor is alive.
            if cells[(left, y)] == ALIVE:  
                numNeighbors += 1 # Left neighbor is alive.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1 # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1 # Bottom left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 # Bottom-right neighbor is alive.
                
            # Set cell based on conway's game of life rules.
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or 
                                           numNeighbors == 3):
                # Living cells with 2 or 3 nrighbors stay alive.
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 31:
                # Dead cells with 3 neighbors become alive.
                nextCells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead.
                nextCells[(x, y)] = DEAD
    
    try:
        time.sleep(1) # Add a 1 second pause to reduce flickering.
    except keyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()
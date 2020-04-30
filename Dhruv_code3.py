# Importing
import pygame

# Defining the maze of cells 8*8
maze = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']

]

#  Defining the maze of cells and walls 16*15
maze_wall = [
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e']

]

# Asking the user for the target cell coordinates
t_row = int(input("Enter the target row : "))
t_col = int(input("Enter the target column : "))

# Defining few variables
constant = 75
k = 25

# Initializing pygame and the font
pygame.init()
pygame.font.init()
# Creating the screen
screen = pygame.display.set_mode((600, 600))

# Setting the caption and the font for the pygame window
pygame.display.set_caption("Navigator Grid")
font = pygame.font.Font('JandaManateeSolid.ttf', 32)

# Setting the value of the target cell to 0
maze[t_row][t_col] = 0


# The fill function writes the numbers into the grid
# It searches the maze for value = c and it writes the adjecent empty cells a value one higher than c
# This happens until all the cells have a value
def fill():
    check_t = True
    check_r = True
    check_b = True
    check_l = True
    c = 0
    enter = True
    while enter:
        enter = False
        # Checking all the cells in the maze
        for b in range(8):
            for a in range(8):
                if maze[a][b] == c:
                    enter = True
                    check_b = True
                    check_l = True
                    check_r = True
                    check_t = True
                    # Checking whether there is a wall between the cell and its adjecent cells
                    if b == 0 or maze_wall[a * 2][(b * 2) - 1] == 'w':
                        check_l = False

                    if b == 7 or maze_wall[a * 2][(b * 2) + 1] == 'w':
                        check_r = False

                    if a == 0 or maze_wall[(a * 2) - 1][b * 2] == 'w':
                        check_t = False

                    if a == 7 or maze_wall[(a * 2) + 1][b * 2] == 'w':
                        check_b = False

                    # If there is no wall and the cell does not have a number then it assigns the cell with a value of c+1
                    if check_l == True and maze[a][b - 1] == 'e':
                        maze[a][b - 1] = c + 1

                    if check_r == True and maze[a][b + 1] == 'e':
                        maze[a][b + 1] = c + 1

                    if check_t == True and maze[a - 1][b] == 'e':
                        maze[a - 1][b] = c + 1

                    if check_b == True and maze[a + 1][b] == 'e':

                        maze[a + 1][b] = c + 1
        # C is incremented by one so when it finishes all the cells with a value of c, it moves on to the next number that is c+1
        c += 1

# When a wall is assigned in maze_wall , the user can see the wall on the pygame window because of this function
# Checks all the wall_cell , and those who have a wall , the wall is printed on the pygame window
def wall_detect():
    for wall_y in range(16):
        for wall_x in range(15):
            if maze_wall[wall_x][wall_y] == 'w':
                check_b = True
                check_l = True
                check_r = True
                check_t = True
                if wall_y == 0:
                    check_l = False

                if wall_x == 0:
                    check_t = False

                # If there is a cell surrounding the wall on the left, then draw a rectangle which is vertical
                if check_l == True and maze_wall[wall_x][wall_y - 1] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y + 1) / 2 * constant - 3, (wall_x) / 2 * constant, 6, 75])

                # If there is a cell surrounding the wall on the top, then draw a rectangle which is horizontal
                if check_t == True and maze_wall[wall_x - 1][wall_y] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y) / 2 * constant, (wall_x + 1) / 2 * constant - 3, 75, 6])

# The show_num function takes the coordinates and the value of what to print and prints it on the pygame window
def show_num(x, y, val):
    num = font.render(val, True, (0, 0, 0))
    screen.blit(num, (x, y))

# The num_detect function scans all the cells in maze and feeds them to the show_num function so they are written on the pygame window
def num_detect():
    for y in range(8):
        for x in range(8):
            d = maze[x][y]
            show_num(y * constant + k, x * constant + k, str(d))

# the path_finder function is designed to find the shortest path for the bot.
def path_finder():
    # Asking the user to input coordinates for the start cell
    s_row = int(input("Enter the starting row : "))
    s_col = int(input("Enter the starting column : "))
    # Defining few variables
    close = False
    executed = False
    # Calling the fill function
    fill()
    while maze[s_row][s_col] != 0:
        if close:
            break
        if executed:
            check_b = True
            check_l = True
            check_r = True
            check_t = True
            # Checking whether there is a wall between the adjecent cells
            if s_col == 0 or maze_wall[s_row * 2][s_col * 2 - 1] == 'w':
                check_l = False

            if s_col == 7 or maze_wall[s_row * 2][s_col * 2 + 1] == 'w':
                check_r = False

            if s_row == 0 or maze_wall[s_row * 2 - 1][s_col * 2] == 'w':
                check_t = False

            if s_row == 7 or maze_wall[s_row * 2 + 1][s_col * 2] == 'w':
                check_b = False

            # if there is no wall and the value of the adjecent cell is less than that of the current cell then the bot moves to that cell
            if check_l == True and maze[s_row][s_col - 1] < maze[s_row][s_col]:
                s_col -= 1

            elif check_r == True and maze[s_row][s_col + 1] < maze[s_row][s_col]:
                s_col += 1

            elif check_t == True and maze[s_row - 1][s_col] < maze[s_row][s_col]:
                s_row -= 1

            elif check_b == True and maze[s_row + 1][s_col] < maze[s_row][s_col]:
                s_row += 1

        # Infinite Loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    running = False
                    close = True

                executed = True
                screen.fill((255, 255, 255))
                # Creating the Grid
                for x in range(8):
                    pygame.draw.line(screen, (0, 0, 0), (75 * x, 0), (75 * x, 600))
                for x in range(8):
                    pygame.draw.line(screen, (0, 0, 0), (0, 75 * x), (600, 75 * x))
                # Drawing the Red rectangle which signifies the bot.
                pygame.draw.rect(screen, (255, 0, 0), [s_col * constant, s_row * constant, constant, constant])
                # Calling the functions which display the walls and the numbers
                wall_detect()
                num_detect()
                pygame.display.update()


path_finder()
print('Reached')

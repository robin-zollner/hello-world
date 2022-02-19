'''
import matplotlib
from matplotlib import pyplot as plt


plt.plot([1,2,4], [2, 3, 6])

plt.show()
'''


import pygame
import random as r
import sys
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
print("Enter desired grid size")
grid_size = 25#int(input())
pxls = grid_size * 25
size = (pxls, pxls)
screen = pygame.display.set_mode(size)
width = 20
height = 20
margin = 1


# Click Behaivor

# Before the loop, load the sounds:
#click_sound = pygame.mixer.Sound("laser5.ogg")

# Creating grid of zeros to be referenced later.


grid = [[0 for x in range(grid_size)] for y in range(grid_size)]


row = 0
while row < grid_size:
	column = 0
	grid[column][row] = 1
	while column < grid_size:
		direction = r.randint(0,1)
		if column%2==0:
			grid[column][row] = 1
		if (row > 0) :
			if column > 0:
				if column%2==0:
					if direction == 0:
						grid[column - 1][row] = 1
					else:
						grid[column][row -1 ] = 1
				else:
					pass
			else:
				grid[column][row - 1] = 1
		else:
			grid[column - 1][row] = 1
		column = column + 1
	row = row + 2


 

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
        	pos = pygame.mouse.get_pos()
        	col_pos = int(pos[0] / (margin + width))
        	row_pos = int(pos[1] / (margin + height))
        	if grid[col_pos][row_pos] == 0:
        		grid[col_pos][row_pos] = 2
        	elif grid[col_pos][row_pos] == 1:
        		grid[col_pos][row_pos] = 3
        	print("click Row: {} Column: {}".format(row_pos, col_pos))
 
    # --- Game logic should go here

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)


    # --- Drawing code should go here
    for row in range(grid_size):
    	for column in range(grid_size):
    		if grid[column][row] == 1:
    			color = GREEN;
    		elif grid[column][row] == 2:
    			color = BLUE;
    		elif grid[column][row] == 3:
    			color = MAGENTA;
    		else: color = BLACK
    		pygame.draw.rect(screen, color, [column*(margin + width), row*(margin + height), width, height], 0)

    pygame.draw.rect(screen, CYAN, [pxls, pxls, 3*width, 2*height])				
    		



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
#!/usr/bin/python
# Head ends here
def nextMove( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    return
# Tail starts here
pacman_r, pacman_c = [ int(i) for i in input().strip().split() ]
food_r, food_c = [ int(i) for i in input().strip().split() ]
r,c = [ int(i) for i in input().strip().split() ]

grid = []
for i in range(0, r):
    grid.append(input().strip())

nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)

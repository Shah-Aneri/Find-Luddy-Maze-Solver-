#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [Aneri Shah Username: annishah|2000564352]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]
		

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
	#Along with finding possible moves for traversing also kept track of the compass directions to find the final path.
	moves=((row+1,col,"S"), (row-1,col,"N"), (row,col-1,"W"), (row,col+1,"E"))

	# Return only moves that are within the board and legal (i.e. on the sidewalk ".")
	return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
def search1(IUB_map):
	# Find my start position
	you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
	fringe=[(you_loc,0,'')]
	#Keep track of already viewed nodes
	viewed=[]
#Refered from "https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/" for getting help with python syntax for implementing the code.
#Logic for finding Shortest path and shortest distance using BFS Algorithm
	while fringe:
		#popping the first move, it's corresponding distance and path from the fringe
		(curr_move, curr_dist,path)=fringe.pop(0)
		#Traverse through all posibile moves and find optimal path and add it to the fringe or if it's "@" then return the distance and path. 
		for move in moves(IUB_map, curr_move[0],curr_move[1]):
			if move not in viewed:
				if IUB_map[move[0]][move[1]]=="@":
					#Reached to the Luddy Hall so returning distance of the path and string of compass directions to reach there. 
					return curr_dist+1,path+move[2]
				else:
					fringe.append((move, curr_dist + 1,path+move[2]))
					viewed.append(move)

	#If no solution exists return inf					
	return "Inf "	


# Main Function
if __name__ == "__main__":
	IUB_map=parse_map(sys.argv[1])
	print("Shhhh... quiet while I navigate!")
	solution = search1(IUB_map)
	print("Here's the solution I found:")
	print(*solution)


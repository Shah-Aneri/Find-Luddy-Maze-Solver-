# Find-Luddy-Maze-Solver-

Find_Luddy Problem:- The aim of this problem is to find out the shortest path from my current location to Luddy Hall and also display the compass directions traversed during finding the path.

Initial State:- Initial state here is my current location(#) on the map.

Goal State:- Is to reach Luddy_Hall(@).

State Space:- N*M unit campus map with labels for sidewalks, Luddy Hall, current location and other buildings.

Successor Function:- Moving to any one sidewalk cell from the four directions starting from current location(#) such that it’s value is ‘.’ and’@’.

Path cost:- Cost of moving each sidewalk cell is 1 so the total cost is equal to the distance of the path traversed from # to @(Luddy_Hall).

If there is no path between # and @ then the program returns “INF”.

Explaination:- First of all I  decided on the algorithm to use for solving the problem. In my code, I have used BFS searching algorithm to search the shortest path to the goal state. It uses queue as a data structure and I have used viewed list to keep track of the already explored path. The code works as follows:- First of all, I have assigned compass direction with the moves which my algorithm will follow. Then I am keeping track of the already viewed moves and finally when my search algorithm reaches the goal state then it returns the distance travelled and the directions moved while travelling along the path.


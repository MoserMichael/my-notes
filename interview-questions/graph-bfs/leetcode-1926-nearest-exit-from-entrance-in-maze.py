#1926. Nearest Exit from Entrance in Maze
#Medium
#You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
#
#In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
#
#Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
#
# 
#
#Example 1:
#
#Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
#Output: 1
#Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
#Initially, you are at the entrance cell [1,2].
#- You can reach [1,0] by moving 2 steps left.
#- You can reach [0,2] by moving 1 step up.
#It is impossible to reach [2,3] from the entrance.
#Thus, the nearest exit is [0,2], which is 1 step away.
#
#Example 2:
#
#Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
#Output: 2
#Explanation: There is 1 exit in this maze at [1,2].
#[1,0] does not count as an exit since it is the entrance cell.
#Initially, you are at the entrance cell [1,0].
#- You can reach [1,2] by moving 2 steps right.
#Thus, the nearest exit is [1,2], which is 2 steps away.
#
#Example 3:
#
#Input: maze = [[".","+"]], entrance = [0,0]
#Output: -1
#Explanation: There are no exits in this maze.
#
# 
#
#Constraints:
#
#    maze.length == m
#    maze[i].length == n
#    1 <= m, n <= 100
#    maze[i][j] is either '.' or '+'.
#    entrance.length == 2
#    0 <= entrancerow < m
#    0 <= entrancecol < n
#    entrance will always be an empty cell.
#

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
         entrance =  tuple(entrance)
         visitedSet = set()
         visitedSet.add(entrance)
         return Solution.walk(maze, [ entrance ], 0, visitedSet)   

    @staticmethod
    def walk(graph, positions, distance, visitedSet):    

        #print(f"distance: {distance} positions: {positions}")

        nextPositions = []

        for pos in positions:
            for npos in Solution.getAdjacentCells(graph, pos):
                if npos not in visitedSet: 
                    visitedSet.add(npos)
                    nextPositions.append(npos)    
                    if Solution.isExit(npos, graph):
                        #print(f"exit: {distance+1} {npos}")
                        return distance+1

        if not len(nextPositions):
            return -1

        ret = Solution.walk(graph, nextPositions, distance+1, visitedSet)
        if ret != -1:
            return ret

        return -1


    @staticmethod
    def getAdjacentCells(graph, position):
        displacements = [ (-1,0), (1,0), (0, -1), (0, 1)]

        graph_y = len(graph)
        graph_x = len(graph[0])
        
        ret = []

        for move in displacements:
            try_y = position[0] + move[0]
            try_x = position[1] + move[1]

            if  0 <= try_x < graph_x and 0 <= try_y < graph_y:
                if graph[try_y][try_x] == '.':
                    ret.append( (try_y, try_x) )

        #print(f"adjacent to: {position} -> {ret}")
        return ret



    
    @staticmethod
    def isExit(position, graph):
        if position[0] == 0 or position[0] == len(graph)-1 or position[1] == 0 or position[1] == len(graph[0])-1:
            return True
        return False

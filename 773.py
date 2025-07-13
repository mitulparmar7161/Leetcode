# 773. Sliding Puzzle

# Hard

# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

# Example 1:


# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Example 2:


# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Example 3:


# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
 

# Constraints:

# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.
# 
# 


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        dir = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        target = "123450"
        vis = set() 
        q = deque()
        start = ""

        for row in board:
            for col in row:
                start += str(col)

        q.append(start)
        vis.add(start)
        step = 0

        while q:
            size = len(q)
            for _ in range(size):
                current = q.popleft()

                if current == target:
                    return step

                zero = current.find('0')

                for move in dir[zero]:
                    next_state = list(current)
                    next_state[zero], next_state[move] = next_state[move], next_state[zero]
                    next_state = ''.join(next_state)
                    if next_state not in vis: 
                        vis.add(next_state)
                        q.append(next_state)
            step += 1
        return -1 
    

obj = Solution()
print(obj.slidingPuzzle([[1,2,3],[4,0,5]]))
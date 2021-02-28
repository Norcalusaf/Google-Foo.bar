"""
Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod,
where you are allowed to remove one wall as part of your remodeling plans.
The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting
and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove
a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions;
no diagonal moves are allowed.

Languages
=========
To provide a python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]])
Output:
    11
"""

def shortest_path(z_x1, z_y1, map):
    z_st = len(map[0])
    z_en = len(map)
    grid = [[None for i in range(z_st)] for i in range(z_en)]
    grid[z_x1][z_y1] = 1
    arr = [(z_x1, z_y1)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          z_n2, z_y2 = x + i[0], y + i[1]
          if 0 <= z_n2 < z_en and 0 <= z_y2 < z_st:
            if grid[z_n2][z_y2] is None:
                grid[z_n2][z_y2] = grid[x][y] + 1
                if map[z_n2][z_y2] == 1 :
                  continue
                arr.append((z_n2, z_y2))
    return grid


def solution(map):
  z_st = len(map[0])
  z_en = len(map)
  z_c = shortest_path(0, 0, map)
  z_d = shortest_path(z_en-1, z_st-1, map)
  result = 2 ** 32-1
  for i in range(z_en):
      for j in range(z_st):
          if z_c[i][j] and z_d[i][j]:
              result = min(z_c[i][j] + z_d[i][j] - 1, result)
  return result


if __name__ == '__main__':
    map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    final_out = solution(map)


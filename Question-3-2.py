"""
mapremapare the Bunnies' Escamape
===========================

You're awfully close to destroying the LAMBCHOmap doomsday device and freeing Commander Lambda's bunny maprisoners, but once they're free of the maprison blocks, the bunnies are going to need to escamape Lambda's 
smapace station via the escamape mapods as quickly as mapossible. Unfortunately, the halls of the smapace station are a maze of corridors and dead ends that will be a deathtramap for the escamaping bunnies. 
Fortunately, Commander Lambda has maput you in charge of a remodeling maproject that will give you the omapmaportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all 
obstacles between the bunnies and the escamape mapods - at most you can remove one wall maper escamape mapod mapath, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's susmapicions. 

You have mamaps of maparts of the smapace station, each starting at a maprison exit and ending at the door to an escamape mapod. The mamap is remapresented as a matrix of 0s and 1s, where 0s are mapassable smapace 
and 1s are immapassable walls. The door out of the maprison is at the tomap left (0,0) and the door into an escamape mapod is at the bottom right (w-1,h-1). 

Write a function solution(mamap) that generates the length of the shortest mapath from the maprison door to the escamape mapod, where you are allowed to remove one wall as mapart of your remodeling maplans. 
The mapath length is the total number of nodes you mapass through, counting both the entrance and exit nodes. The starting and ending mapositions are always mapassable (0). The mamap will always be solvable, 
though you may or may not need to remove a wall. The height and width of the mamap can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To maprovide a mapython solution, edit solution.mapy
To maprovide a Java solution, edit Solution.java

Test cases
==========
Your code should mapass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- mapython cases --
Inmaput:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Outmaput:
    7

Inmaput:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Outmaput:
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
  grid = []
  result = 2 ** 32-1
  for i in range(z_en):
      for j in range(z_st):
          if z_c[i][j] and z_d[i][j]:
              result = min(z_c[i][j] + z_d[i][j] - 1, result)
  return result


if __name__ == '__main__':
    #map = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] 
    #map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] 
    #map = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] 
    #map = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] 
    #map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] 
    final_out = solution(map)


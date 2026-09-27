from collections import deque
class Solution:
    def shortestPath(self, grid, source, destination):
        n = len(grid)
        m = len(grid[0])
        q = deque()
        sr , sc  = source
        dr , dc = destination
        if grid[sr][sc] == 0 or grid[dr][dc]== 0 :
            return -1
        # if grid[n][m] == 0:
        #     continue
        q.append((sr,sc,0))
        vis= [[0 for _ in range(m)] for _ in range(n)]  
        vis[sr][sc] = 1
        dir =[(-1,0),(0,-1),(0,1),(1,0)]
        while q:
            r , c , d = q.popleft()
            if r == dr and c == dc:
                return d
            for x , y in dir:
                nr = x + r 
                nc = y + c 
                if (0<= nr <n and 0<= nc <m) and grid[nr][nc] == 1 and vis[nr][nc] == 0 :
                    vis[nr][nc] = 1 
                    q.append((nr,nc,d + 1))
        return -1
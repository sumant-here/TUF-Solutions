from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        m = len(image)
        n = len(image[0])
        vi = set()
        dirc = [(-1,0),(0,-1),(1,0),(0,1)]
        old_c = image[sr][sc]
        if old_c == newColor:
            return image
        vi.add((sr,sc))
        image[sr][sc] = newColor
        q = deque()
        q.append((sr,sc))
        
        while q :
            r , c = q.popleft()
            for dr , dc in dirc:
                nr = dr + r
                nc = dc + c 
                if  0<= nr <  m and  0<= nc < n and image[nr][nc] == old_c and (nr,nc) not in vi:
                    vi.add((nr,nc))
                    image[nr][nc] = newColor 
                    q.append((nr,nc))
        return image
                    

      
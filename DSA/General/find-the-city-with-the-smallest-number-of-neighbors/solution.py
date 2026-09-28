class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        adj = [[10**4 for _ in range(n)] for _ in range(n)]
        for u , v , w in edges:
            adj[u][v] = w
            adj[v][u] = w
        for i in range(n):
            adj[i][i] = 0 
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i][via] != 10**4 and adj[via][j] != 10**4:
                        adj[i][j] = min(adj[i][j],adj[i][via]+adj[via][j])
        min_neigh = n 
        city =-1
        for i in range(n):
            count = 0 
            for j in range(n):
                if adj [i][j] <= distanceThreshold:
                    count += 1
            if count <= min_neigh:
                min_neigh = count
                city = i 
        return city

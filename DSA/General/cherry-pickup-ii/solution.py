class Solution:
    def cherryPickup(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        dp = [[[0 for _ in range(c)] for _ in range(c)] for _ in range(r)]
        # base case 
        for j1 in range(c):
            for j2 in range(c):
                if j1 == j2 :
                    dp[r-1][j1][j2] = matrix[r-1][j1]
                else:
                    dp[r-1][j1][j2] = matrix[r-1][j1] + matrix[r-1][j2]
        for i in range(r-2,-1,-1):
            for j1 in range(c):
                for j2 in range(c):
                    if j1 == j2 :
                        che = matrix[i][j1]
                    else:
                        che = matrix[i][j1]+matrix[i][j2]
                    maxi = float('-inf')
                    for d1 in [-1,0,1]:
                        for d2 in [-1,0,1]:
                            nj1 = j1 + d1
                            nj2 = j2 + d2
                            if (0<= nj1 < c and 0<= nj2< c ):
                                maxi = max(maxi,dp[i+1][nj1][nj2])
                    dp[i][j1][j2] = che + maxi
        return dp[0][0][c-1]
                    
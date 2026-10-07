class Solution:
    def combinationSum(self, candidates, target):
        #your code goes here
        ans = [] # bcz mu sethe store koribi 
        def backt(i , target,current):
            if target == 0 :
                ans.append(current.copy())
                return
            if target < 0 or i == len(candidates):
                return 
            #number take 
            current.append(candidates[i])
            backt(i,target-candidates[i],current)
            #remove number
            current.pop()
            #donot take number
            backt(i+1,target,current)
        backt(0,target,[])
        return ans
from collections import deque
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        words = set(wordList)
        if targetWord not in words:
            return 0
        q = deque()
        q.append((startWord,1))
        vis = set()
        vis.add(startWord)
        while q:
            word,step = q.popleft()
            if word == targetWord:
                return step
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_w = word[:i] + ch + word[i+1:]
                    if new_w in words and new_w not in vis:
                        vis.add(new_w)
                        q.append((new_w,step +1))
        return 0 
    

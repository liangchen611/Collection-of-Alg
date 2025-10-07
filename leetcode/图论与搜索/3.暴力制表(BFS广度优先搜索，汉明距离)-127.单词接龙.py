from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        L = len(wordList)
        table = [[0]*L for _ in range(L)]

        # 建立两两间距离表
        for i in range(L):
            for j in range(i+1, L):
                if sum(a != b for a, b in zip(wordList[i], wordList[j])) == 1:
                    table[i][j] = table[j][i] = 1
        
        # BFS
        que = deque()
        visited = [False]*L
        steps = 1

        # 起点可能不在wordList
        for i, w in enumerate(wordList):
            if sum(a != b for a, b in zip(beginWord, w)) == 1:
                que.append(i)
                visited[i] = True
        
        while que:
            for _ in range(len(que)):
                idx = que.popleft()
                if wordList[idx] == endWord:
                    return steps + 1
                for j in range(L):
                    if table[idx][j] and not visited[j]:
                        visited[j] = True
                        que.append(j)
            steps += 1

        return 0
    
        # 1 2 3 2 3 3
        # 0 1 2 1 2 2
        #   0 1 1 2 2
        #     0 2 1 1
        #       0 1 2
        #         0 1
        #           0

        # cog
        # cog-dog、cog-log
        # cog-dog-dot、cog-log-dog、cog-log-lot
        # cog-dog-dot-dog，cog-log-dot-hot，cog-log-dog-

'''
暴力思路：对于所有单词之间，建立一个两两差异表，算出-汉明距离，然后基于距离表进行BFS广度优先搜索

注意：
1.汉明距离的算出：sum(a != b for a, b in zip(wordList[i], wordList[j])) == 1

2.需要加入一个visited表，来表示某个下标所对应的单词在当前搜索过程中是否已经搜索过（visisted表在BFS中几乎必须，防止重复查找并提高性能）

3.需要判断开头的单词是否存在于wordlist当中，如果存在，那么预先加入队列

BFS：对每次的队列，弹出它当前的下标，如果当前下标所对的单词就是终结词，那么返回长度step+1

如果不是终结词，看它的表中汉明距离为1的位置（在一列中查找），将这些下标加入到que中，然后标记visited

每进行一层的队列BFS，长度step+1

'''
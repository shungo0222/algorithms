# Depth First Search with recursion
# AtCoder Typical Contest 001 - A 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys

# set the upper limit of the number of recursion to 10 ** 8
sys.setrecursionlimit(10**8) 

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

def dfs(x, y):
    # exit conditions
    if not (0 <= x < h) or not (0 <= y < w) or c[x][y] == '#':
        return
    
    # when find the goal
    if c[x][y] == 'g':
        print('Yes')
        exit()
    
    # mark indicating that it has been searched
    c[x][y] = '#'
    
    # exploration with recursion
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sx, sy = i, j

dfs(sx, sy)
print('No')
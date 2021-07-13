# Depth First Search with stack
# AtCoder Typical Contest 001 - A 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
from collections import deque
import numpy as np

class Node(object):
    """
    Class of node

    Parameters
    ----------
    index : list
        the location of node
    nears : list
        the list of adjacent nodes
    visit : bool
        the sign indicating visited or not
        True - visited
        False - not visited
    """

    def __init__(self, index):
        self.index = index
        self.nears = [[index[0]+1, index[1]], [index[0]-1, index[1]], [index[0], index[1]+1], [index[0], index[1]-1]]
        self.visit = False
    
    def __repr__(self):
        return f'Node {{index: {self.index}, nears: {self.nears}, visit: {self.visit}}}'

def main():
    input = sys.stdin.readline
    
    h, w = map(int, input().split())
    
    # padding with '#'
    c = np.pad([list(input().strip()) for _ in range(h)], 1, 'constant', constant_values='#')
    
    stack = deque()
    nodes = []
    
    for i in range(h+2):
        nodes.append([])
        for j in range(w+2):
            nodes[i].append(Node([i, j]))
            
            # if you find start, make the "visit" True and add this to stack
            if c[i][j] == 's':
                stack.append(nodes[i][j])
                nodes[i][j].visit = True
    
    # DFS
    # until the stack is empty
    while stack:
        # pop() -> DFS
        # popleft() -> BFS
        node = stack.pop()
        
        # take out adjacent nodes and examine them one by one
        nears = node.nears
        for near in nears:
            # if you haven't visited before, examine this if it's road or wall
            if nodes[near[0]][near[1]].visit == False:
                if c[near[0]][near[1]] == '.':
                    nodes[near[0]][near[1]].visit = True
                    stack.append(nodes[near[0]][near[1]])
                elif c[near[0]][near[1]] == 'g':
                    print('Yes')
                    exit()
    
    print('No')

if __name__ == '__main__':
    main()
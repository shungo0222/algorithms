# Breadth First Search with queue
# AtCoder Beginner Content 168 - D ..(Double Dots)
# https://atcoder.jp/contests/abc168/tasks/abc168_d

import sys
from collections import deque

class Node(object):
    """
    Class of node

    Parameters
    ----------
    index : int
        the location of node
    nears : list
        the list of adjacent nodes
    visit : int
        -1 - initial value
        others - the index of the room where the road sign points
    """
    
    def __init__(self, index, nears):
        self.index = index
        self.nears = nears
        self.visit = -1
    
    def __repr__(self):
        return f'Node {{index: {self.index}, nears: {self.nears}, visit: {self.visit}}}'

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    # get the adjacent node indices
    r = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        r[a-1].append(b-1)
        r[b-1].append(a-1)
    
    # make instances from class
    nodes = []
    for i in range(n):
        nodes.append(Node(i, r[i]))
    
    # add the start position to queue
    queue = deque()
    queue.append(nodes[0])
    nodes[0].visit = 0
    
    # BFS
    # until the queue is empty
    while queue:
        # pop() -> DFS
        # popleft() -> BFS
        node = queue.popleft()
        
        # take out adjacent nodes and examine them one by one
        nears = node.nears
        for near in nears:
            # if you haven't visited before, 
            # save the index of the previous room and add this to queue
            if nodes[near].visit == -1:
                nodes[near].visit = node.index
                queue.append(nodes[near])
    
    ans = []
    for i in nodes[1:]:
        if i.visit != -1:
            ans.append(i.visit + 1)
        else:
            print('No')
            exit()
    
    print('Yes')
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
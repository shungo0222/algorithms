# https://www.geeksforgeeks.org/topological-sorting/
# https://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/
# https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/

# O(V+E)

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

class DAG(object):
    """
    Graph is represented using adjacency list. Every
    node of adjacency list contains vertex number of
    the vertex to which edge connects. It also contains
    weight of the edge
    
    Parameters
    ----------
    V : int
        number of vertices
    graph : dict
        dictionary containing adjacency list
    topological_sort : list
        sorted vertices list by topological sort
    """
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.topological_sort = []
    
    def addEdge(self, u, v, w):
        """
        function to add an edge to graph
        
        Parameters
        ----------
        u : int
            start point
        v : int
            end point
        w : int or float
            weight
        """
        self.graph[u].append((v, w))
    
    def _topologicalSortUtil(self, v, visited, calculated, stack):
        """A recursive function used by topologicalSort"""
        
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                # visiting the uncalculated vertices twice means that there is a loop
                if visited[node] and not calculated[node]:
                    return -1
                
                if not visited[node]:
                    if self._topologicalSortUtil(node, visited, calculated, stack) == -1:
                        return -1
        
        calculated[v] = True
        
        # Push current vertex to stack which stores result
        stack.append(v)
        
        return None
    
    def topologicalSort(self):
        """
        The function to do Topological Sort. It uses recursive
        _topologicalSortUtil()
        """
        
        # Mark all the vertices as not visited
        visited = [False] * self.V
        
        # Mark all the vertices as not calculated
        calculated = [False] * self.V
        
        # sorted vertices
        stack = []
        
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                if self._topologicalSortUtil(i, visited, calculated, stack) == -1:
                    return -1
        
        # store list in reverse order
        self.topological_sort = stack[::-1]
        
        return None
    
    def getTopologicalSort(self):
        if not self.topological_sort:
            if self.topologicalSort() == -1:
                return 'There is a loop!!'
        
        return self.topological_sort
    
    def shortestPath(self, s):
        """The function to find shortest paths from given vertex"""
        if not self.topological_sort:
            if self.topologicalSort() == -1:
                return 'There is a loop!!'
        
        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float('inf')] * self.V
        dist[s] = 0
        
        # Process vertices in topological order
        flag = False
        for i in self.topological_sort:
            if i == s:
                flag = True
            if flag:
                # Update distances of all adjacent vertices
                for node, weight in self.graph[i]:
                    if dist[node] > dist[i] + weight:
                        dist[node] = dist[i] + weight
        
        return dist
    
    def longestPath(self, s):
        """The function to find longest paths from given vertex"""
        if not self.topological_sort:
            if self.topologicalSort() == -1:
                return 'There is a loop!!'
        
        # Initialize distances to all vertices as minus infinite and
        # distance to source as 0
        dist = [-float('inf')] * self.V
        dist[s] = 0
        
        # Process vertices in topological order
        flag = False
        for i in self.topological_sort:
            if i == s:
                flag = True
            if flag:
                # Update distances of all adjacent vertices
                for node, weight in self.graph[i]:
                    if dist[node] < dist[i] + weight:
                        dist[node] = dist[i] + weight
        
        return dist

def main():
    a = DAG(6)
    a.addEdge(0, 1, 5)
    a.addEdge(0, 2, 3)
    a.addEdge(1, 3, 6)
    a.addEdge(1, 2, 2)
    a.addEdge(2, 4, 4)
    a.addEdge(2, 5, 2)
    a.addEdge(2, 3, 7)
    a.addEdge(3, 4, -1)
    a.addEdge(4, 5, -2)
    
    b = DAG(6)
    b.addEdge(0, 1, 5)
    b.addEdge(0, 2, 3)
    b.addEdge(1, 3, 6)
    b.addEdge(1, 2, 2)
    b.addEdge(2, 4, 4)
    b.addEdge(2, 5, 2)
    b.addEdge(2, 3, 7)
    b.addEdge(3, 5, 1)
    b.addEdge(3, 4, -1)
    b.addEdge(4, 5, -2)
    
    s = 1
    
    print(f'start point: {s}')
    print(f'shortest path: {a.shortestPath(s)}')
    print(f'longest path: {b.longestPath(s)}')

if __name__ == '__main__':
    main()
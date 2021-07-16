# https://www.geeksforgeeks.org/topological-sorting/

# O(V+E)

from collections import defaultdict

class DAG(object):
    """
    Class to represent a graph
    
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
    
    def addEdge(self, u, v):
        """
        function to add an edge to graph
        
        Parameters
        ----------
        u : int
            start point
        v : int
            end point
        """
        self.graph[u].append(v)
    
    def _topologicalSortUtil(self, v, visited, stack):
        """A recursive function used by topologicalSort"""
        
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for i in self.graph[v]:
                if not visited[i]:
                    self._topologicalSortUtil(i, visited, stack)
        
        # Push current vertex to stack which stores result
        stack.append(v)
    
    def topologicalSort(self):
        """
        The function to do Topological Sort. It uses recursive
        _topologicalSortUtil()
        """
        
        if self.topological_sort:
            return self.topological_sort
        
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []
        
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self._topologicalSortUtil(i, visited, stack)
        
        self.topological_sort = stack[::-1]
        
        return self.topological_sort

def main():
    g = DAG(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    
    print(f'topological sort: {g.topologicalSort()}')

if __name__ == '__main__':
    main()
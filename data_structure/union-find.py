from collections import defaultdict

class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n+1)]
        
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return None
        
        if self.parents[x] < self.parents[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_all_groups(self):
        all_groups = defaultdict(list)
        for i in range(self.n + 1):
            all_groups[self.find(i)].append(i)
        return dict(all_groups)
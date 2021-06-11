class Cumsum(object):
    """
    cumsum
    
    Parameters
    ----------
    x : list
        the original list
    c : list
        the cumsum of x
    """
    
    def __init__(self, x):
        self.x = x
        self.c = self._make_cumsum()
    
    def _make_cumsum(self):
        c = [0] * (len(self.x)+1)
    
        for i in range(len(self.x)):
            c[i+1] = c[i] + self.x[i]
        
        return c
    
    def get_sum(self, left, right):
        return (self.c[right] - self.c[left])



class Cumsum2D(object):
    """
    2 dim cumsum
    
    Parameters
    ----------
    matrix : list
        the original matrix
    c : list
        the cumsum of matrix
    """
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.c = self._make_cumsum()
    
    def _make_cumsum(self):
        row, col = len(self.matrix), len(self.matrix[0])
    
        c = [[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                c[i+1][j+1] = c[i][j+1] + c[i+1][j] - c[i][j] + self.matrix[i][j]

        return c
    
    def get_sum(self, row_index, col_index):
        return self.c[row_index[1]][col_index[1]] - self.c[row_index[1]][col_index[0]] \
                - self.c[row_index[0]][col_index[1]] + self.c[row_index[0]][col_index[0]]
    
    def show_cumsum(self):
        print('='*20)
        print('Cumsum')
        print('[', end='')
        print(*self.c, sep=',\n', end='')
        print(']')
        print('='*20)
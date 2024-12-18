class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def update(self, i, det):
        i += 1
        while i <= self.size:
            self.tree[i] += det
            i += i & -i
    def query(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result
    def query_range(self, left, right):
        return self.query(right) - self.query(left - 1)

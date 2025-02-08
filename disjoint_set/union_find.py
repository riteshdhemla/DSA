#Time Complexity O(n)
#Space Complexity O(n)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        x , p_x = x, self.parent[x] 
        while p_x != x:
            p_x, x = self.parent[p_x], p_x
        return p_x
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        self.parent[parent_x] = min(parent_x, parent_y)
        self.parent[parent_y] = min(parent_x, parent_y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Time Complexity O(alpha(n)), alpha(n) is inverse Ackermann function
# Space complexity O(n)
class UnionFindByPathCompression:
    def __init__(self, n):
        self.parent: list[int] = list(range(n))
        self.rank = [1] * n
    
    def findByCompression(self, x):
        if x != self.parent[x]:
            self.parent[x] = \
                self.findByCompression(self.parent[x])
        return self.parent[x]

    def unionByRank(self, x, y):
        parent_x = self.findByCompression(x)
        parent_y = self.findByCompression(y)

        if parent_x == parent_y:
            return
        
        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_y] += 1
        

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# for graph operations use union find from networkx library
# import networkx as nx

# uf = nx.utils.UnionFind()
# uf.union(1, 3)
# uf.union(2, 3)
# assert uf[1] == uf[2]

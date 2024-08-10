"""
Also known as fenwick tree
Purpose : Calculate prefix sum efficiently, O(log n), which can be modified to calculate range query sum efficiently.

APIs: 
construct(arr, n): construct fenwick tree of length n.  
sum(idx): return sum from index 0 to specific index idx. 
update(index, val) : update value in array, and fenwick tree at index with value val.
"""

class FenwickTree:
    def __init__(self, lst):
        self.n = len(lst)
        self.ft = [0] * (self.n + 1)
        self.lst = lst
        self.__construct()

    def __construct(self,):
        for i, num in enumerate(self.lst):
            c_idx = i + 1
            while c_idx <= self.n:
                self.ft[c_idx] += num
                c_idx = c_idx + (c_idx & (-c_idx))

    def sum(self, index):
        c_idx = index + 1
        total_sum = 0
        while c_idx > 0:
            total_sum += self.ft[c_idx]
            c_idx = c_idx - (c_idx & (-c_idx))
        return total_sum

    def update(self, index, value):
        diff = value - self.lst[index]
        c_idx = index + 1
        while c_idx <= self.n:
            self.ft[c_idx] += diff
            c_idx = c_idx + (c_idx & (-c_idx))
        self.lst[index] = value



arr = [10, 120, 50, 60, 70]
fen_tree = FenwickTree(lst = arr,)
print(fen_tree.ft)
assert fen_tree.sum(index = 2) == 180
fen_tree.update(index=1, value=20)
print(fen_tree.ft)
assert fen_tree.sum(index = 2) == 80
fen_tree.update(index=2, value=90)
print(fen_tree.ft)
assert fen_tree.sum(index = 2) == 120

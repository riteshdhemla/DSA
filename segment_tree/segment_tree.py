
INT_MAX = 1000000007
INT_MIN = -1000000007

def operation(val1, val2, op = ""):
    if op == "min":
        return min(val1, val2)
    elif op == "max":
        return max(val1, val2)
    elif op == "sum":
        return val1 + val2
    else:
        raise NotImplementedError

class SegmentTree:
    def __init__(self, lst: list[int], op = "min"):
        """
        Construct segment tree from a given input list
        n is size of input lst.
        Time Complexity : O(n)
        """
        self.lst_start = 0
        self.lst_end = len(lst) - 1
        self.st = [0] * 4 * len(lst)  # 2 * 2 * lower_bound(logbase2 n) - 1
        self.lst = lst 
        self.op = op
        self.__construct(self.lst_start, self.lst_end, 0)
        self.return_val = {
            "min" : INT_MAX,
            "max" : INT_MIN,
            "sum" : 0,
        }
        
    def __construct(self, start:int, end:int, index:int,):
        # print(f"cst({start}, {end}, {idx})")
        if start == end:
            self.st[index] = self.lst[start]
            return self.st[index]
        mid = int((start + end)/2)        
        self.st[index] = operation(
                        self.__construct(start, mid, 2*index + 1), 
                        self.__construct(mid+1, end, 2*index + 2),
                        op = self.op,
                    )
        return self.st[index]
    
    def __update_helper(self, s_start:int, s_end:int, index:int, value:int, c_idx:int):
        if index < s_start or index > s_end:
            return self.st[c_idx]
        
        if index == s_start and index == s_end:
            self.st[c_idx] = value
            return self.st[c_idx]
        
        if s_start < s_end:
            mid = s_start + int((s_end - s_start) / 2)
            # call both sides the above condition will terminate if index goes out of range
            self.st[c_idx] = operation(
                self.__update_helper(s_start, mid, index, value, 2*c_idx + 1),
                self.__update_helper(mid + 1, s_end, index, value, 2*c_idx + 2),
                op=self.op,
            )

        return self.st[c_idx]



    def update(self, index:int, value:int):
        """
        Update value at index with value.
        Time Complexity : O(log n)
        """
        # for sum operation
        self.__update_helper(s_start=self.lst_start, s_end=self.lst_end, index=index, value=value, c_idx = 0)
        self.lst[index] = value
        

    def __query_helper(self, s_start:int, s_end:int, q_start:int, q_end:int, c_idx:int = 0):
        """
        c_idx represent the node in the segment tree which root of the node which contains precomputed values for input array indexes (s_start, s_end)
        s_start represent the start index of range of array
        s_end represent the end index of range of array 
        q_start represent the array index which start of query range (inclusive)
        q_end represents the array index which end of query range (inclusive)
        Time Complexity : O(log n)
        """ 
        print(f"query({s_start}, {s_end}, {q_start}, {q_end}, {c_idx})")
        if (s_start >= q_start) and (q_end >= s_end): # selection of node value, if representative segment is completely within query range
            return self.st[c_idx]
        
        if s_start > q_end or q_start > s_end:
            return self.return_val[self.op]
        mid = s_start + int((s_end - s_start) / 2)
        return operation(
                self.__query_helper(s_start, mid, q_start, q_end, c_idx =2*c_idx + 1),
                self.__query_helper(mid+1, s_end, q_start, q_end, c_idx =2*c_idx + 2), 
                op=self.op
                )
        
        

    def query(self, q_start:int, q_end:int,):
        """
        Return value of operation from q_start to q_end
        Time Complexity : O(log n)
        """
        if q_start < 0 or q_end > self.lst_end:
            print(f"Index out of range, query range must be within ({self.lst_start}, {self.lst_end})")
            return
        if q_start > q_end:
            print(f"start index {q_start} for query can not be greater than end index {q_end}")
        
        return self.__query_helper(self.lst_start, self.lst_end, q_start=q_start, q_end=q_end, c_idx=0)
        
        


arr = [10, 120, 50, 60, ]
seg_tree = SegmentTree(lst = arr, op="min")
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 50
seg_tree.update(index=1, value=20)
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 20

arr = [10, 120, 50, 60, 70]
seg_tree = SegmentTree(lst = arr, op="sum")
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 230
seg_tree.update(index=1, value=20)
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 130
seg_tree.update(index=2, value=90)
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 170

arr = [10, 120, 50, 60, ]
seg_tree = SegmentTree(lst = arr, op="max")
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 120
seg_tree.update(index=1, value=20)
print(seg_tree.st)
assert seg_tree.query(q_start = 1, q_end = 3) == 60

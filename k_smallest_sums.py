from collections import deque
from random import random
#base case for float: cant float past the root

#base case for sink: can't sink past the first leaf which is harder to identify so instead we substitute with 
# equivalent base case of current_idx must be either a node or leaf in the tree so that we stop if we overshoot
# instead of stopping when destination is hit. if n is even n / 2 gives left endpoint of split with x - 1 elements to left
# and x elements to the right and if n is odd n / 2 gives middle endpoint with x elements to the left and x elements to the right
# and since a "full" tree will always have x - 1 nodes and x leaves if n = 2x - 1 if we had a "full" tree I think the < n / 2 
# threshold would work

class min_heap:
    def __init__(self):
        self.underlying = [None]
    
    def parent(self, child_idx):
        if child_idx == 1:
            return -1
        return child_idx // 2
    
    def first_child(self, parent_idx):
        return 2 * parent_idx
    
    def swap(self, idx_1, idx_2):
        temp = self.underlying[idx_1]
        self.underlying[idx_1] = self.underlying[idx_2]
        self.underlying[idx_2] = temp


    def float(self, current_idx, compare_to):
        if current_idx > 1:
            parent_idx = self.parent(current_idx)
            if compare_to(self.underlying[parent_idx], self.underlying[current_idx]) > 0:
                self.swap(parent_idx, current_idx)
                self.float(parent_idx, compare_to)



    def sink(self, current_idx, compare_to):
        min_idx = current_idx
        child_start = self.first_child(current_idx)

        for i in range(2):
            child_idx = child_start + i
            if child_idx < len(self.underlying):
                if compare_to(self.underlying[child_idx], self.underlying[min_idx]) < 0:
                    min_idx = child_idx

        if min_idx != current_idx:
            self.swap(current_idx, min_idx)
            self.sink(min_idx, compare_to)

    def is_empty(self):
        return self.underlying[len(self.underlying) - 1] is None

    def insert(self, item, compare_to):
        self.underlying.append(item)
        self.float(len(self.underlying) - 1, compare_to)

    def delete_min(self, compare_to):
        if self.is_empty() != True:
            if len(self.underlying) - 1 > 1:
                min = self.underlying[1]
                self.underlying[1] = self.underlying.pop()
                self.sink(1, compare_to)
                return min
            else:
                min = self.underlying.pop()
                return min

        
    def heap_from(self, items, compare_to):
        for i in range(len(items)):
            self.underlying.append(items[i])

        for node_idx in range((len(self.underlying) - 1) // 2, 0, -1):
            self.sink(node_idx, compare_to)

    def show_by_level(self):
        queue = deque()
        queue.append(1)
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current = queue.popleft()
                print(f"{self.underlying[current]}", end= ",")
                child_start = self.first_child(current)
                for j in range(2):
                    child_idx = child_start + j
                    if child_idx < len(self.underlying):
                        queue.append(child_idx)
            print("\n")


def test_heap():
    def compare_to(n1, n2):
        return n1 - n2
    
    items = [8,7,3,2,11,1,6,5,9]

    print(f"items are: {items}\n")

    heap = min_heap()
    heap.heap_from(items, compare_to)
    heap.show_by_level()

    while(heap.is_empty() != True):
        min = heap.delete_min(compare_to)
        print(f"min is: {min}\n")

    another_heap = min_heap()
    for item in items:
        another_heap.insert(item, compare_to)

    another_heap.show_by_level()

    while(another_heap.is_empty() != True):
        min = another_heap.delete_min(compare_to)
        print(f"min is: {min}\n")

    

#test_heap()

class heap_item:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

def compare_heap_item(item_1, item_2):
    return item_1.priority - item_2.priority

def k_smallest_sums(nums_1, nums_2, k):
    
    result = []
    heap = min_heap()
    heap.insert(heap_item([0, 0], nums_1[0] + nums_2[0]), compare_heap_item)
    inserted = {0: [False] * (k + 1)}
    inserted.get(0)[0] = True    
    count = 0
    
    while count < k:
        current = heap.delete_min(compare_heap_item)
        result.append([nums_1[current.value[0]], nums_2[current.value[1]]])
        count += 1
        for i in range(0, 2):
            next = current.value.copy()
            next[i] = next[i] + 1
            if next[0] < len(nums_1) and next[1] < len(nums_2):
                if inserted.get(next[0]) is None:
                    inserted[next[0]] = [False] * (k + 1)
                    heap.insert(heap_item(next, nums_1[next[0]] + nums_2[next[1]]), compare_heap_item)
                    inserted.get(next[0])[next[1]] = True
    
                if inserted.get(next[0])[next[1]] != True:
                    print(f"next_0 is {next[0]}\n")
                    print(f"next_1 is {next[1]}\n")
    
                    heap.insert(heap_item(next, nums_1[next[0]] + nums_2[next[1]]), compare_heap_item)
                    inserted.get(next[0])[next[1]] = True


    return result

def test_k_smallest_sums():
    #nums_1 = [1,7,11]
    #nums_2 = [2,4,6]

    nums_1 = [1,1,2]
    nums_2 = [1,2,3]

    result = k_smallest_sums(nums_1, nums_2, 2)
    print(f"the smallest sum pairs (u, v) are: {result}\n")

test_k_smallest_sums()

    
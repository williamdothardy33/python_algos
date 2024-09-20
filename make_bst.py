from collections import deque

class node(object):
    def __init__(self) -> None:
        self.value = None
        self.left = None
        self.right = None
    
def bst_from(nums, start, end):
    if start == end:
        leaf = node()
        leaf.value = nums[start]
        return leaf
    if start < end:
        tree_node = node()
        mid = int((start + end) / 2)
        tree_node.value = nums[mid]
        tree_node.left = bst_from(nums, start, mid - 1)
        tree_node.right = bst_from(nums, mid + 1, end)
        return tree_node

def print_bst(bst):
    level = 0
    queue = deque()
    queue.append(bst)
    level_count = 1

    while len(queue) != 0:
        for i in range(level_count):
            current = queue.popleft()
            level_count -= 1
            if current is not None:
                print(f"for level {level} the value is {current.value}\n")
                queue.append(current.left)
                queue.append(current.right)
                level_count += 2
            else:
                print(f"for level {level} the value is {current}\n")

        level += 1

    




def test_bst_from():
    nums = [-10, -3, 0, 5, 9]
    result = bst_from(nums, 0, len(nums) - 1)
    print(f"{result}\n")
    #print_bst(result)

test_bst_from()    


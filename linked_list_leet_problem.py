import threading
class node:
    def __init__(self, val = None, next = None) -> None:
        self.val = val
        self.next = next

def traverse(ns_head, last_offset):
    print(f"t(h, l) = t({ns_head.val if ns_head else ns_head}, {last_offset})\n")
    if last_offset == 0:
        return ns_head
    else:
        split_offset = int(last_offset / 2)
        last_left_node = traverse(ns_head, split_offset)
        if last_left_node is not None:
            print(f"the value at the current node is: {last_left_node.val}\n")
            last_right_node = traverse(last_left_node.next, last_offset - split_offset)
# call trace:
#1)    t(h, 4) 
#2) -> t(h, 2), t(h.next, 2) 
#3) -> t(h, 1) -> returns last_left_node = None, t(h.next, 1) 
#4) -> t(h, 0) -> h, t(h.next, 1) -> (h.next, (h.next.next, (h.next.next.next, (h.next.next.next.next, h.next.next.next.next.next))))
#  
#5) -> t(h.next, 0) -> h.next, t(h.next.next, 1) -> (h.next.next, (h.next.next.next, (h.next.next.next.next, h.next.next.next.next.next))) 
#6) -> t(h.next.next, 0) -> h.next.next, t(h.next.next.next, 1) -> (h.next.next.next, (h.next.next.next.next, h.next.next.next.next.next)) 
#7) -> t(h.next.next.next, 0) -> h.next.next.next, t(h.next.next.next.next, 1) ->  (h.next.next.next.next, h.next.next.next.next.next)
#8) -> t(h.next.next.next.next, 0) -> h.next.next.next.next, t(h.next.next.next.next.next, 1) -> h.next.next.next.next.next (7) <- (8)
#9) -> t(h.next.next.next.next.next, 0) -> h.next.next.next.next.next (8) <- (9)

def test_traverse():
    ns_head = node(-1, node(5, node(3, node(4, node(0, None)))))
    last_offset = 4
    traverse(ns_head, last_offset)
    #ns_length = 1

    # for i in range(0, 18):
    #     current = ns_head
    #     while current.next is not None:
    #         current = current.next
    #     current.next = node(i, None)
    #     ns_length += 1
    #     traverse(ns_head, ns_length)
    #     print("\n")

#test_traverse()

def traverse_v2(ns_head, start_offset, end_offset):
    #print(f"t(h, s, e) = t({ns_head.val if ns_head else ns_head}, {start_offset}, {end_offset})\n")
    if start_offset == end_offset:
        return ns_head
    else:
        split_offset = int((start_offset + end_offset) / 2)
        #print(f"t(head, start, split) is ({ns_head.val if ns_head else ns_head}, {start_offset}, {split_offset})\n")
        last_left_node = traverse_v2(ns_head, start_offset, split_offset)
        if last_left_node is not None:
            print(f"the value at the current node is: {last_left_node.val}\n")
            #print(f"t(head, split + 1, end) is ({last_left_node.next.val if last_left_node.next else last_left_node.next}, {split_offset + 1}, {end_offset})\n")

            last_right_node = traverse_v2(last_left_node.next, split_offset + 1, end_offset)
            return last_right_node
        return last_left_node
    
def split(head):
        lead = head
        lag = head
        while lead is not None and lead.next is not None:
            lead = lead.next.next
            if lead is not None:
                lag = lag.next

        right = lag.next #grab handle to the right of the lag in the original list
        lag.next = None #disconnect original list up to lag from the rest of the list
        return right

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.val <= right.val:
        left.next = merge(left.next, right)
        return left
    else:
        right.next = merge(left, right.next)
        return right
    
def merge_sort(head):
    if head is None or head.next is None:
        return head
    else:
        rest = split(head)
        left = merge_sort(head)
        right = merge_sort(rest)
        return merge(left, right)

    


            
                
        

def test_merge_sort():
    head = node(-1, node(5, node(3, node(4, node(0, None)))))
    head = merge_sort(head)
    current = head
    while current:
        print(f"the current value is {current.val}\n")
        current = current.next

test_merge_sort()

def test_traverse_v2():
    #ns_head = node(-1, node(5, node(3, node(4, node(0, None)))))
    #last_offset = 
    #traverse_v2(ns_head, 0, last_offset + 1)

    ns_head = node(-1, None)
    ns_length = 1

    for i in range(0, 18):
        current = ns_head
        while current.next is not None:
            current = current.next
        current.next = node(i, None)
        ns_length += 1
        traverse_v2(ns_head, 0, ns_length)
        print("\n")

#test_traverse_v2()
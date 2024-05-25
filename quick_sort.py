import random
import time


def swap(ns, pivot_1, pivot_2):
    temp = ns[pivot_1]
    ns[pivot_1] = ns[pivot_2]
    ns[pivot_2] = temp

def partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer = 0):
    if ns[left_pointer] < ns[pivot_index] and left_pointer < last_idx:
        return partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer + 1)
    elif ns[right_pointer] > ns[pivot_index] and right_pointer > 0:
        return partition_recur(ns, last_idx, pivot_index, right_pointer - 1, left_pointer)
    elif left_pointer >= right_pointer:        
        print()
        print('final swap')
        print(f'swapped (i, n): ({left_pointer}, {ns[left_pointer]}) with: ({pivot_index}, {ns[pivot_index]})')
        swap(ns, left_pointer, pivot_index)
        print(f'result: {ns}')
        print()
        return left_pointer
    else:
        print()
        print(f'swapped (i, n): ({left_pointer},{ns[left_pointer]}) with: ({right_pointer}, {ns[right_pointer]})')
        swap(ns, left_pointer, right_pointer)
        
        print(f'result: {ns}')
        print()
        return partition_recur(ns, last_idx, last_idx, right_pointer - 1, left_pointer + 1)
    




def partition_iter(ns, end_idx, right_pointer, left_pointer = 0):
    #left_pointer = 0
    #end_idx = len(ns) - 1
    #right_pointer = end_idx - 1
    pivot_index = end_idx
    while left_pointer <= end_idx and right_pointer >= 0:
        if ns[left_pointer] < ns[pivot_index] and left_pointer < end_idx:
            left_pointer += 1
        elif ns[right_pointer] > ns[pivot_index] and right_pointer > 0:
            right_pointer -= 1
        elif left_pointer >= right_pointer:
            # print()
            # print('final swap')
            # print(f'left pointer is: {left_pointer}, and right pointer is {right_pointer}')
            # print(f'swapped (i, n): ({left_pointer}, {ns[left_pointer]}) with: ({pivot_index}, {ns[pivot_index]})')
            # print(f'ns before: {ns}')
            swap(ns, left_pointer, pivot_index)
            # print(f'result: {ns}')
            # print()
            return left_pointer
        else:
            # print()
            # print(f'left point is: {left_pointer}, and right pointer is {right_pointer}')
            # print(f'swapped (i, n): ({left_pointer},{ns[left_pointer]}) with: ({right_pointer}, {ns[right_pointer]})')
            # print(f'ns before: {ns}')
            swap(ns, left_pointer, right_pointer)
            # print(f'result: {ns}')
            # print()
            left_pointer += 1
            right_pointer -= 1



    
        

def test_partition_recur():
    ns = [81,1,23,72,4,5,23]
    #pivot_index = random.choice(range(0, len(ns)))
    last_idx = len(ns) - 1

    print(f'ns: {ns}')
    print(f'(pivot index, pivot value): ({last_idx}, {ns[last_idx]})')

    print()
    partition_recur(ns, last_idx, last_idx, last_idx - 1)
    
    print(f'partitioned ns: {ns}')

#test_partition_recur()

def test_partition_iter():
    #ns = [9,21, 33, 1,3,7,45,81]
    ns = [81,1,23,72,4,5,23]
    #pivot_index = random.choice(range(0, len(ns)))
    end_idx = len(ns) - 1

    print(f'ns: {ns}')
    print(f'(pivot index, pivot value): ({end_idx}, {ns[end_idx]})')
    print()
    partition_iter(ns, end_idx, end_idx - 1)
    print(f'partitioned ns: {ns}')

test_partition_iter()

def quick_sort(ns, start_idx, end_idx):
    print(f'start index: {start_idx}, end index: {end_idx}')
    time.sleep(2)
    if end_idx - start_idx > 1: # it takes log(N) recursive steps to get it to this size
        # there will be 2^N leaves at the end of the call tree and 2^N - 1 nodes
        # partition will only be run on the nodes of the call tree because the leaves have size <= 1.
        # since partition is O(N) at each recursive step we will add the number
        # of steps to get N + 2 (N/2) + 4 (N/4) ...8 * (N/8) +...until we reach size <= 1 which takes approx log(N) steps
        # N(number of steps to reach base case) = NLogN. each 'level' of the call tree will have partition taking approx N
        # steps altogether and there will be approx LogN 'levels' where partition is run
        pivot_point = partition_iter(ns, end_idx, end_idx - 1, start_idx)
        print()
        print(f'pivot point: {pivot_point}')
        print(f'ns after partition: {ns}')
        quick_sort(ns, start_idx, pivot_point - 1)
        quick_sort(ns, pivot_point + 1, end_idx)


def test_quick_sort():
    ns = [10,9,8,7,5,3,2,1,0]
    print(f'ns before sorting: {ns}')
    start_idx = 0
    end_idx = len(ns) - 1
    quick_sort(ns, start_idx, end_idx)
    print(f'ns after sorting: {ns}')

test_quick_sort()

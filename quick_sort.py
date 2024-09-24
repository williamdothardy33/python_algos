import random
import time


def swap(ns, idx_1, idx_2):
    temp = ns[idx_1]
    ns[idx_1] = ns[idx_2]
    ns[idx_2] = temp

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

#the idea is to insert all the values less than the pivot to the left starting from
#the start_idx and when done the in_offset will point to the first value bigger than the
#pivot which you swap with the pivot value and return the offset
def partition_iter_1(ns, start_idx, end_idx):
    in_offset = start_idx
    pivot_offset = end_idx
    for i in range(start_idx, end_idx):
        if ns[i] < ns[pivot_offset]:
            swap(ns, in_offset, i)
            in_offset += 1
    swap(ns, in_offset, pivot_offset)
    return in_offset


#base case of only one element then it's already partitioned
#because of preorder traversal we can be assured that any partition value will find it's partition index within the partition interval
def quick_sort_1(ns, start_idx, end_idx):
    if end_idx > start_idx:
        pivot_idx = partition_iter_1(ns, start_idx, end_idx)
        quick_sort_1(ns, start_idx, pivot_idx - 1)
        quick_sort_1(ns, pivot_idx + 1, end_idx)

def test_quick_sort_1():
    ns = [10,9,8,7,5,3,2,1,0]
    print(f'ns before sorting: {ns}')
    start_idx = 0
    end_idx = len(ns) - 1
    quick_sort_1(ns, start_idx, end_idx)
    print(f'ns after sorting: {ns}')

test_quick_sort_1()


def test_partition_iter_1():
    #ns = [9,21, 33, 1,3,7,45,81]
    ns = [81,1,23,72,4,5,23]
    #pivot_index = random.choice(range(0, len(ns)))
    end_idx = len(ns) - 1

    print(f'ns: {ns}')
    print(f'(pivot index, pivot value): ({end_idx}, {ns[end_idx]})')
    print()
    pivot_index = partition_iter_1(ns, 0, end_idx)
    print(f"partitioned ns: {ns} with pivot index: {pivot_index}\n")

test_partition_iter_1()
    
        

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

#test_partition_iter()

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

def quick_select(ns, start_idx, end_idx, ordinal):
    if end_idx - start_idx > 1:
        pivot_point = partition_iter(ns, end_idx, end_idx - 1, start_idx)
        if pivot_point == ordinal - 1:
            return ns[pivot_point]
        elif pivot_point > ordinal - 1:
            quick_select(ns, start_idx, pivot_point -1, ordinal)
            result = ns[ordinal - 1]
            return result
        else:
            quick_select(ns, pivot_point + 1, end_idx, ordinal)
            result = ns[ordinal - 1]
            return result



def test_quick_sort():
    ns = [10,9,8,7,5,3,2,1,0]
    print(f'ns before sorting: {ns}')
    start_idx = 0
    end_idx = len(ns) - 1
    quick_sort(ns, start_idx, end_idx)
    print(f'ns after sorting: {ns}')

#test_quick_sort()

def test_quick_select():
    ns = [8,5,3,2,1,1,0]
    for o in range(1, len(ns) + 1):
        ordinal_value = quick_select(ns, 0, len(ns) - 1, o)
        print(f'the ordinal-{o} value is: {ordinal_value}')

#test_quick_select()

def product(ns, start_pointer, end_pointer):
    result = 1
    while start_pointer < end_pointer:
        result *= ns[start_pointer]
        start_pointer += 1
    return result

def largest_3product(ns):
    ns_length = len(ns)
    if ns_length < 4:
        result = product(ns, 0, ns_length)
        return result
    else:
        quick_sort(ns, 0, ns_length)
        result = product(ns, ns_length - 3, ns_length)
        return result
    
def missing_number(ns):
    ns_length = len(ns)
    quick_sort(ns, 0, ns_length)
    pointer1 = 0
    pointer2 = 1
    while pointer2 < ns_length:
        current = ns[pointer2]
        next = ns[pointer1]
        if next != current + 1:
            return current + 1
        else:
            pointer1 += 1
            pointer2 += 1

# O(N^2) max

def max_slow(ns):
    ns_length = len(ns)
    if ns_length == 0:
        return None
    if ns_length == 1:
        return ns[0]
    else:
        start = 0
        current_max = ns[start]
        next_pointer = 1
        while start < ns_length:
            if next_pointer >= ns_length:
                start += 1
                next_pointer = start
            elif ns[next_pointer] > current_max:
                current_max = ns[next_pointer]
                next_pointer += 1
            else:
                next_pointer += 1

        return current_max
    
# O(NLogN)
def max_average(ns):
    ns_length = len(ns)
    if ns_length == 0:
        return None
    if ns_length == 1:
        return ns[0]
    else:
        quick_sort(ns, 0, ns_length - 1)
        result = ns[ns_length - 1]
        return result

# O(N)
def max_fast(ns):
    ns_length = len(ns)
    if ns_length == 0:
        return None
    if ns_length == 1:
        return ns[0]
    else:
        pointer = 0
        current_max = ns[0]
        while pointer < ns_length:
            if current_max < ns[pointer]:
                current_max = ns[pointer]
                pointer += 1
            else:
                pointer += 1
        return current_max



def test_max_versions():
    ns = [81,23,21,9,101,37,92]
    result = max_fast(ns)
    print(f'max returned: {result}')

#test_max_versions()


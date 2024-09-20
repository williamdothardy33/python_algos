import math
def recur_test(start, end, level):
    if start < end:
        mid = int((start + end) / 2)
        print(f"for [tree node] at level {level}: (start, end) = ({start}, {end})\n")
        print("\n")
        print(f"for [left child] at level {level + 1}: (start, mid) = ({start}, {mid})\n")
        print("\n")
        print(f"for [right child] at level {level + 1}: (mid + 1, end) = ({mid + 1}, {end})\n")
        print("\n")
        recur_test(start, mid, level + 1)
        recur_test(mid + 1, end, level + 1)

def recur_test_v2(start, end, level):
    if start <= end:
        mid = int((start + end) / 2)
        print(f"for [tree node] at level {level}: (start, end) = ({start}, {end})\n")
        print("\n")
        print(f"for [left child] at level {level + 1}: (start, mid - 1) = ({start}, {mid - 1})\n")
        print("\n")
        print(f"for [right child] at level {level + 1}: (mid + 1, end) = ({mid + 1}, {end})\n")
        print("\n")
        recur_test_v2(start, mid - 1, level + 1)
        recur_test_v2(mid + 1, end, level + 1)


# with the following split scheme. the recursive call tree on the left and right sub-arrays will reduce
# the following 3 cases outside of the base case:

# 1) the left or right sub-array will be of length 1 (start and end are same) since start + end / 2 = start = end
#  this will be a leaf in the recursive call tree and left and right subarray will hit the base case with end < start

# 2) the left or right sub-array will be of length 2 (end is 1 bigger than start) since start + end will be odd, mid will be the left 
# end point (since (x + x + 1) / 2 = (2x + 1) / 2 = 2x/2 + 1/2 = x - (left endpoint))
# the left subarray will hit the base case and the right subarray will hit case for subarray of length 1 yielding a left-leaning
# subtree with the left endpoint as the root of the subtree and the right endpoint as a leaf (right branch)

#3) the left or right subarray will be of length 3 (end is 2 bigger than start) since (x + x + 2) / 2 = (2x + 2) / 2 = x + 1 the mid
# will be one bigger than the left end point (right between left and right) and the left and right subarray will reduces to cases
# of subarray of length 1 yield a subtree with a root node of the mid and to leaves with the start and end values.
#any any case this split scheme looks like a legitimate traversal where every entry in the array is hit exactly once by the midpoint
def recur_test_v4(ns, start, end, level):
    if start <= end:
        mid = int((start + end) / 2)
        recur_test_v4(ns, start, mid - 1, level + 1)
        print(f"(start + end) / 2 = (({start} + {end}) / 2) = mid = {mid} at level {level}\n")
        print("\n")
        recur_test_v4(ns, mid + 1, end, level + 1)

#probably should compute max before using this
def recur_test1(ns, start, end):
    if start >= end:
        return 10**3
    else:
        mid = int((start + end) / 2)
        left = recur_test1(ns, start, mid)
        right = recur_test1(ns, mid + 1, end)
    return min(left, right, ns[mid + 1] - ns[mid])

def run():
    #recur_test_v2(0, 4, 0)
    ns = []
    for i in range (1, 16):
        ns.append(i)
        recur_test_v4(ns, 0, len(ns) - 1, 0)
        print("\n\n")
    #ns = [1,5,8,14,17,21]
    #result = recur_test1(ns, 0, len(ns) - 1)
    #print(f"the result is {result}")

run()
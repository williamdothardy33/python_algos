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
    recur_test(0, 5, 0)
    #ns = [1,5,8,10,11,12,14,17,21]
    ns = [1,5,8,14,17,21]
    result = recur_test1(ns, 0, len(ns) - 1)
    print(f"the result is {result}")

run()
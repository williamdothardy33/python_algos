def binary_search(ns, start, end, key, e = 0):
    mid = int((start + end) / 2)
    if start > end:
        return mid
    elif (key + e) == ns[mid]:
        return mid
    elif (key + e) > ns[mid]:
        return binary_search(ns, mid + 1, end, key, e)
    else:
        return binary_search(ns, start, mid -1, key, e)



def test_right_boundary_search():
    ns = [6,7,7,7,7,9,9,12,13,13,13,14]
    result = binary_search(ns, 0, len(ns) - 1, 13, 0.5)
    print("\n")
    print(f"right boundary search returned: {result}")

test_right_boundary_search()

def test_right_boundary_search():
    ns = [6,7,7,7,7,9,9,12,13,13,13,14]
    result = binary_search(ns, 0, len(ns) - 1, 13, -0.5)
    print("\n")
    print(f"left boundary search returned: {result}")

test_right_boundary_search()
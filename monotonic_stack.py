from stack import stack

def increasing_monotonic_stack(ns):
    increasing_stack = stack()
    increasing_stack.push(ns[0])
    ns_length = len(ns)
    ns_pointer = 1
    sequences = []

    while increasing_stack.is_empty() == False:
        if ns_pointer == ns_length:
            sequences.append(increasing_stack.to_array())
            return sequences
        else:
            current = ns[ns_pointer]
            if current < increasing_stack.peek():
                sequences.append(increasing_stack.to_array())
                while increasing_stack.is_empty() == False and current < increasing_stack.peek():
                    increasing_stack.pop()
                increasing_stack.push(current)
            else:
                increasing_stack.push(current)
        ns_pointer += 1

def decreasing_monotonic_stack(ns):
    decreasing_stack = stack()
    decreasing_stack.push(ns[0])
    ns_length = len(ns)
    ns_pointer = 1
    sequences = []

    while decreasing_stack.is_empty() == False:
        if ns_pointer == ns_length:
            sequences.append(decreasing_stack.to_array())
            return sequences
        else:
            current = ns[ns_pointer]
            if current > decreasing_stack.peek():
                sequences.append(decreasing_stack.to_array())
                while decreasing_stack.is_empty() == False and current > decreasing_stack.peek():
                    decreasing_stack.pop()
                decreasing_stack.push(current)
            else:
                decreasing_stack.push(current)
        ns_pointer += 1

def test_monotonic_stack():
    ns = [71,72,74,75,73,83,33,45,27]
    result = increasing_monotonic_stack(ns)
    print(f'ns is: {ns}')
    print(f'the increasing subsequences of ns is: {result}')

    ns = [71,72,74,75,73,83,33,45,27]
    result = decreasing_monotonic_stack(ns)
    print(f'ns is: {ns}')
    print(f'the decreasing subsequences of ns is: {result}')

test_monotonic_stack()

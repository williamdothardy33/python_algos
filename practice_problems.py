def is_trending_up(ns):
    ns_pointer = 0
    ns_length = len(ns)
    low = ns[0]
    mid = None
    while ns_pointer < ns_length:
        current = ns[ns_pointer]
        if current <= low:
            low = current
        else:
            if mid is not None:
                if current < mid:
                    mid = current
                else:
                    return True
            else:
                mid = current
        ns_pointer += 1
    return False

def greatest_profit(ns):
    ns_pointer = 0
    ns_length = len(ns)
    current_low = ns[0]
    max_profit = 0

    while ns_pointer < ns_length:
        current = ns[ns_pointer]
        print(f'current is: {current}')
        print(f'current low is: {current_low}')
        if current <= current_low:
            current_low = current
        else:
            current_profit = current - current_low
            print(f'the current profit is: {current_profit}')
            if current_profit > max_profit:
                max_profit = current_profit
        ns_pointer += 1

    return max_profit

def greatest_product(ns):
    positive_term = None
    negative_term = None
    positive_product = 0
    negative_product = 0
    ns_pointer = 0
    ns_length = len(ns)
    while ns_pointer < ns_length:
        current = ns[ns_pointer]
        if current >= 0:
            if positive_term is not None:
                current_product = positive_term * current
                if current_product > positive_product:
                    positive_product = current_product
                if current > positive_term:
                    positive_term = current
            else:
                positive_term = current
        else:
            if negative_term is not None:
                current_product = negative_term * current
                if current_product > negative_product:
                    negative_product = current_product
                if current < negative_term:
                    negative_term = current
            else:
                negative_term = current
        ns_pointer += 1
        
    if positive_product > negative_product:
        return positive_product
    else:
        return negative_product
    
def test_greatest_product():
    ns = [5,-10,-6,9,4]
    result = greatest_product(ns)
    print(f'the greatest product of {ns} is {result}')

test_greatest_product()

def test_greatest_profit():
    ns = [10,7,5,8,11,2,6]
    result = greatest_profit(ns)
    print(f'max profit to be made over {len(ns)} days with closing prices {ns} is: {result}')

#test_greatest_profit()



def test_is_trending_up():
    ns = [22,25,21,18,19.6,17,16,20.5]
    print(f'stock prices for the last {len(ns)} days are: {ns}')
    result = is_trending_up(ns)
    print(f'stock prices are trending up: {result}')

#test_is_trending_up()



            
        



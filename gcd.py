#I have to remove factors that n1 and n2 do not share in common
#if n2 cannot divide n1 then you can find factors they share in common by finding factors that n2
#and the remainder r after pulling out the maximum number of groups of size n2 from n1 because if they share a common factor f then f will also
#divide n2 * (maximum number of groups of size n2 from n1) and r since f divides n2 and r (the definition of common factor)
#the gcd must divide both numbers so if we partition for example n1 = n2 * x + r and d is the gcd then d must divide n2 and it also must divide r
#in order for to divide n1.
#so if the check for n2 divides n1 fails we can find the largest value less than n2 after removing the maximum number of groups of size 
# n2 (n1 % n2 = r) and check if r divides n2. keep doing this until
# we find something. since n1 % n2 < n2 and at each recursive step n1 <- n2, and n2 <- n1 % n2 then n1 >= n2 and if n2 doesn't divide n1 ever
# it will converge to 1 since if n = n1 % n2 != 0 then n < n2 at each recursive step.
def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)

def test_gcd():
    n1 = 8
    n2 = 12
    result = gcd(n1, n2)
    print(f"the gcd of {n1} and {n2} is {result}\n")

test_gcd()

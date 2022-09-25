from eulerlib import is_square,primes

(is_sq,sqroot) = is_square(600851475143)
test_primes = primes(sqroot+1)
len_p = len(test_primes)
for i in range(1,len_p+1):
    j = 0 - i
    test_fact = test_primes[j]
    if 600851475143 % test_fact == 0:
        break
answer = test_fact

print(test_fact)


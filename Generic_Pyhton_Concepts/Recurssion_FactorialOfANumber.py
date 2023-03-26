"""
def factorial_iterative(n):
    ans = 1
    for i in range(n):
        ans = ans * (n - i)
    print(ans)
    return ans

print(factorial_iterative(5))
"""
fact = 1
def factorial_recurrsive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recurrsive(n-1)

factorial_recurrsive(5)
print(factorial_recurrsive(5))


def isPrimeNumber(n):
    for i in range(2, n):
        if n%i == 0:
            print("not a prime")
            break
        else:
            print("yes it is prime")
            break

isPrimeNumber(1334)
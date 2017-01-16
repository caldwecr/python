# It pretends to be useful at generating fib sequence

def fib_rec(n, curr = 1, prev = 0):
    if n == 1:
        return [curr]
    else:
        return [curr] + fib_rec(n - 1, curr + prev, curr)

def fib(n):
    i, prev, curr = 0, 0, 1
    result = []
    while i < n:
        i += 1
        result.append(curr)
        next = curr + prev
        prev = curr
        curr = next
    return result

if __name__ == "__main__":
    import sys
    print(fib_rec(int(sys.argv[1])))
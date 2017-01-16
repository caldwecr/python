# It pretends to be useful at generating fib sequence

def fib_rec(n, curr = 1, prev = 0):
    if n == 1:
        return [curr]
    else:
        return [curr] + fib_rec(n - 1, curr + prev, curr)

if __name__ == "__main__":
    import sys
    print(fib_rec(int(sys.argv[1])))
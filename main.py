def fib(n):
    def make_fib_list(n, fib_list):
        i = len(fib_list)
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        if i == n:
            return fib_list[i]
        return make_fib_list(n, fib_list)

    if n <= 1:
        return n
    else:
        return make_fib_list(n, [0, 1])

def bad_fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

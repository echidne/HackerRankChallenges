cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    result =[]
    a,b =0,1
    while len(result)<n:
        result.append(a)
        a,b = b, a+b
    return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
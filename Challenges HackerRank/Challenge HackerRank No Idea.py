with open("test.txt",'r') as f:
    n , m = map(int,f.readline().split())
    integers = list(map(int,f.readline().split()))
    A = set(map(int,f.readline().split()))
    B = set(map(int,f.readline().split()))
    print(sum([1 if el in A else -1 if el in B else 0 for el in integers ]))
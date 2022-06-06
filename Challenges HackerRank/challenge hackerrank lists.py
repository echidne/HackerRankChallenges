if __name__ == '__main__':
    N = int(input())
    liste  = []
    for i in range(N):
        command,*(numbers) = input().split()
        var = tuple(int(i) for i in numbers)
        if command == "print":
            print(liste)
        else:
            exec(f"liste.{command}{var}")
            
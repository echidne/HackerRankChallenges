if __name__ == '__main__':
    height, width = input().split()
    height, width = int(height), int(width)
    txt ='.|.'
    for i in range(1,height,2):
        x = txt*i
        print(x.center(width,'-'))
    print('WELCOME'.center(width,'-'))
    for i in range(height-2,0,-2):
        x = txt*i
        print(x.center(width,'-'))



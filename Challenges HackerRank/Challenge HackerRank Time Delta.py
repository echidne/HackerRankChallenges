from datetime import datetime

def time_delta(t1, t2):
    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(int((date1- date2).total_seconds()))

with open("testtimedelta.txt",'r') as f:
    t = int(f.readline())
    print(t)
    for t_itr in range(t):
        t1 = f.readline().strip()
        print(t1)
        print(datetime.strptime(t1, "%a %d %b %Y"))
        t2 = f.readline()
        print(t2)
        delta= time_delta(t1, t2)
        print(delta)
while True:
    try:
        n = int(input())
        if n == -1:
            break
        dt = []
        Sum = 0
        for i in range(n):
            tmp = input().split(' ')
            Sum += int(tmp[0]) * int(tmp[1]) * int(tmp[2])
            avg = Sum / n
            dt.append(tmp)
        for i in range(n):
            a = int(dt[i][0]) * int(dt[i][1]) * int(dt[i][2])
            if a != avg:
                for j in range(i + 1, n):
                    b = int(dt[j][0]) * int(dt[j][1]) * int(dt[j][2])
                    if a + b - 2 * avg == 0 and a < avg:
                        print("%s took clay from %s." % (dt[j][3], dt[i][3]))
                    elif a + b - 2 * avg == 0 and a > avg:
                        print("%s took clay from %s." % (dt[i][3], dt[j][3]))
                    else:
                        continue
    except:
        break

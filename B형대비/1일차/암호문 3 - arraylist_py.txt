def func(lst, cmd, x):
    global idx

    if cmd == 'I':
        y = int(input_line[idx])
        idx += 1

        insertIdx = x
        for i in range(y):
            k = int(input_line[idx])
            idx += 1
            lst.insert(insertIdx, k)
            insertIdx += 1
    elif cmd == 'D':
        y = int(input_line[idx])
        idx += 1

        for i in range(y):
            lst.pop(x)
    elif cmd == 'A':
        for i in range(x):
            y = input_line[idx]
            idx += 1

            lst.append(y)

for tt in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    Q = int(input())
    input_line = input().split()
    idx = 0

    for i in range(Q):
        cmd = input_line[idx]
        idx += 1

        x = int(input_line[idx])
        idx += 1

        func(lst, cmd, x)

    print(f'#{tt} ', end='')
    for i in range(10):
        print(lst[i], end=' ')
    print()
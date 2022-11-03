n, m, q = map(int, input().split())
R = {x : 0 for x in range(1, n+1)}
datacenter = {x: [1]*m for x in range(1, n+1)}
for i in range(q):
    temp = input().split()

    if temp[0] == "RESET":
        datacenter[int(temp[1])] = [1] * m
        R[int(temp[1])] += 1

    elif temp[0] == "DISABLE":
        datacenter[int(temp[1])][int(temp[2]) - 1] = 0

    elif temp[0] == "GETMAX":
        get_max = -9223372036854775807
        maxim = {}
        for key, items in datacenter.items():
            if R[key] * sum(items) > get_max:
                maxim[R[key] * sum(items)] = key
                get_max = R[key] * sum(items)
        print(maxim[get_max])

    elif temp[0] == "GETMIN":
        get_min = 9223372036854775807
        mixim = {}
        for key, items in datacenter.items():
            if R[key] * sum(items) < get_min:
                mixim[R[key] * sum(items)] = key
                get_min = R[key] * sum(items)
        print(mixim[get_min])

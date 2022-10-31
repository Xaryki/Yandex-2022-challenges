rockets = {}
ans = []
N = int(input())

'''Input Values'''
for _ in range(N):
    info = input().split()
    if info[3] in rockets:
        rockets[str(info[3])].append(info)
    else:
        rockets[str(info[3])] = [info]

'''Sort by time'''
for key, item in rockets.items():
    rockets[key] = sorted(item, key=lambda x: (int(x[0]), int(x[1]), int(x[2])))
'''Summary time in space'''
for key, item in rockets.items():
    temp = 0
    actions = ""
    start_time = 0
    end_time = 0
    for i in range(len(item)):
        actions += item[i][4]
        if item[i][4] == "A":
            start_time = (int(item[i][0]) * 24 * 60 + int(item[i][1]) * 60 + int(item[i][2]))
        elif item[i][4] in "SC":
            end_time = (int(item[i][0]) * 24 * 60 + int(item[i][1]) * 60 + int(item[i][2]))
        if actions in ["ABS", "ABC", "AC"]:
            temp += end_time - start_time
            actions = ""
    ans.append([key, temp])
'''Output'''
ans = sorted(ans, key=lambda x: int(x[0]))
print(ans)
for i in range(len(ans)):
    print(ans[i][1], end=" ")

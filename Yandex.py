lst = []
for _ in range(int(input())):
    txt = input().split(",")
    FCS = len(set(''.join(list(map(",".join, txt[:3])))) - {","})
    date = sum(map(int, "".join(txt[3:5]))) * 64
    second_name = list(txt[0])
    second_name = (ord((second_name[0]).lower()) - 96) * 256
    sun_first_three = date + second_name + FCS
    sum_first_three = hex(date + second_name + FCS)[2::].upper()
    if len(sum_first_three) < 3:
        i = 3 - len(sum_first_three)
        while i > 0:
            sum_first_three += "0"
            i -= 1
        lst.append(sum_first_three)
    elif len(sum_first_three) >= 3:
        sum_first_three = ''.join(reversed(sum_first_three))[:3:][::-1]
        lst.append(sum_first_three)
print(*lst)

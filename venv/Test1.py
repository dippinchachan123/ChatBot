l = [[658, 833],
[259, 78],
[572, 233],
[602, 683],
[378, 871],
[666, 856],
[573, 696],
[60, 479],
[579, 326],
[890, 476],
[780, 723],
[747, 378],
[393, 524],
[189, 475],
[638, 590],
[424, 160],
[16, 75],
[85, 460],
[144, 365]]
print(l)

prime_list = [2, 3, 5, 7, 11]
def prime_Adder():
    length = len(prime_list)
    i = prime_list[length - 1] + 2
    run = True
    while run:
        for y in prime_list:
            if i % y == 0:
                break
            else:
                if y == prime_list[length - 1]:
                    run = False
                    prime_list.append(i)
        i += 2
    return prime_list



def F(l,b):
    target = l*b
    PF = {}

    while (prime_list[-1] < max(l, b)):
        prime_Adder()

    for i in prime_list:
        while True:
            if (target % i == 0):
                target = target / i
                try:
                    PF[i] += 1
                except:
                    PF[i] = 1
            else:
                break

    ans = 1
    for i in PF.keys():
        if (PF[i] % 2) != 0:
            ans = (PF[i] % 2) * i * ans
    return (PF,"   ",ans)

#for i in l:
#    print(F(i[0],i[1]))
print(F(572,233))

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list = []
list_1 = []
n = int(input("Введите число от 3 до 20: "))
if 2 < n < 21:
    h = int(n / 2)
    for i in numbers3[1:h]:
        n_1 = n % numbers3[i]
        if n % numbers3[i] == 0:
            list_1.append(numbers3[i])
        else:
            continue
    for i in range(h):
        for j in range(n):
            g3 = f"{numbers1[i]}{numbers2[j]}"
            if numbers1[i] + numbers2[j] == n and numbers1[i] != numbers2[j]:
                list.append(g3)
            for l in range(len(list_1)):
                if numbers1[i] + numbers2[j] == list_1[l] and numbers1[i] != numbers2[j]:
                    if g3[::-1] not in list:
                        list.append(g3)
    print(f"{n} - {''.join(list)}")
else:
    print(f"{n} - не входит в диапазон от 3 до 20")

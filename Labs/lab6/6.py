dict1 = {
    "яблоко": "malum, pomum, popular",
    "фрукт": "baca, bacca, popum",
    "наказание": "malum, multa"
}
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
k = dict1.get("яблоко") + ", " + dict1.get("фрукт") + ", " + dict1.get("наказание")
k = k.split(", ")
result = dict.fromkeys(k)
for i in result.keys():
    for j in dict1.keys():
        if i in dict1.get(j):
            if i == k[1]:
                s1.append(j)
                result[i] = s1
            elif i == k[2]:
                s2.append(j)
                result[i] = s2
            elif i == k[3]:
                s3.append(j)
                result[i] = s3
            elif i == k[4]:
                s4.append(j)
                result[i] = s4
            elif i == k[5]:
                s5.append(j)
                result[i] = s5
            elif i == k[6]:
                s6.append(j)
                result[i] = s6
            elif i == k[7]:
                s7.append(j)
                result[i] = s7


result_list = sorted((value, key) for (value, key) in result.items())
for e in result_list:
    if e[0] == "malum":
        print(e[0], "-", e[1][0]+",", e[1][1])
    else:
        print(e[0], "-", e[1][0])

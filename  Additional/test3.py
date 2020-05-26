dict1 = {
    "яблоко": "malum, pomum, popular",
    "фрукт": "baca, bacca, popum",
    "наказание": "malum, multa"
}
k = dict1.get("яблоко") + ", " + dict1.get("фрукт") + ", " + dict1.get("наказание")
k = k.split(", ")
result = dict.fromkeys(k, [])
ss = []
for i in result.keys():
    for j in dict1.keys():
        if i in dict1.get(j):
            ss.append(j)
            result[i] = ss

result_list = sorted((value, key) for (value, key) in result.items())
for e in result_list:
    if e[0] == "malum":
        print(e[0], "-", e[1][0]+",", e[1][1])
    else:
        print(e[0], "-", e[1][0])


print(result["Яблоко"])




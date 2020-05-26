precipitation = {
    "Январь": "38мм",
    "Февраль": "29мм",
    "Март": "33мм",
    "Апрель": "36мм",
    "Май": "40мм",
    "Июнь": "61мм",
    "Июль": "77мм",
    "Август": "79мм",
    "Сентябрь": "71мм",
    "Октябрь": "65мм",
    "Ноябрь": "58мм",
    "Декабрь": "49мм",
}

precipitation_sort = sorted(precipitation.items(), key=lambda i: i[1])

for j in precipitation_sort:
    print(j[0], ":", j[1])

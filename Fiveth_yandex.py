def cook(potions_book, potion_info):
    potion = []
    potion_number, potion_ingredients = potion_info
    for ingred in potion_ingredients:
        if potions_book.get(ingred):
            potion += potions_book[ingred]
        else:
            return False
    return potion


book = {1: [1], 2: [2]}
failed = []
for i in range(3, int(input()) + 1):
    count, *ingredients = map(int, input().split())
    info = [i, ingredients]
    res = cook(book, info)
    if res:
        book[i] = res
    else:
        failed.append(info)

k = len(failed)
while not all(x is None for x in failed):
    failed_poutions = failed.copy()
    for i in range(len(failed_poutions)):
        if failed_poutions[i] is not None:
            k -= 1
            res = cook(book, failed_poutions[i])
            if res:
                book[failed_poutions[i][0]] = res
                failed[i] = None
    if k < 0:
        break

for key in book.keys():
    ings = book[key]
    f = ings.count(1)
    s = ings.count(2)
    book[key] = [f, s]

result = ""
q = int(input())
for _ in range(q):
    a, b, number = map(int, input().split())
    if book.get(number):
        ingredients = book[number]
        if ingredients[0] <= a and ingredients[1] <= b:
            result += "1"
        else:
            result += "0"
    else:
        result += "0"
print(result)
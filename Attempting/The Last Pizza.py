n = int(input())

pizzas = []
total = 0
for i in range(n):
    pizza = int(input())
    total += pizza
    pizzas.append(pizza)

for i in pizzas:
    if (total - i) % 2 == 0:
        print("Ja")
        quit()



if total % 2 == 0:
    print("Ja")
else:
    print("Nej")
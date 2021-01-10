import random

price = round(random.uniform(0, 100),2)
print('Цена 1 кг конфет: ', price)
for i in range(1,11):
    print("Стоимость ", i, 'кг: {0:.2f}'.format(i * price))

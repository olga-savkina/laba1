number = int(input("введите число"))
for i in range(1,int(number/2+1)):
      if number%i==0:
          print(i)

print("\n------------------------------------------------------------\n")
spisok=input("введите строку\n")
print(spisok)
words = spisok.split()
counter=1
if len(words)%2 ==0: counter+=1
print("кол-во четных слов",counter)
print(max(spisok.split(),key=len))
print("\n------------------------------------------------------------\n")
spisok=[3,148,-45,75,21,-26,-173,-37,54]
newlist=[int(x) for x in spisok if x%2== 0]
print(newlist)
if len(newlist)!=0:
    print(max(newlist))
else: print(spisok[0])
spisok.sort(reverse=True)
print(spisok)
print("\n------------------------------------------------------------\n")
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=False)[:3]
print(result)
print("\n------------------------------------------------------------\n")
shop = {
   "Кольцо": ["золото", 500, 15],
   "Цепочка": ["серебро", 200, 10],
   "Браслет": ["сталь", 100, 5],
   "Серьги": ["Белое золото", 550, 12]
}

print("Добро пожаловать в ювелирный магазин !\n")
while True:
   print("Меню:")
   print("1. Просмотр описания")
   print("2. Просмотр цены")
   print("3. Просмотр количества")
   print("4. Вся информация")
   print("5. Покупка")
   print("6. До свидания")

   choice = input("\nВыберите пункт меню: ")

   if choice == "1":
       print('Все товары нашего магазина: ')
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

       name = input("\nВведите название изделия: ")
       if name in shop:
           description = shop[name][0]
           print(f"Описание: {description}")
       else:
           print("Такого изделия нет в магазине")

   elif choice == "2":
       print('Все товары нашего магазина: ')
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

       name = input("Введите название изделия: ")
       if name in shop:
           price = shop[name][1]
           print(f"Цена: {price} руб.")
       else:
           print("Такого изделия нет в магазине")

   elif choice == "3":
       print('Все товары нашего магазина: ')
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

       name = input("Введите название изделия: ")
       if name in shop:
           quantity = shop[name][2]
           print(f"Количество: {quantity} шт.")
       else:
           print("Такого изделия нет в магазине")

   elif choice == "4":
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

   elif choice == "5":
       name = input("Введите название изделия (или 'n' для выхода): ")
       if name == "n":
           break
       if name not in shop:
           print("Такого изделия нет в магазине")
           continue
       quantity = int(input("Введите количество: "))
       if quantity > shop[name][2]:
           print("Недостаточно товара на складе")
           continue
       price = shop[name][1] * quantity
       shop[name][2] -= quantity
       print(f"\nВы купили {quantity} шт. {name}.\nСумма покупки: {price} руб.")

   elif choice == "6":
       break

   else:
       print("Неверный пункт меню")
print("\n------------------------------------------------------------\n")
values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)
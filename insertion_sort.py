list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(f'Vamos trabalhar com a seguinte lista {list}')
print('No insertion sort ele separa por tamanho de lista inicial\n')

for i in range(1, len(list)):
    j = i
    while j > 0 and list[j-1] > list[j]:
        list[j], list[j-1] = list[j-1], list[j]
        j -= 1
print(f'A primeira passagem fica {list}')


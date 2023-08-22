list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(f'Vamos trabalhar com a seguinte lista {list}')
print('No selection sort ele separa pelo mínimo valor para a esquerda')

for i in range(len(list)-1):
    minimo = list[0]
    if list[i+1] < minimo:
        minimo = list[i+1]
        list.remove(minimo)
        list.insert(0, minimo)
print(f'A lista com a primeira passagem fica {list}\n')
for i in range(len(list)-1):
    minimo = list[1]
    if list[i+1] < minimo:
        minimo = list[i+1]
        list.remove(minimo)
        list.insert(1, minimo)
print(f'A lista com a segunda passagem fica {list}\n')
for i in range(2, len(list)-1):
    minimo = list[2]
    if list[i+1] < minimo:
        minimo = list[i+1]
    list.remove(minimo)
    list.insert(2, minimo)
print(f'A lista com a terceira passagem fica {list}\n')
for i in range(3, len(list)-1):
    minimo = list[3]
    if list[i+1] < minimo:
        minimo = list[i+1]
    list.remove(minimo)
    list.insert(3, minimo)
print(f'A lista com a quarta passagem fica {list}\n')
for i in range(4, len(list)-1):
    minimo = list[4]
    if list[i+1] < minimo:
        minimo = list[i+1]
    list.remove(minimo)
    list.insert(4, minimo)
print(f'A lista com a quinta passagem fica {list}\n')
for i in range(5, len(list)-1):
    minimo = list[5]
    if list[i+1] < minimo:
        minimo = list[i+1]
    list.remove(minimo)
    list.insert(5, minimo)
print(f'A lista com a sexta passagem fica {list}\n')
for i in range(6, len(list)-1):
    minimo = list[6]
    if list[i+1] < minimo:
        minimo = list[i+1]
    list.remove(minimo)
    list.insert(6, minimo)
print(f'A lista com a sétima passagem fica {list}\n')

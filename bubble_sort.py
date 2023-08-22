print('Vamos trabalhar com a seguinte lista [54, 26, 93, 17, 77, 31, 44, 55, 20]')
print('No bubble sort ele compara dois termos')
list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a primeira passagem {list}\n')
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a segunda passagem {list}\n')
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a terceira passagem {list}\n')
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a quarta passagem {list}\n')
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a quinta passagem {list}\n')
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a sexta passagem {list}\n')
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(f'A lista com a sétima passagem {list}')
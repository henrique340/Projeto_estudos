import os
def Menu():
    print('''1 - Ver os tipos de ordenação
2 - Ver as conversões de base\n''')

def cabecalho(nome):
    print('-'*45)
    print(nome.center(45))
    print('-'*45)

opc = 1
while opc != 0:
    Menu()
    opc = int(input('Digite a opção escolhida: '))
    if opc == 1:
        #os.system('cls')
        cabecalho('Tipos de sort')
        print('''1 - selection sort
2 - bubble sort
3 - insertion sort
4 - merge sort
5 - quick sort
6 - heap sort
7 - counting sort
8 - radix sort 
9 - bucket sort\n''')
        opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            cabecalho('Selection sort')
            list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
            print(f'Vamos trabalhar com a seguinte lista {list}')
            print('No selection sort ele separa pelo mínimo valor para a esquerda')

            for i in range(len(list) - 1):
                minimo = list[0]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                    list.remove(minimo)
                    list.insert(0, minimo)
            print(f'A lista com a primeira passagem fica {list}\n')
            for i in range(len(list) - 1):
                minimo = list[1]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                    list.remove(minimo)
                    list.insert(1, minimo)
            print(f'A lista com a segunda passagem fica {list}\n')
            for i in range(2, len(list) - 1):
                minimo = list[2]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                list.remove(minimo)
                list.insert(2, minimo)
            print(f'A lista com a terceira passagem fica {list}\n')
            for i in range(3, len(list) - 1):
                minimo = list[3]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                list.remove(minimo)
                list.insert(3, minimo)
            print(f'A lista com a quarta passagem fica {list}\n')
            for i in range(4, len(list) - 1):
                minimo = list[4]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                list.remove(minimo)
                list.insert(4, minimo)
            print(f'A lista com a quinta passagem fica {list}\n')
            for i in range(5, len(list) - 1):
                minimo = list[5]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                list.remove(minimo)
                list.insert(5, minimo)
            print(f'A lista com a sexta passagem fica {list}\n')
            for i in range(6, len(list) - 1):
                minimo = list[6]
                if list[i + 1] < minimo:
                    minimo = list[i + 1]
                list.remove(minimo)
                list.insert(6, minimo)
            print(f'A lista com a sétima passagem fica {list}\n')
        elif opcao == 2:
            cabecalho('Bubble Sort')
            list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a primeira passagem {list}\n')
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a segunda passagem {list}\n')
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a terceira passagem {list}\n')
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a quarta passagem {list}\n')
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a quinta passagem {list}\n')
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a sexta passagem {list}\n')
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            print(f'A lista com a sétima passagem {list}')
        elif opcao == 3:
        elif opcao == 4:
        elif opcao == 5:
        elif opcao == 6:
        elif opcao == 7:
        elif opcao == 8:
        elif opcao == 9:
    elif opc == 2:
        cabecalho('Conversão de bases')
        #os.system('cls')
        print('''1 - decimal para binário
2 - decimal para octal
3 - decimal para hexadecimal
4 - binário para decimal
5 - binário para oxtal
6 - binário para hexadecimal
7 - octal para decimal
8 - octal para binário
9 - octal para hexadecimal
10 - hexadecimal para decimal
11 - hexadecimal para binário
12 - hexadecimal para octal''')
        opcao = int(input('Digite a opção escolhida: '))
        if opcao == 1:
        elif opcao == 2:
        elif opcao == 3:
        elif opcao == 4:
        elif opcao == 5:
        elif opcao == 6:
        elif opcao == 7:
        elif opcao == 8:
        elif opcao == 9:
        elif opcao == 10:
        elif opcao == 11:
        elif opcao == 12:
def expresion():
    number = input()
    cal=(pow(3,(int(number))))-1
    return cal

list_ent = range (0,((expresion()+1)))


def verificar_existente(lista,numeros):
    for n3 in lista:
        for n4 in n3:
            if n4 == numeros:
                return True
    return False

def verificar_next(lista):

    list_numbers_ter_verf = []
    for n in lista:
        index_n = lista.index(n)
        if n[0] == 1 or n[1] == 1:
            if not(verificar_existente(list_numbers_ter_verf, n)):
                list_numbers_group = []
                list_numbers_group.append(n)
                for n2 in lista:
                    if lista.index(n2) > index_n:
                        if n2[0] == 1 or n2[1] == 1:
                            if not(verificar_existente(list_numbers_ter_verf,n2)):
                                list_numbers_group.append(n2)
                        else:
                            break
            else:
                continue
            list_numbers_ter_verf.append(list_numbers_group)
        else:
            list_numbers_ter_verf.append(n)
    return list_numbers_ter_verf

def cal_ternario():
    list_number_ter = []

    for numbers in list_ent:
        cociente = numbers / 3
        resto = numbers % 3
        tuple_number_ter = (int(cociente),int(resto))
        list_number_ter.append(tuple_number_ter)

    return list_number_ter


def orden(lista):
    for number in lista:
        for number_2 in number:
            if number_2 != 2:
                return 3
            else:
                return 1

verificar_next(cal_ternario())
print(orden(verificar_next(cal_ternario())))




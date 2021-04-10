def expresion():
    print("Ingrese un Valor  para calcular rango")
    print("")
    number = input()
    cal=(pow(3,(int(number))))-1
    return cal

list_ent = range (0,((expresion()+1)))


def verificar_existente(lista, numeros):

    for i in lista:
        for j in i:
            if j == numeros:
                return True
    return False

def verificar_condicion_1(numbers):
    #Se verifica si el grupo de numeros ternarios cuenta con el numero 1
    if numbers[0] == 1 or numbers[1] == 1:
        return True
    else:
        return False


def lista_agrupados(lista):

    lista_numeros = []

    for numeros in lista:
        if verificar_condicion_1(numeros):
            if (verificar_existente(lista_numeros, numeros)):
                continue
            else:
                lista_condicion_2 = []
                lista_condicion_2.append(numeros)
                for numeros_condicion_2 in lista:
                    if lista.index(numeros_condicion_2) > lista.index(numeros):
                        if verificar_condicion_1(numeros_condicion_2):
                            if (verificar_existente(lista_numeros, numeros_condicion_2)):
                                pass
                            else:
                                lista_condicion_2.append(numeros_condicion_2)
                        else:
                            break
            lista_numeros.append(lista_condicion_2)
        else:
            lista_numeros.append(numeros)
    return lista_numeros

def cal_ternario():
    list_number_ter = []

    for numeros in list_ent:
        cociente = numeros / 3
        resto = numeros % 3
        tuple_number_ter = (int(cociente),int(resto))
        list_number_ter.append(tuple_number_ter)

    return list_number_ter


def numero_enGrupos(lista):

    lista_enGrupos = []
    for numeros in lista:
        if type(numeros) == tuple:
            lista_enGrupos.append(1)
        if type(numeros) == list:
            lista_enGrupos.append(len(numeros))

    return lista_enGrupos

print("Lista de numeros ternarios agrupados")
print(lista_agrupados(cal_ternario()))
print("")
print("Lista de numeros agrupados por tamaño")
print(numero_enGrupos(lista_agrupados(cal_ternario())))




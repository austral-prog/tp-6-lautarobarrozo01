def remove_elements(list_to_remove_elements):
    lista1 = list_to_remove_elements[:]
    longlista1 = len(lista1)
    if longlista1 == 0:
        lista1
    else:
        if longlista1 == 5:
            del lista1[4]
        elif longlista1 < 5:
            lista1
        else:
            del lista1[5]
            del lista1[4]
        del lista1[0]
    return lista1


def add_elements(list_to_add_elements):
    lista2 = list_to_add_elements[:]
    lista2.insert(0,'Pink')
    lista2.append('Yellow')
    return lista2


def is_empty(list_to_check):
    lista3 = list_to_check[:]
    if lista3 == []:
        return True


def check_lists(list_to_compare1, list_to_compare2):
    lista4 = list_to_compare1[:]
    lista5 = list_to_compare2[:]
    longlista4 = len(lista4)
    longlista5 = len(lista5)
    if (longlista4 < 3 or longlista5 < 3):
        return False    
    else:
        lista4_3 = lista4[2]
        lista5_3 = lista5[2]
        if lista4_3 == lista5_3:
            return True
        else:
            return False


def list_of_lists(list_of_lists_to_modify):
    lista6 = list_of_lists_to_modify[:]
    lista6[0] = lista6[0][:2]
    lista6[1] = lista6[1][1:4]
    lista6[2] = lista6[2][-2:]
    return lista6

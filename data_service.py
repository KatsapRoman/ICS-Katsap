""" модуль для доступу до вхідних даних та перегляду даних
"""



def get_dovidnuk():
    """ отримує данні по товарам

    Returns:
        dovidnuk_list : список товарів
    """

    from_file = [
        "1;Масло",
        "2;Сир твердий",
        "3;Молоко",
        "4;Сир",
        "5;Маргарин",
        "6;М'ясо",
        "7;Ковбаса",
        "8;Фарш м'ясний",
        "9;М`ясо кістки",
    ]

    #накопичувач рядків
    dovidnuk_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidnuk_list.append(line_list)
    return dovidnuk_list

def get_pokazn():
    """повертає список накладних

    Returns:
        from_file: список накладних
    """

    from_file = [
        "1;1;23.54;64.56;72.52",
        "2;2;11.72;21.45;21.1",
        "1;3;57.54;87.35;95.59",
        "2;4;31.26;41.26;61.1",
        "1;5;42.48;32.78;52.56",
        "2;6;25.56;65.15;95.96",
        "2;7;31.1;65.86;87.85",
        "1;8;24.25;75.7;79.84",
        "1;9;9.45;21.15;23.62",
        "3;1;15.77;43.26;48.59",
        "3;2;7.85;14.37;14.14",
        "3;3;38.55;58.52;64.05",
        "3;4;20.94;27.64;40.94",
        "3;5;28.46;21.96;35.22",
        "3;6;17.13;43.65;64.29",
        "3;7;20.84;44.13;58.86",
        "3;8;16.25;50.72;53.49",
        "3;9;6.33;14.17;15.83",
    ]

    # розбити строку на реквізити та перетворити формати (при потребі)
    pokazn_list = []    # список-накопичувач
    for line in from_file:
        line_list = line.split(';')
        line_list[2] = float(line_list[2])
        line_list[3] = float(line_list[3])
        line_list[4] = float(line_list[4])
        pokazn_list.append(line_list)

    return pokazn_list

def show_dovidnuk(dovidnuk):
    """виводить список товарів за заданої умови

    Args:
        dovidnuk : сприсок товарів
    """

    dovidnuk_code_from = input("З якого кода товара?")
    dovidnuk_code_to   = input("По який код товара?")
    
    for dovidnuk in dovidnuk():
        if  dovidnuk_code_from  <= dovidnuk[0] <= dovidnuk_code_to:
            print( "код товару: {:4} назва товару: {:18} ".format(dovidnuk[0], dovidnuk[1] ))

def show_pokazn(pokazn):
    """виводить список товарів за заданої умови

    Args:
        pokazn : сприсок товарів
    """

    pokazn_code_from = input("З якого склада товара?")
    pokazn_code_to   = input("По який склад товара?")
    
    for pokazn in pokazn():
        if  pokazn_code_from  <= pokazn[0] <= pokazn_code_to:
            print("номер складу: {:4} код товару: {:10} залишок: {16} прибуток: {22} вибуток: {28}}").format(pokazn[0], pokazn[1], pokazn[2] ,pokazn[3] ,pokazn[4] )

dovidnuk = get_dovidnuk()
for o in dovidnuk:
    print(o)

pokazn = get_pokazn()
for l in pokazn:
    print(l)

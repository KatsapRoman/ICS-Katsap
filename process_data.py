""" Розрахунок заявок на товари по магазину
"""

from data_service import get_dovidnuk, get_pokazn


# структура вихідниз данних 
zajavka = {

    'Number_composition'               : '',     #  номер складу
    'Product_name'                     : '',     #  назва товара
    'Balance_of_beginning_the_month'   : 0.0,    #  залишок на початок місяця
    'Profit'                           : 0.0,    #  прибуток
    'Excess'                           : 0.0,    #  вибуток
    'Balance_at_end_months'            : 0.0     #  залишок на кінець місяця
}

dovidnuk_list = get_dovidnuk()
pokazn_list = get_pokazn()


def create_zajavka_list():
    """ накопичує та повертає список заявок
    """

    def get_dovidnuk_name(dovidnuk_code):
        """ повертає назву клієнтів по його коду

        Args: 

        Retuens:
        """
        for dovidnuk in dovidnuk_list:
            if dovidnuk_code == dovidnuk[0]:
                return dovidnuk[1]

        return "*** назва не знайдена"


    # накопичувач заявок 
    zajavka_list = []

    for pokazn in pokazn_list:

        # створити робосу копію
        zajavka_work = zajavka.copy()

        zajavka_work['Number_composition']               = pokazn[0]
        zajavka_work['Product_name' ]                    = get_dovidnuk_name(pokazn[1])
        zajavka_work['Balance_of_beginning_the_month']   = pokazn[2]
        zajavka_work['Profit']                           = pokazn[3]
        zajavka_work['Excess']                           = pokazn[4]
        zajavka_work['Balance_at_end_months']            = zajavka_work['Profit'] + zajavka_work['Balance_of_beginning_the_month'] - zajavka_work['Excess']


        zajavka_list.append(zajavka_work)
 
    return zajavka_list


z = create_zajavka_list()
for i in z:
    print(i)
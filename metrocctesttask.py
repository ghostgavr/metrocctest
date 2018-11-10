import csv
import random
from datetime import datetime


def getpricelist():
    pricelist = {}
    counter = 1
    with open('pricelist.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        for row in data:
            pricelist[counter] = {'art': row[0], 'product': row[1], 'cost': float(row[2])}
            counter += 1
        return pricelist


def printproductlist():
    for key in pricelist.keys():
        print(key, pricelist[key]['product'], sep='\t')
    while True:
        userinput = input('Выберите товар[1-'+str(len(pricelist.keys()))+']:')
        if userinput.isdigit():
            selectedproduct = int(userinput)
            if 1 < int(selectedproduct) < len(pricelist.keys()):
                print('Вы выбрали:', pricelist[selectedproduct]['product'])
                return int(selectedproduct)
            else:
                print('Неверные данные')
        else:
            print('Неверные данные')


def getweight():
    return round(random.uniform(0.1, 10), 2)


def sendinfo(selectedproduct, productweight):
    barcodenum = createbarcodenum()
    totalcost = round(productweight * pricelist[selectedproduct]['cost'], 2)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if True:
        print("Информация переданна на сервер")
    printlabel("Штрихкод:", barcodenum,
               "Наименование товара:", pricelist[selectedproduct]['product'],
               "Цена кг.:", pricelist[selectedproduct]['cost'],
               "Вес:", productweight,
               "Стооимость:", totalcost,
               "Время упаковки:", time)


def createbarcodenum():
    return random.randint(1000000, 9999999)


def printlabel(*args):
    for i in args:
        print(i)


pricelist = getpricelist()  # получаем актуальные цены из доверенного источника
selectedproduct = printproductlist()  # спрашиваем у пользователя что он взвешивает
productweight = getweight()  # получаем вес товара
sendinfo(selectedproduct, productweight)  # передаем на сервер и печатаям ярлык со штрихкодом

input("Press Enter...")

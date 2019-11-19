import random
outFile = open('outputFile.txt', 'w')
for i in range(1, 101):
    x = True
    y = 1
    nonoList = []
    while x == True:
        IDrand = random.randint(1, 5)
        while True:
            if IDrand in nonoList:
                IDrand = random.randint(1,5)
            else:
                break
        nonoList.append(IDrand)
        Qtyrand = random.randint(1,10)
        outFile.write('INSERT INTO SALES VALUES (')
        outFile.write(str(i))
        outFile.write(", ")
        if i <= 31:
            m = 1
            d = i
        elif i > 31 and i <= 59:
            m = 2
            d = i - 31
        elif i > 59 and i <= 90:
            m = 3
            d = i - 59
        elif i > 90:
            m = 4
            d = i - 90
        outFile.write("'"+str(m)+"/"+str(d)+"/2018"+"', ")
        outFile.write(str(y)+", ")
        outFile.write(str(IDrand) + ", ")
        outFile.write(str(Qtyrand) + ", ")
        PriceUnit = 0
        if IDrand == 1:
            PriceUnit = 4.99
        elif IDrand == 2:
            PriceUnit = 0.99
        elif IDrand == 3:
            PriceUnit = 1.99
        elif IDrand == 4:
            PriceUnit = 7.99
        elif IDrand == 5:
            PriceUnit = 15.00
        price = round(PriceUnit * Qtyrand, 2)
        outFile.write(str(price)+", ")
        salesmanList = [2,3,4,7,13,15]
        salesmanRand = random.randint(0,5)
        outFile.write(str(salesmanList[salesmanRand]))
        outFile.write(");\r\n")
        rand = random.randint(1,3)
        y += 1
        if rand == 1:
            x = True;
        else:
            break



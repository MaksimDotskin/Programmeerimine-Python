numbers =(input("Sisesta mitu komadega eraldatud numbrit: ").split(","))
col=0
product=1
summa=0


for number in numbers:
    number = float(number)
    

    product *= number
    summa+= number
    col += 1

arifm=summa/col
geom=pow(product, 1/col)


print("Korrutis-",product)
print("Summa-",summa)
print("aritmeetiline keskmine-",arifm)
print("geomeetriline keskmine-",geom)

  
while True:
    numbers =(input("Sisesta mitu komadega eraldatud numbrit: ").split(","))
    if numbers.isaplha():
        print("введите цифры")
    else:
        break

    for number in numbers:
        number = float(number)
        print(number)









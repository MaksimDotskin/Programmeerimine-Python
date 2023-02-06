try:
    numbers = input("Sisestage mitu komadega eraldatud numbrit: ").split(",")
    sum = 0
    product = 1
    count = 0

    for number in numbers:
        number = float(number)
        sum += number
        product *= number
        count += 1

    arithmetic_mean = sum/count
    geometric_mean = pow(product, 1/count)

    print("summa:", sum)
    print("aritmeetiline keskmine:", arithmetic_mean)
    print("geomeetriline keskmine:", geometric_mean)
    print("korrutis:", product)
except:
    print("Vale Andmed")
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    my_price=10000
    print("지역버전 = ", my_price)
    return total

my_price = float(input("Enter a price : "))

totalprice = calculateTax(my_price, 0.09)
print("price = ", my_price, "totalprice = ",totalprice)
print("my_price(전역변수) = ", my_price)
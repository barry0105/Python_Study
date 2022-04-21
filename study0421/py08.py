def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total

my_price = float(input("Enter a price : "))

totalprice = calculateTax(my_price, 0.09)
print("price = ", my_price, "totalprice = ",totalprice)
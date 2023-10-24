price = float(input("What is the price of the meal?"))

priceTip = round((price / 100) * 15, 3)
priceTax = round((price / 100) * 21, 3)

total = round(price + priceTip + priceTax, 3)

print("Tax: ", priceTax," , Tip: ",priceTip,", Total: ",total)
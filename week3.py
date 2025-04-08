# Defining function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        selling_price = price * (1 - (discount_percent/100))
        return selling_price
    else:
        return price

#Prompting user and calling function 
price= int(input("Please enter the original price: "))
discount_percent =int(input("Please enter the percent discount: "))
selling_price = calculate_discount(price, discount_percent)
if selling_price < price:
    print(f"The selling price after applying discount is: {selling_price}")
else:
    print(f"There is no discount applied, the selling_price is: {price}")


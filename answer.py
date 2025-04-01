def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final = price - discount_amount
        return final
    else:
        return price

price = float(input("Enter the original price of the item: ksh "))
discount_percent = float(input("Enter the discount percentage: "))
final = calculate_discount(price, discount_percent)
print(f"Final Price after discount: ksh {final:.2f}")

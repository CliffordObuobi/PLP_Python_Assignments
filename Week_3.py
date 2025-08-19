# Declaring a function
def discounted_price(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Taking input and converting to number
original_item_price = float(input("Enter the original price of the item: "))
entered_discount_percentage = float(input("Enter the discount percentage: "))

# Final price calculation
final_calculated_price = discounted_price(original_item_price, entered_discount_percentage)

# Net Price displayed
print(f"The final price after considering the discount is: GHC{final_calculated_price:.2f}")


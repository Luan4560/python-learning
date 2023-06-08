# Write a script that read a price of a product and show
# your new price with 5% discount.

price = float(input('Type product price: '))

result = price - (price * 5 / 100)

print('The price of product with 5% of discount is R${:.2f}'.format(
    float(result)))

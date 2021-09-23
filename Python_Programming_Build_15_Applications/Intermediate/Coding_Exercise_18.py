total = 760
discount = 0
promo_item_bought = True

if total > 500 and total <= 1000:
    discount = 5
elif  promo_item_bought or total > 1000:
    discount = 10
    
discountValue = (total * discount) / 100
tot = total - discountValue

print('Discount : ' + str(discount) + "% OFF -" + str(discountValue))
print('Total : ' + str(tot))
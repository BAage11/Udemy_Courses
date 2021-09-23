total = 870
discount = 0

if total > 500 and total <= 1000:
    discount = 5
elif total > 1000:
    discount = 10
    
discountValue = (total * discount) / 100 
tot = total - discountValue

print('Discount : ' + str(discount) + '% OFF -' + str(discountValue))
print('Total : ' + str(tot))
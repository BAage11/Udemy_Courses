# Use for loop to create uniques list and print it!
lst = [ 'red', 'blue', 'yellow', 'black', 'red', 'blue', 'green', 'black', 'blue']
new_ls = []

for i in lst:
    if i in new_ls:
        continue
    else:
        new_ls.append(i)
    
print(new_ls)
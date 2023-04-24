lst0 = [12,45,-1,22,89,56]
max_item = lst0[0]
for item in lst0:
    if max_item < item:
        max_item = item
print(max_item)
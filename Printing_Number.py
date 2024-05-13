# Printing numbers from 1 to 9, skipping 3, breaking at 7
print("Printing numbers from 1 to 9, skipping 3, breaking at 7:")
for i in range(1, 10):
    if i == 3:
        continue
    print(i)
    if i == 7:
        break

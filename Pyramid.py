blocks = int(input("Input how many blocks has the pyramid: "))
height = 0
layer = 1

while layer <= blocks:
    height += 1
    blocks -= layer
    layer += 1

print(height)
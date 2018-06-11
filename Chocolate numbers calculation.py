# Getting number of boys and girls as input
# Each Boy and girl will share 2 and 3 chocolates resp.
# if total chocolates to boys exceeds 100 nos. give 10% of choc. extra to each boys
# if total chocolates to girls exceeds 100 nos. give 10% of choc. extra to each girl
# Code to find how many chocolates is needed

boys = int(input('no of boys:'))
girls = int(input('no of girls:'))
bc = boys*2
gc = girls*3
print('total boys chocolate', bc); print('t g ch', gc)
if bc > 100:
    bcx = bc * 0.10
    gcx = gc
elif gc > 100:
    gcx = gc * 0.10
    bcx = bc
else:
    bcx = bc; gcx = gc
chocolates = bc + gc + bcx + gcx
print('Total number of chocolates =', chocolates)
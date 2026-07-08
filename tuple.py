tup=(1,2,3,45,6,7)
tup1=()
tup2=()
for i in tup:
    if i%2 == 0 :
        tup1=tup1 +(i,)
    else:
        tup2=tup2 +(i,)

print(f"tuple of even integer{tup1}")
print(f"tuple of odd integer{tup2}")
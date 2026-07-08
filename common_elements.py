# list1 = [1, 2, 3,4] 
# list2 = [3, 4]
# s=set(list1)
# s1=set(list2)
# common = s & s1
# if common == 0:
#     print("There is no common element in the lists")
# else:
#     print(f"There are {common} common element in the lists")

list1 = [1, 2, 3, 4 ,5]
list2 = [5, 6, 7, 8]

common = set(list1) & set(list2)

if len(common) == 0:
    print("The two lists share no common elements.")
else:
    print("The two lists share common elements.")
    print(common)
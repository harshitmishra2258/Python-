dict={}
while True:
    print("\nA. Add a Student")
    print("B. Update Marks")
    print("C. Search for a Student")
    print("D. Display All Students and Marks")
    print("Else. Exit")

    choice = input("Enter your choice: ")

    if choice =="A":
        name = input()
        marks=int(input())
        dict[name]=marks
        print("success")

    elif choice == "B":
        name = input()
        if name in dict:
            marks=int(input())
            dict[name]=marks
        else:
            print("not found")

    elif choice =="C":
        name = input()
        if name in dict:
            print(name,dict[name])
        else:
            print("not found")
    
    elif choice =="D":
        for name in dict:

            print(name,dict[name])
    
    else:
        break



        


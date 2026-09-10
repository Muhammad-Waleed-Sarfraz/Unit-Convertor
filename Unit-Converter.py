print("-----Welcome-----")
print("1. Kilometer to Miles \n2. Miles to Kilometer \n3. Centimeter to Meter \n4. Meter to Centimeter")
choice = input("Which unit you want to convert (1/2/3/4) = ")
if choice in ["1","2","3","4"]:
    distance = float(input("Write the distance = "))
if (choice == "1"):
    kilometer = round(distance*0.62,2)
    print(distance,"Kilometer is equal to",kilometer)
if (choice == "2"):
    miles = round(distance*1.62,2)
    print(distance,"Miles are equal to",miles)
if (choice == "3"):
    CM = round(distance*0.01,2)
    print(distance,"Centimeter are equal to",CM)
elif(choice=="4"):
    M = round(distance*100,2)
    print(distance,"Meter's are equal to",M)

else:
    print("------Invalid Choice------")
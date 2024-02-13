mathematic =int (input("mathematic"))

if mathematic < 0 or mathematic > 100:
    print("invalid i nput")

english =int (input("english"))

if english < 0 or english > 100:
    print("invalid input")


kiswahili =int (input("kiswahili"))

if kiswahili < 0 or kiswahili > 100:
    print("invalid input")

history =int (input("history"))

if history < 0 or history > 100:
    print("invalid input")

physics =int (input("physics"))

if physics < 0 or physics > 100:
    print("invalid input")


total = (mathematic+english+kiswahili+history+physics)

average =(total/5)

print(f"Average:{average}")


if average >= 71:
    print("A")

elif average >=61:
    print("B")

elif average>=51:
    print("C")

elif average>=40:
    print("D")

else:
    print("E")


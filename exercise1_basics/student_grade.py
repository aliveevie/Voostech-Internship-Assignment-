mark=int(input("Enter Mark: "))
if(mark>70 and mark<=100):
    print("your grade is A")
elif(mark>=60 and mark<=69):
    print("your grade is B")
elif(mark>=50 and mark<59):
    print("Your grade is C")
elif(mark>=40 and mark<49):
    print("your grade is D")
elif(mark>=0 and mark<39):
    print("your grade is F")
else:
    print("Invalid Answer!")

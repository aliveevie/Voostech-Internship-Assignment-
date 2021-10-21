marks = int(input('Enter your marks: '))
if (marks>70 and marks<=100):
    print('Your grade is A Excellent')
elif (marks>=60 and marks <=69):
    print('Your grade is B Very Good')
elif (marks>=50 and marks <59):
    print('Your grade is C Good')
elif (marks>=40 and marks <49):
    print('Your grade is D Pass')
elif (marks>=0 and marks <39):
    print('Your grade is F Fail')
else:
    print('Invalid Result')

#find out obtained grade in exam using if-elid-else
marks = int(input("Enter the marks?"))
if marks>85 and marks <=100:
    print("congrats! you scored grade A...")
elif marks>60 and marks <=85:
    print("YOu scored grade B+..")
elif marks>=40 and marks<=60:
    print("You scored grade B...")
elif marks>=50 and marks<=70:
    print("you scored grade c..")
else:
    print("sorry! you are fail...")
    
q=['What is the name of owner this pc:-','who is the programer of this program:-','who is most closest to the owner\'s heart:-','who is the first love of programer:-','what is the name of programer father:-','birth year of owner','favrate digit:-','favraite number(or bad date) of owner:-','owner have gail stocks:-','how much stocks have owner:-']
ans=['shashank','shashank','brother','om','dinesh','2003','8','3817','yes','151']
a=0
for i in range (10):
    print(q[i])
    uans=input("enter the answer:- ")
    if (uans==ans[i]):
        a=a+10
    else:
        continue
print("total score:-",a)
if(a==100):
    print("you win".center(100))
else:
    print("Sorry you lose".center(100))
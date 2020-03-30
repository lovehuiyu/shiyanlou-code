N =10
sum=0
count=0
print("please input 10numbers:")
while count<N:
    number=float(input())
    sum=sum+number
    count=count+1
average=sum/N
print("N={},sum = {}".format(N,sum))
print("Averae = {:.2f}".format(average))

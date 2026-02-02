def transform_number(n,m):
    if n!=0 and m==0:
        return -1
    if n==m:
        return 0
    division=m/n
    numberdivisibleby2=0
    numberdivisibleby3=0
    while division%2==0:
        division=division/2
        numberdivisibleby2+=1
    while division%3==0:
        division=division/3
        numberdivisibleby3+=1
    if division!=1:
        return -1
    else:
        return numberdivisibleby2+numberdivisibleby3
n,m=map(int,input().split())
result=transform_number(n,m)
print(result)

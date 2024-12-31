n=int(input("donner un nbr"))
count = 0
for i in range(2,n):
    if n%i==0:
        count+=1
if count!= 1 and n>1:
    print(f"le nombre {n}premier")
else:
    print(f"le nombre {n}est non premier")

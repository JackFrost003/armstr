n=int(input())
lenght=len(list(str(n)))
m=n
sum=0
for i in range(lenght):
  a=int(m%10)
  sum+=(a**lenght)
  m=int(m/10)


#print("HI")
print(sum)
for i in range(0,1):
    pass
print("Hi")
print(f'the armstorng={sum}')



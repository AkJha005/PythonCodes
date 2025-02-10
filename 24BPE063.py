#Prac-3 Q1
a=int(input('Enter 1st No. :-'))
b=int(input('Enter 2nd No. :-'))
if a>b:
  print(a,'is Bigger')
else:
  print(b,'is Bigger')

#Prac-3 Q2
a=int(input('Enter 1st No. :-'))
b=int(input('Enter 2nd No. :-'))
c=int(input('Enter 3rd No. :-'))
if a>b>c:
  print(a,'is Bigger')
elif b>c>a:
  print(b,'is Bigger')
else:
  print(c,'is Bigger')

#Prac-3 Q3
a=int(input('Enter the No. :-'))
if (a%2==0):
  print(a,'is Even')
else:
  print(a,'is Odd')

#Prac-3 Q4
a=int(input('Enter the No. :-'))
if (a%10==0):
  print(a,'is Divisible by 10')
else:
  print(a,'is not Divisible by 10')

#Prac-3 Q5
a=int(input('Enter the age of the person :-'))
if (a>18):
  print('The person is a Minor')
else:
  print('The person is a Major')

#Prac-3 Q6
a=int(input('Enter the No. you want to count :-'))
count=0
while a!=0:
  a//=10
  count=count+1
print('No. of Digits :-'+str(count))  

#Prac-3 Q7
a=int(input('Enter the No. you want to count :-'))


#Prac-1 Q1
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("Addition:", a+b)

#Prac-1 Q2
print("Subtraction:", a-b)

#Prac-1 Q3
print("Multiplication:", a*b)

#Prac-1 Q4
print("Division:", a/b)

#Prac-1 Q5
print("Add, Multiply, Subtract, Divide:", a+b, a*b, a-b, a/b)

#Prac-1 Q6
hours=int(input("Enter hours:-"))
print("Minutes:",hours*60)

#Prac-1 Q7
minutes=int(input("Enter minutes:-"))
print("Hours:", minutes/60)

#Prac-1 Q8
dollars=float(input("Enter dollars:-"))
print("Rs:", dollars*48)

#Prac-1 Q9
rupees=float(input("Enter Rs:-"))
print("Dollars:",rupees/48)

#Prac-1 Q10
dollars=float(input("Enter dollars:-"))
print("Pounds:",(dollars*48)/70)

#Prac-1 Q11
grams=float(input("Enter grams:-"))
print("Kgs:", grams/1000)

#Prac-1 Q12
kgs=float(input("Enter kgs:-"))
print("Grams:", kgs*1000)

#Prac-1 Q13
bytes=float(input("Enter bytes:-"))
print("KB:",bytes/1024)
print("MB:",bytes/(1024**2))
print("GB:",bytes/(1024**3))

#Prac-1 Q14
celsius=float(input("Enter Celsius:-"))
print("Fahrenheit:",(9/5*celsius)+32)

#Prac-1 Q15
fahrenheit=float(input("Enter Fahrenheit:-"))
print("Celsius:",(5/9)*(fahrenheit-32))

#Prac-1 Q16
p=float(input("Enter principal:-"))
r=float(input("Enter rate:-"))
n=float(input("Enter time:-"))
interest=(p*r*n)/100
print("Interest:",interest)

#Prac-1 Q17
length=float(input("Enter length of square:-"))
area_square=length**2
perimeter_square=4*length
print("Area of square:",area_square)
print("Perimeter of square:",perimeter_square)

#Prac-1 Q18
length=float(input("Enter length of rectangle:-"))
breadth=float(input("Enter breadth of rectangle:-"))
area_rectangle=length*breadth
perimeter_rectangle=2*(length+breadth)
print("Area of rectangle:",area_rectangle)
print("Perimeter of rectangle:",perimeter_rectangle)

#Prac-1 Q19
radius=float(input("Enter radius of circle:-"))
area_circle=(22/7)*radius*radius
print("Area of circle:",area_circle)

#Prac-1 Q20
height=float(input("Enter height of triangle: "))
length=float(input("Enter length of triangle: "))
area_triangle=(height*length)/2
print("Area of triangle:", area_triangle)

#Prac-1 Q21
gross_salary=float(input("Enter gross salary:-"))
allowance=gross_salary*0.10
deduction=gross_salary*0.03
net_salary=gross_salary+allowance-deduction
print("Net Salary:",net_salary)

#Prac-1 Q22
gross_sales=float(input("Enter gross sales:-"))
net_sales=gross_sales-(gross_sales*0.10)
print("Net Sales:", net_sales)

#Prac-1 Q23
subject1=float(input("Enter marks for subject 1:-"))
subject2=float(input("Enter marks for subject 2:-"))
subject3=float(input("Enter marks for subject 3:-"))
total=subject1+subject2+subject3
average=total/3
print("Total:",total)
print("Average:",average)

#Prac-1 Q24
x=float(input("Enter first value:-"))
y=float(input("Enter second value:-"))
x,y=y,x
print("Swapped values:",x,y)
#Prac-2 Q1
a=int(input('Enter 1st No. :-'))
b=int(input('Enter 2nd No. :-'))
if a>b:
  print(a,'is Bigger')
else:
  print(b,'is Bigger')

#Prac-2 Q2
a=int(input('Enter 1st No. :-'))
b=int(input('Enter 2nd No. :-'))
c=int(input('Enter 3rd No. :-'))
if a>b>c:
  print(a,'is Bigger')
elif b>c>a:
  print(b,'is Bigger')
else:
  print(c,'is Bigger')

#Prac-2 Q3
a=int(input('Enter the No. :-'))
if (a%2==0):
  print(a,'is Even')
else:
  print(a,'is Odd')

#Prac-2 Q4
a=int(input('Enter the No. :-'))
if (a%10==0):
  print(a,'is Divisible by 10')
else:
  print(a,'is not Divisible by 10')

#Prac-2 Q5
a=int(input('Enter the age of the person :-'))
if (a>18):
  print('The person is a Minor')
else:
  print('The person is a Major')

#Prac-2 Q6
a=int(input('Enter the No. you want to count :-'))
count=0
while a!=0:
  a//=10
  count=count+1
print('No. of Digits :-'+str(count))  

#Prac-2 Q7
a=int(input('Enter the Year :-'))
if a%4==0:
  print(a,"is Leap Year")
else:
  print(a,"is not a Leap Year")

#Prac-2 Q8
a=int(input("Enter The First Angle of the Triangle :-"))
b=int(input("Enter The Second Angle of the Triangle :-"))
c=int(input("Enter The Third Angle of the Triangle :-"))
if a+b+c==180:
  print("The Triangle is Valid")
else:
  print("The Triangle is Invalid")

#Prac-2 Q9
a=int(input("Enter a No.:-"))
b=abs(a)
print("The absolute value of",a,"is",b)

#Prac-2 Q10
l=int(input("Enter the length of the Rectangle:-"))
b=int(input("Enter the breadth of the Rectangle:-"))
a=l*b
p=2*(l+b)
if a>p:
    print(f"The area of the rectangle",a,"is greater than its perimeter",p)
else:
    print(f"The area of the rectangle",a,"is not greater than its perimeter",p)

#Prac-2 Q11
x1=float(input("Enter x1 :-"))
y1=float(input("Enter y1 :-"))
x2=float(input("Enter x2 :-"))
y2=float(input("Enter y2 :-"))
x3=float(input("Enter x3 :-"))
y3=float(input("Enter y3 :-"))
if (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
    print("The points are collinear")
else:
    print("The points are not collinear")

#Prac-2 Q12
cx=float(input("Enter the center of the circle x:-"))
cy=float(input("Enter the center of the circle y:-"))
r=float(input("Enter the radius of the circle:-"))
px=float(input("Enter the point coordinates x:-"))
py=float(input("Enter the point coordinates y:-"))
d=(px-cx)**2+(py-cy)**2
if d<r**2:
    print("The point lies inside the circle")
elif d==r**2:
    print("The point lies on the circle")
else:
    print("The point lies outside the circle")

#Prac-2 Q13
n=int(input("Enter a number between 0 and 19:-"))
words=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
if 0<=n<=19:
    print(words[n])
else:
    print("Number out of range")

#Prac-2 Q14
a=float(input("Enter marks for subject 1:-"))
b=float(input("Enter marks for subject 2:-"))
c=float(input("Enter marks for subject 3:-"))
total=a+b+c
average=total/3
if a<0 or b<0 or c<0:
    result="Absent"
    grade1="NA"
    grade2="NA"
    grade3="NA"
else:
    if a<=39:
        result="Fail"
        grade1="F"
    elif a<=44:
        grade1="P"
    elif a<=49:
        grade1="C"
    elif a<=54:
        grade1="B"
    elif a<=59:
        grade1="B+"
    elif a<=69:
        grade1="A"
    elif a<=79:
        grade1="A+"
    else:
        grade1="O"
    
    if b<=39:
        result="Fail"
        grade2="F"
    elif b<=44:
        grade2="P"
    elif b<=49:
        grade2="C"
    elif b<=54:
        grade2="B"
    elif b<=59:
        grade2="B+"
    elif b<=69:
        grade2="A"
    elif b<=79:
        grade2="A+"
    else:
        grade2="O"
    
    if c<=39:
        result="Fail"
        grade3="F"
    elif c<=44:
        grade3="P"
    elif c<=49:
        grade3="C"
    elif c<=54:
        grade3="B"
    elif c<=59:
        grade3="B+"
    elif c<=69:
        grade3="A"
    elif c<=79:
        grade3="A+"
    else:
        grade3="O"
    
    if result!="Fail":
        result="Pass"

grades=grade1+" "+grade2+" "+grade3
print("Total:",total)
print("Average:",average)
print("Result:",result)
print("Grades:",grades)

#Prac-3 Q1
a=input("Enter a string:-")
vowels="aeiouAEIOU"
count=0
for char in a:
 if char in vowels:
  count+=1
print("Number of vowels :-",count)

#Prac-3 Q2
s=input("Enter a string :-")
lower=s.lower()
upper=s.upper()
toggle=""
for char in s:
    if char.islower():
        toggle += char.upper()
    elif char.isupper():
        toggle += char.lower()
    else:
        toggle += char
print("Lower case :-",lower)
print("Upper case :-",upper)
print("Toggle case :-",toggle)

#Prac-3 Q3
s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
if s1 in s2:
 print(s1,"is present in",s2)
else:
 print(s1,"is not present in",s2)

#Prac-3 Q4
s1=input("Enter the main string:-")
s2=input("Enter the string to remove:-")
result=""
i=0
while i<len(s1):
 if s1[i:i+len(s2)]==s2:
  i+=len(s2)
 else:
  result+=s1[i]
  i+=1
print("Final string:",result)

#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def area(r):
    pi=3.14
    return(4*pi*r*r)
radius=int(input("Enter radius of sphere "))
print('area of sphere is ',area(radius))

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect(num):
    n=0
    for i in range (1,num):
        if(num%i==0):
            n=n+i
    if(n==num):
        print(num,'is perfect number')
for i in range (1,1001):
    perfect(i)

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
n=int(input("enter number to print it's multiplicatin table "))
for i in range (1,11):
    print(i,'*',n,'=',n*i)

#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(num,n):
    if(n==1):
       return(num*1)
    else:
       return(num*(power(num,n-1)))
num=int(input('enter number to calculate it\'s power '))
n=int(input('enter another number '))              
print('power of number ',num ,'raised to ',n,' is',power(num,n))



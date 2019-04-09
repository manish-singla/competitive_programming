#Problem Link: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
#Solution Author: Manish Singla 
#Linkedin url: https://www.linkedin.com/in/programmermanish/
#Date: 07/04/2019

####Solution Approach: Constructive####
#For each input number n i.e. 54384, we can reaplce all 4's in this number with 1's and then add a 3 to repective places.
#54584 can be written as:
#41581 +
#03003

####Code####
t=int(input()) # there are t test cases
for j in range(0,t): # for each test case
    n=input() #input number as n
    a=n.replace('4','1') # a is calculated  by replacing all 4's with 1's
    #steps to find b for each nth value
    l=len(n)  #
    b=0
    for i in n:
        if(i == '4'):
            b=b*10+3
        else:
            b=b*10    
    print("Case #{0}: {1} {2}".format(j+1,a,b))

#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=2345
#Create a variable "sum_even" and assign it 0.
sum_odd=0
#Find the sum of the odd digits in the variable "var_int".
a=var_int%10
b=var_int//10%10
c=var_int//100%10
d=var_int//1000
sum_odd=(((a%2)*a)+((b%2)*b)+((c%2)*c)+((d%2)*d))

#A four-digit integer is given. Find the number of even digits in it.
a=2345
x1=a%10
x2=a//10%10
x3=a//100%10
x4=a//1000
var_int=((x1+1)%2)+((x2+1)%2)+((x3+1)%2)+((x4+1)%2)
print(var_int)

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
#int division - drops a decimal when divididng floats
dec_numb = 20.5
dec_numb2 = 10.3
int_div_answer = dec_numb // dec_numb2
print(int_div_answer)

#modulo or modulus operator. Divides two numbers and the remainder 
mod1 = 5
mod2 = 2
mod_answer = mod1 % mod2
print(mod_answer)

#expontents **
print(2 ** 8)

#string can only be added or concatonated (combined)
string1 = "8"
string2 = "9"
print(string1 + string2)

#all inputs come in as strings
#therefore you can not calculate them like normal 
#so we have to convert those string to other numerical types like float or int
#there are built in functions to help us convert

# int() - converts in int
# float() - converts to float

#one of the cool things about python is that functions are first class citizens
#this means that you can use functions inside of other functions 
#chain functions 

number1 = int(input("give me your first number to add "))
number2 = int(input("give me your second number to add "))
answer = number1 + number2
print(answer)

float1 = int(input("give me a number to multipy"))
float2 = int(input("give me a number to multiply"))

print(float1 * float2)
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

# Approach 1: 
def solution(num1,num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))
            
print(solution(num1,num2))

#Approach2 
#Given a string of length one, the ord() function returns an integer representing the Unicode code point of the character 
#when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10        

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)
print(solution(num1, num2))
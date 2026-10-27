#even number function
def is_even(n):
    return n%2==0
print(is_even(4))
print(is_even(7))
print(is_even(0))


#find vowels in dtring
def count_vowels(s):
    vowels="aeiou"
    count=0
    for i in s.lower():
        if i in vowels:
            count=count+1
    return count
print(count_vowels("education"))
print(count_vowels(""))
print(count_vowels("AEIOU"))


#find max in string
def max_of_list(num):
    big=num[0]
    for i in num:
     if(i >big):
        big=i
    return big
print(max_of_list([10,20,40,60]))
print(max_of_list([3, 8, 1, 9, 4]))
print(max_of_list([-5, -2, -9]))



#reverse the string using loop
#reverse
def reverse_string(s):
    reverse=""
    for letter in s:
        reverse=letter+reverse
    return reverse
print(reverse_string("abc"))
print(reverse_string("hello"))
print(reverse_string(""))



#find factorialdef fact(n):
   
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))
print(factorial(0))


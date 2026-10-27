def is_even(n):
    return n%2==0

def count_vowels(s):
    vowels="aeiou"
    count=0
    for i in s.lower():
        if i in vowels:
            count=count+1
    return count


print(is_even(4))
print(is_even(7))
print(is_even(0))
print(count_vowels("education"))
print(count_vowels(""))
print(count_vowels("AEIOU"))
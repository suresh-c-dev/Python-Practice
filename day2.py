#Leap year function
def is_leap_year(year):
    if year % 4==0:
        if year % 100==0:
           if year % 400==0:
              return True
           else:
              return False
        else:
            return True
    else:
        return False
print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2023))



#Marks Grade Function
def marks_grade(marks):
    if marks >=90:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "F"
print(marks_grade(76))
print(marks_grade(90))
print(marks_grade(89))
print(marks_grade(75))
print(marks_grade(74))
print(marks_grade(50))
print(marks_grade(49))
print(marks_grade(0))
print(marks_grade(100))



#Find Biggest no function
def biggest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and  b>=c:
        return b
    else:
        return c

print(biggest_of_three(10,10,40))
print(biggest_of_three(5, 5, 3))
print(biggest_of_three(3, 5, 5))
print(biggest_of_three(5, 3, 5))
print(biggest_of_three(7, 7, 7))





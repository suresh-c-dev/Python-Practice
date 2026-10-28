                                #string functions
#1 
def first_and_last(text):
    ltr1=text[0]
    ltr2=text[-1]
    final_txt=ltr1+ltr2
    print(ltr1)
    print(ltr2)
    return final_txt

print(first_and_last("Pyhton")=="Pn")
print(first_and_last("Uday")=="Uy")


#2
def second_and_second_last(txt):
    ltr1=txt[1]
    ltr2=txt[-2]
    return txt[1]+txt[-2]
print(second_and_second_last("pyhton")=="yo")  
print(second_and_second_last("uday")=="dy")  


#3
def shout(text):
    replace_txt=text.replace(" ","-")
    return replace_txt.upper()
print(shout("hello world")=="HELLO-WORLD")
print(shout("python")=="PYTHON")


#4
def make_slug(text):
    replaced_txt=text.replace(" ","-")
    removed_txt=replaced_txt.replace("!","")
    return removed_txt.lower()
print(make_slug("HELLO WORLD!")=="hello-world")
print(make_slug("Python Is Fun!!")=="python-is-fun")


#5
def count_words(text):
   split_str=str.split(text)
   return len(split_str)
print(count_words("i  love python")==3)
print(count_words("hello")==1)


#6
def second_item(text):
    split_txt=text.split(",")
    return split_txt[1]
print(second_item("a,b")=="b")
print(second_item("red,green,blue")=="green")


#7
def remove_ends(text):
    return text[2:-1]
print(remove_ends("python")=="tho")
print(remove_ends("Uday")=="a")


#8
def trim_two(text):
    return text[2:-2]
print(trim_two("python")=="th")
print(trim_two("Uday")=="")
print(trim_two("ab")=="")

                        #list
#1
def add_and_clean(items):
    items.remove("a")
    items.append("z")
    return items
print("add_and_clean test1: ",add_and_clean(["a","b","c"])==["b","c","z"])
print("add_and_clean test2: ",add_and_clean(["a","x"])==["x","z"])


#2
def fix_list(items):
    items[0]="Start"
    items.append("End")
    return items
print("fix_list test 1: ",fix_list(["A","B",])==["Start","B","End"])
print("fix_list test 2: ",fix_list(["X"])==["Start","End"])


#3
def top_two(nums):
    nums.sort(reverse=True)
    return nums[:2]
print("top_two test1: ",top_two([5,1,9,3])==[9,5])
print("top_two test2: ",top_two([2,8])==[8,2])


#4
def bottom_two(items):
    items.sort()
    return items[:2]
print("bottom_two test1: ",bottom_two([5,1,9,3])==[1,3])
print("bottom_two test2: ",bottom_two([8,2])==[2,8])
print("test line: ",9 in [5,1,9,3])


                        #loop for this Topics
#1
def double_sum(nums):
    total=0
    for i in nums:
        total=total+i
    return total*2  
print("double_sum test1: ",double_sum([3,5,2])==20)
print("double_sum test2: ",double_sum([1])==2)
print("double_sum test3: ",double_sum([])==0)


#2
def count_chars(text):
    count=0
    for ch in text:
        count=count+1
    return count
print("count_char test1: ",count_chars("python")==6)
print("count_char test2: ",count_chars("")==0)


                        #Combined Problem
#it is a combination of 
#string,list and loop of 
#today task Day 3
def clean_words(sentance):
    word=sentance.split()
    result=[]
    for ch in word:
        result.append(ch.lower())
    result.sort()
    return result[:3]
    
print("clean_words test1: ",clean_words("Banana apple Cherry date")==['apple', 'banana', 'cherry'])
print("clean_words test2: ",clean_words("Zed Yak")==['yak', 'zed'])
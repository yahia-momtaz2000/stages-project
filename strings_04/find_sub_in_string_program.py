# show all ways to find sub string is found in a string - ignore case
string1 = "Ahmed is a good employee, who works as engineer"

if "ahmed" in string1.lower():
    print("Yes! it is present in the string")
else:
    print("No! it is not present")


# -------------------------------------------
print('----------------------------------------')

# input strings str1 and substr
string = "geeks for geeks"  # or string=input() -> taking input from the user
substring = "geeks"  # or substring=input()

# splitting words in a given string
s = string.split()
if substring in s:
    print("yes")
else:
    print("no")


# -------------------------------------------
print('----------------------------------------')


def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")


# driver code
string = "geeks for geeks"
sub_str = "geek"
check(string, sub_str)


# -------------------------------------------
print('----------------------------------------')


def check(s2, s1):
    if (s2.count(s1) > 0):
        print("YES")
    else:
        print("NO")


s2 = "A geek in need is a geek indeed"
s1 = "geeks"
check(s2, s1)

# -------------------------------------------
print('----------------------------------------')

any_string = "Geeks for Geeks substring "
start = 0
end = 1000
print(any_string.index('substring', start, end))

# -------------------------------------------
print('----------------------------------------')


# Remove all characters except letters and numbers
# initialising string
ini_string = "123abcjw:, .@! eiw"

result = ""
for i in ini_string:
    if i.isalpha() or i.isnumeric():
       result = result + i

print("final string", result)
#  find all the duplicate characters which are similar
#  to each other. Let us look at the example.

input = 'He is Ahmed, Ahmed lives in cairo, Ahmed plays football'

x=[]
for i in input:
    if i not in x and input.count(i)>1:
        x.append(i)
print(" ".join(x))
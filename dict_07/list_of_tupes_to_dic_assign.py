
colors_list = [('red', 201),('blue', 205),('green', 223)]

colors_dict = dict(colors_list)
print(colors_dict)
# ------------ another solution --------
print('-------------  another solution  ------------')
res_dict = {}
for key, val in colors_list:
    res_dict.setdefault(key, val)

print(res_dict)
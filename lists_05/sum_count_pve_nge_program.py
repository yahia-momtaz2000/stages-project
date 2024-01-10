# Ex No. 2 : # get the sum, count of positive, negative and zeros
numbers_list = [15, -16, 20, -3, 0, 20]
sum_positive, sum_negative, count_positive, count_negative, count_zeros = 0, 0, 0, 0, 0

for item in numbers_list:
    if item > 0:
        sum_positive = sum_positive + item
        count_positive = count_positive + 1
    elif item < 0:
        sum_negative = sum_negative + item
        count_negative = count_negative + 1
    else:
        count_zeros = count_zeros + 1

print(sum_positive)
print(count_positive)
print(sum_negative)
print(count_negative)
print(count_zeros)
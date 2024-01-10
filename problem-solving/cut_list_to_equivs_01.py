"""
how to split this list into 2 equivalent lists in summation
input [1,6,2,2,3,4]
output [1,2,6][2,3,4]
"""
def split_equally(input_list):
    input_list.sort(reverse=True)  # Sort the input list in descending order for better distribution
    list1, list2 = [], []
    sum1, sum2 = 0, 0

    for num in input_list:
        if sum1 <= sum2:
            list1.append(num)
            sum1 += num
        else:
            list2.append(num)
            sum2 += num

    return list1, list2

# Example usage:
input_list = [1, 6, 2, 2, 3, 4]
result_list1, result_list2 = split_equally(input_list)
sum_list1 = sum(result_list1)
sum_list2 = sum(result_list2)
if sum_list1 != sum_list2:
    print(f"The sums of the two resulting lists are not equal:")
    print(f"List 1: {result_list1} - Sum: {sum_list1}")
    print(f"List 2: {result_list2} - Sum: {sum_list2}")
else:
    print("The sums of the two resulting lists are approximately equal.")

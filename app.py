from utils import pipe, flatten, sum_list, flatten_and_sum, flatten_and_product

input = [[1, 2], [3, 4], 5]

sum_output = flatten_and_sum(input)
product_output = flatten_and_product(input)


print("The data is:", input)  # Output: The data is: [[1, 2], [3, 4], 5]
print("The sum result is:", sum_output)  # Output: The result is: 15
print("The product result is:", product_output)  # Output: The result is: 120

#Write a function that takes an array of integers and an integer as parameters.
#The function should return the indexes of two numbers in the array, which summed up equal to the value of the second parameter of the function (the integer). 
#The function doesn't need to find all possible combinations; finding one is enough. You can assume that there will always be a valid pair in the array.
# Examples:
# Input: [2, 3, 8, 5], 10
# Output: [0, 2]

# Input: [6, 2, 7, 1], 8
# Output: [0, 1] or [2, 3]

# Input: [2, 15, 3, 0], 15
# Output: [1, 3]
def solution(arr: list, n: int):
    first = arr[0]
    count = 0
    while True:
        for i in arr[1:]:
            total = 0
            total += i + first
            if total == n:
                return [arr.index(first), arr.index(i)]
        count += 1
        first = arr[count]


print(solution([2, 2, 4, 1, 3], 7))

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
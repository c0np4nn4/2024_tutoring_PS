#using hash map dictionary
def count_pairs(arr, n, x):
    num_dict = {}
    count=0

    for num in arr:
        target = x -num
        if target in num_dict:
            count += 1
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    return count

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(count_pairs(arr, n, x))

s = input("").encode()
cnt_arr = [0] * 26

for c in s:
    cnt_arr[int(c) - int.from_bytes(b'a')] += 1

for n in cnt_arr:
    print(n, end=' ')
print()

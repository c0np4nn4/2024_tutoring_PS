A,B,C = map(int, [input().strip() for _ in range(3)])

result = A*B*C

result_str = str(result)

cnt = [0]*10

#cnt the occurance of each digit
for char in result_str:
    cnt[int(char)] +=1

#print the cnt of each digit from 0 to 9
for i in range(10):
    print(cnt[i])



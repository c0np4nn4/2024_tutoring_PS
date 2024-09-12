import math

N = input().strip()

cnt = [0] * 10

for i in N:
    cnt[int(i)]+=1

#counting needed sets for 6 and 9 
cnt_6_9  = cnt[6] + cnt[9]
sets_cnt_6_9 = math.ceil(cnt_6_9/2)

#find the max num of sets needed for digits 0-5 and 7-9
maximum = max(cnt[:6] + cnt[7:9])

total = max(maximum, sets_cnt_6_9)

print(total)

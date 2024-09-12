S = input().strip()

alphabet_cnt = [0] * 26

for char in S:
    alphabet_cnt[ord(char) - ord('a')] +=1

print(" ".join(map(str, alphabet_cnt)))

#ord converts a char into its corresponding int

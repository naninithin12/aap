def find_good_pairs(strings):
    good_pairs = []
    n = len(strings)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if dp[i][j]:
                break
            if any(c in strings[i] for c in strings[j]):
                dp[i][j] = dp[j][i] = True

    for i in range(n):
        for j in range(i + 1, n):
            if dp[i][j]:
                good_pairs.append((strings[i], strings[j]))

    return good_pairs

# Example input
binary_strings = [
    "1010",
    "0011",
    "1111",
    "1001"
]

result = find_good_pairs(binary_strings)

print("Good pairs of strings:")
for pair in result:
    print(pair)

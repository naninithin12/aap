def subset_sum_recursive(numbers, target, partial=[], partial_sum=0, idx=0):
    if partial_sum == target:
        print("Solution found:", partial)
    if partial_sum >= target or idx == len(numbers):
        return

    for i in range(idx, len(numbers)):
        current_num = numbers[i]
        subset_sum_recursive(numbers, target, partial + [current_num], partial_sum + current_num, i + 1)

# Function to find subsets with the target sum
def find_subset_with_sum(numbers, target_sum):
    subset_sum_recursive(numbers, target_sum)

# Example input
S = [1, 2, 5, 6, 8,9,-1,10]
target_sum = 9

print(f"Finding subsets of {S} that sum up to {target_sum}:")
find_subset_with_sum(S, target_sum)

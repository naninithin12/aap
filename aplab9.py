def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    # Calculate value-to-weight ratio for each item
    val_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    val_per_weight.sort(reverse=True)

    max_value = 0  # Maximum value the knapsack can hold
    current_weight = 0  # Current weight in the knapsack

    for val, weight, val_total in val_per_weight:
        if current_weight + weight <= capacity:
            max_value += val_total
            current_weight += weight
        else:
            remaining_capacity = capacity - current_weight
            max_value += val * remaining_capacity
            break

    return max_value

# Example input
weights = [10, 20, 30]
values = [60, 100, 1200]
knapsack_capacity = 50

max_possible_value = fractional_knapsack(weights, values, knapsack_capacity)
print(f"The maximum value that can be obtained: {max_possible_value}")

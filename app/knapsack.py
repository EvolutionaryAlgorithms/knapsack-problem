def knapsack(capacity, amount, values, weights):
    # Base Case
    if amount == 0 or capacity == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity,
    # then this item cannot be included
    # in the optimal solution
    if weights[amount - 1] > capacity:
        return knapsack(capacity, amount - 1, values, weights)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            values[amount - 1] + knapsack(capacity - weights[amount - 1], amount - 1, values, weights),
            knapsack(capacity, amount - 1, values, weights)
        )

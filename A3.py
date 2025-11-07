def fractional_knapsack(weight, value, capacity):
    n = len(value)
    ratio = []

    # Step 1: Calculate ratio = value/weight
    for i in range(n):
        ratio.append((value[i] / weight[i], weight[i], value[i]))

    # Step 2: Sort by ratio (descending)
    ratio.sort(reverse=True)

    total_value = 0.0

    # Step 3: Pick items
    for r, w, v in ratio:
        if capacity >= w:
            # take the whole item
            capacity -= w
            total_value += v
        else:
            # take only the fraction that fits
            fraction = capacity / w          # how much part fits
            total_value += v * fraction      # take fraction of value
            capacity = 0                     # now bag is full
            break

    return total_value


# Example
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(weight, value, capacity)
print("Maximum value in Knapsack =", max_value)

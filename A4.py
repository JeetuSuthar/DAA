def knapsack_dp(weights,values,capacity):
    n=len(values)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for c in range(1,capacity+1):
            if(c>=weights[i-1]):
                include=values[i-1]+dp[i-1][c-weights[i-1]]
                exclude=dp[i-1][c]
                dp[i][c]=max(include,exclude)
            else:
                dp[i][c]=dp[i-1][c]
    return dp[n][capacity]

values=[60,100,120]
weights=[10,20,30]
capacity=50
max_val=knapsack_dp(weights,values,capacity)
print("maxi",max_val)
